<template>
  <div>
    <v-row>
      <h3 class="my-10 ml-4 text-uppercase">Contacts</h3>
    </v-row>
    <v-data-table :items-per-page="20" :headers="headers" :items="items">
      <template v-slot:header.actions>
        <v-btn
          class="btn-new"
          tile
          depressed
          @click="createContact()"
        >
          <v-icon>mdi-account-multiple</v-icon>New contact
        </v-btn>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon v-cloak @click="editContact(item)" color="light-blue"
          >mdi-pencil</v-icon
        >
        <v-icon v-cloak @click="deleteContact(item)" color="red"
          >mdi-delete</v-icon
        >
      </template>
    </v-data-table>
    <v-dialog
      v-model="dialogNewContact"
      persistent
      max-width="700"
      clas="border-alert"
    >
      <v-card>
        <v-card-title class="justify-center text-center">
          <h3>{{actionTitle}}</h3>
        </v-card-title>
        <v-form v-model="validUser" @submit.prevent="onSubmit(action)">
          <v-card-text class="justify-center text-center">
            <v-text-field
              v-model="name"
              label="Name"
              required
              :rules="rulesGlobal.name"
            ></v-text-field>
            <v-text-field
              v-model="email"
              label="E-mail"
              :rules="rulesGlobal.email"
              required
            ></v-text-field>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn color="red darken-1" @click="dialogNewContact = false">
              Close
            </v-btn>
            <v-btn color="grey darken-1" :disabled="!validUser" type="submit"> {{actionButton}} </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="dialogDeleteContact"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">
          Are you sure?
        </v-card-title>

        <v-card-text>
          This action can not be undone.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="red darken-1"
            @click="dialog = false"
          >
            No
          </v-btn>

          <v-btn
            color="green darken-1"
            @click="onDelete"
          >
            Yes
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      dialog: false,
      dialogNewContact: false,
      dialogDeleteContact: false,
      src: '',
      name: '',
      email: '',
      validUser: false,
      action: 'create',
      actionButton: 'Create',
      actionTitle: 'Create contact',
      contactSelected: null,
      headers: [
        { text: 'Name', value: 'nombre' },
        { text: 'Email', value: 'email' },
        { text: 'Actions', value: 'actions' },
      ],
      items: [
        {
          id: 1,
          name: 'Emanuel Ceriana',
          email: 'emanuelceriana@gmail.com',
        },
        {
          id: 2,
          name: 'Agustín Osatinsky',
          email: 'aosatinsky@gmail.com',
        },
      ],
    }
  },
  mounted() {
    this.$axios
      .$get("/api/contactos")
      .then((result) => {
        this.items = result.data
      })
  },
  methods: {
    createContact(){
        this.name = null
        this.email = null
        this.actionButton = 'Create'
        this.actionTitle = 'Create contact'
        this.action = 'create'
        this.dialogNewContact = true
    },
    editContact(item) {
        this.name = item.nombre
        this.email = item.email
        this.actionButton = 'Save'
        this.actionTitle = 'Edit contact'
        this.action = 'edit'
        this.contactSelected = item.id
        this.dialogNewContact = true
    },
    deleteContact(item) {
        this.contactSelected = item.id
        this.dialogDeleteContact = true
    },
    onSubmit(action){

        if(action == 'create'){

        this.$axios
          .$post('/api/contactos', {nombre: this.name, email: this.email},{
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(result => {
            this.$axios
              .$get("/api/contactos")
              .then((result) => {
                this.items = result.data
              })
          })
        } else {

          this.$axios
            .$post(`/api/contactos/${this.contactSelected}`, {nombre: this.name, email: this.email},{
              headers: {
                'Content-Type': 'application/json'
              }
            })
            .then(result => {
              this.$axios
                .$get("/api/contactos")
                .then((result) => {
                  this.items = result.data
                })
            })
            
        }
        this.name = null
        this.email = null
        this.dialogNewContact = false;
    },
    onDelete() {

      this.$axios
        .$delete(`/api/contactos/${this.contactSelected}`)
        .then(result => {
          this.$axios
            .$get("/api/contactos")
            .then((result) => {
              this.items = result.data
            })
        })

        this.contactSelected = null
        this.dialogDeleteContact = false
    }
  },
}
</script>
