from init import cors, socketio, app, db
from flask import render_template, Response, jsonify, send_file, request
from flask_cors import CORS, cross_origin
from database import Registro, Contacto
from camera import VideoCamera

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historial', methods=['GET']) 
@cross_origin()
def foo():
    
    # re = Registro(camera_id = "320", accuracy = "0.4")
    # db.session.add(re)
    # db.session.commit()
    
    db.create_all()
    db.session.commit()
    
    data = db.session.query(Registro).all()
    return jsonify(data=[i.serialize for i in data])

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/contactos", methods=["GET", "POST"])
def contacts():
    if request.form and request.method == "POST":
        contacto = Contacto(nombre=request.form.get("nombre"), email=request.form.get("email"))
        db.session.add(contacto)
        db.session.commit()
        return jsonify(contacto.serialize)
    if request.method == "GET":
        data = db.session.query(Contacto).all()
        return jsonify(data=[i.serialize for i in data]) 

@app.route("/contactos/<id>", methods=["POST", "DELETE", "GET"])
def updateContact(id):
    if request.form and request.method == "POST":
        contacto = Contacto.query.get(id)
        contacto.nombre = request.form.get("nombre")
        contacto.email = request.form.get("email")
        db.session.commit()
        return jsonify(contacto.serialize)
    if request.method == "DELETE":
        contacto = Contacto.query.get(id)
        db.session.delete(contacto)
        db.session.commit()
        return jsonify(contacto.serialize)
    if request.method == "GET":
        contacto = Contacto.query.get(id)
        return jsonify(contacto.serialize)

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route("/images/<path:path>")
def images(path):
    filename = "./images/"+path
    return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app)