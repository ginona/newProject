from init import app, db, mail
from flask_mail import Message 
from database import Registro
import datetime
from datetime import timedelta
import cv2 as cv
import argparse
import sys
import numpy as np
import os.path
import threading

# Initialize the parameters
confThreshold = 0.45  #Confidence threshold
nmsThreshold = 0.4  #Non-maximum suppression threshold

inpWidth = 416  #608     #Width of network's input image
inpHeight = 416 #608     #Height of network's input image


global dateCompare
dateCompare = datetime.datetime.now() - timedelta(minutes=5)

parser = argparse.ArgumentParser(description='Object Detection using YOLO in OPENCV')
parser.add_argument('--image', help='Path to image file.')
parser.add_argument('--video', help='Path to video file.')
args = parser.parse_args()

# Load names of classes
classesFile = "pistol.names";

classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# Give the configuration and weight files for the model and load the network using them.

modelConfiguration = "yolov4-tiny.cfg";
modelWeights = "yolov4-tiny_best.weights";


net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# Get the names of the output layers
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Draw the predicted bounding box
def drawPred(image, classId, conf, left, top, right, bottom):
    # Draw a bounding box.
    cv.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 1)

    label = '%.2f' % conf

    # Get the label for the class name and its confidence
    if classes:
        assert(classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    #Display the label at the top of the bounding box
    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv.rectangle(image, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (0, 0, 255),1)
    cv.putText(image, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 2)
    
# Calcula la diferencia entre el tiempo actual y el ultimo registro de la base de datos
def getTimeDifference():
    dt = dateCompare
    dt2 = datetime.datetime.now()
    difference = dt2 - dt
    seconds_in_day = 24 * 60 * 60
    datetime.timedelta(0,8,562000)
    return divmod(difference.days * seconds_in_day + difference.seconds, 60)

# Remove the bounding boxes with low confidence using non-maxima suppression
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    classIds = []
    confidences = []
    boxes = []
    # Scan through all the bounding boxes output from the network and keep only the
    # ones with high confidence scores. Assign the box's class label as the class with the highest score.
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        # print("out.shape : ", out.shape)
        for detection in out:
            #if detection[4]>0.001:
            scores = detection[5:]
            classId = np.argmax(scores)
            #if scores[classId]>confThreshold:
            
            confidence = scores[classId]
            if detection[4]>confThreshold:
                # print(detection[4], " - ", scores[classId], " - th : ", confThreshold)
                # print(detection)  
                with app.app_context():
                    
                    result = getTimeDifference()
                        
                    if result > (3,0) and confidence > 0.8:
                        global dateCompare
                        dateCompare = datetime.datetime.now()
                        path = str(hash(dateCompare))
                        registro = Registro(camera_id = "001", accuracy = str(confidence), date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), path=path+".jpg")
                        db.session.add(registro)
                        db.session.commit()
                        print('ARMA DETECTADA CON %r DE PRESICIÓN' % confidence)
                        cv.imwrite('./images/'+path+'.jpg', frame)
                        msg = Message("Hello",sender="alerts@sauron.ar",recipients=["aosatinsky@gmail.com"])
                        f = open("email.html", "r")
                        html = f.read()
                        msg.html = html
                        msg.attach(path+'.jpg','image/jpg',open('./images/'+path+'.jpg', 'rb').read(), 'inline', headers=[['Content-ID','<image>'],])
                        sender = threading.Thread(name='mail_sender', target=send_async_email, args=(app,msg))
                        sender.start()

                        
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Perform non maximum suppression to eliminate redundant overlapping boxes with
    # lower confidences.
    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        # print('--------------')
        # print(i)
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        right=left+width
        bottom=top+height
  
        drawPred(frame ,classIds[i], confidences[i], left, top, right, bottom)
        red=[255,0,0]
        frame = cv.copyMakeBorder(frame,20,20,20,20,cv.BORDER_CONSTANT,value=red)

class VideoCamera(object):
    def __init__(self):
        self.video = cv.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()

        # Create a 4D blob from a frame.
        blob = cv.dnn.blobFromImage(image, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)

        # Sets the input to the network
        net.setInput(blob)

        # Runs the forward pass to get output of the output layers
        outs = net.forward(getOutputsNames(net))

        # Remove the bounding boxes with low confidence
        postprocess(image, outs)

        # Put efficiency information. The function getPerfProfile returns the overall time for inference(t) and the timings for each of the layers(in layersTimes)
        t, _ = net.getPerfProfile()
        # label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
        # image = cv.putText(image, label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
        ret, jpeg = cv.imencode('.jpg', image)
        return jpeg.tobytes()
