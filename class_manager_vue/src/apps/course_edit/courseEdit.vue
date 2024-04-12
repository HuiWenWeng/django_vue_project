<template>
    <div>
      This is the page where we are going to edit movie in vuejs, this is cool This is the form coming
      from django, displayed in vue
    </div>
    
    <div>
      <form method="post" class="form">
        <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token" />
        <p>
          <label for="id_name">Name:</label>
          <input type="text" name="name" value="Matrix" maxlength="100" required="" id="id_name" />
        </p>
        <p>
          <label for="id_running_time">Running time:</label>
          <input
            type="hidden"
            name="running_time"
            :value="get_time_string"
            required=""
            id="id_running_time"
          />
          <VueDatePicker
            style="display: inline-block; width: 150px; padding-bottom: 10px; padding-left: 10px"
            v-model="time"
            :time-picker="true"
            enable-seconds
          ></VueDatePicker>
        </p>
  
        <p>
          <label for="id_actors">Actors:</label>
          <select hidden name="actors" required="" id="id_actors" multiple="">
            <option v-for="actor in actor_list" :value="actor.id" selected=""></option>
          </select>
          <multiselect
            v-model="actor_list"
            :options="actor_list_source"
            :multiple="true"
            :close-on-select="false"
            :clear-on-select="false"
            :preserve-search="true"
            placeholder="Choose the actors"
            label="name"
            track-by="name"
            :preselect-first="true"
            style="display: inline-block; width: 300px; padding-bottom: 10px; padding-left: 10px"
          >
            <template slot="selection" slot-scope="{ values, search, isOpen }"
              ><span class="multiselect__single" v-if="values.length" v-show="!isOpen"
                >{{ values.length }} options selected</span
              ></template
            >
          </multiselect>
        </p>
        <p>
          <label for="id_director">Director:</label>
          <input
            type="text"
            name="director"
            value="The Wachowskis"
            maxlength="200"
            required=""
            id="id_director"
          />
        </p>
        <p>
          <label for="id_release_date">Release date:</label>
          <input
            type="hidden"
            name="release_date"
            :value="get_date_string"
            required=""
            id="id_release_date"
          />
          <VueDatePicker
            style="display: inline-block; width: 300px; padding-bottom: 10px; padding-left: 10px"
            v-model="date"
            :enable-time-picker="false"
          ></VueDatePicker>
        </p>
        <button
          type="submit"
          class="btn btn-primary"
          @click.prevent="submit_form"
          :disabled="submitting_form"
        >
          Submit
        </button>
      </form>
    </div>
    <br /><br />
  </template>
  
  <script>
  import VueDatePicker from '@vuepic/vue-datepicker'
  import '@vuepic/vue-datepicker/dist/main.css'
  import Multiselect from 'vue-multiselect'
  
  export default {
    name: 'App',
    components: {
      VueDatePicker,
      Multiselect
    },
    data: function () {
      return {
        csrf_token: ext_csrf_token,
        update_bis_url: ext_update_bis_url,
        form: ext_form,
        movie_dico: ext_movie_dict,
        actor_list_source: ext_actor_list,
        date: this.init_date(ext_movie_dict.release_date),
        time: this.init_time(ext_movie_dict.running_time),
        actor_list: ext_movie_dict.actors,
        submitting_form: false,
        form_error: [],
        form_updated: ''
      }
    },
    methods: {
      convert_date_to_string(dato) {
        const offset = dato.getTimezoneOffset()
        dato = new Date(dato.getTime() - offset * 60 * 1000)
        console.log('date', dato, dato.toISOString())
        return dato.toISOString().split('T')[0]
      },
      init_date(date_string) {
        let dato = new Date(date_string)
        const offset = dato.getTimezoneOffset()
        dato = new Date(dato.getTime() + offset * 60 * 1000)
        return dato
      },
      init_time(time_string) {
        let time_split = time_string.split(':')
        return {
          hours: time_split[0],
          minutes: time_split[1],
          seconds: time_split[2]
        }
      },
      submit_form() {
        let formData = new FormData()
        if (this.submitting_form === true) {
          return
        }
        this.submitting_form = true
        var form = document.createElement('form')
        form.setAttribute('method', 'post')
        let form_data = {
          csrfmiddlewaretoken: this.csrf_token,
          name: this.movie_dico.name,
          running_time: this.get_time_string,
          director: this.movie_dico.director,
          release_date: this.get_date_string
        }
        console.log('actor_list', this.actor_list)
        console.log('form_data', form_data)
        for (var key in form_data) {
          var html_field = document.createElement('input')
          html_field.setAttribute('type', 'hidden')
          html_field.setAttribute('name', key)
          html_field.setAttribute('value', form_data[key])
          form.appendChild(html_field)
          formData.append(key, form_data[key])
        }
        var actor_field = document.createElement('select')
        actor_field.setAttribute('name', 'actors')
        actor_field.setAttribute('id', 'id_actors')
        actor_field.setAttribute('multiple', '')
        for (var actor of this.actor_list) {
          console.log('actor', actor)
          var option_field = document.createElement('option')
          option_field.setAttribute('value', actor.id)
          option_field.setAttribute('selected', '')
          actor_field.appendChild(option_field)
        }
        form.appendChild(actor_field)
        document.body.appendChild(form)
        form.submit()
        fetch(this.update_bis_url, {
          method: 'post',
          body: formData,
          headers: { 'X-CSRFToken': this.csrf_token },
          credentials: 'same-origin'
        })
      },
      submit_form_fetch() {
        this.form_error = []
        this.form_updated = ''
        let formData = new FormData()
        let form_data = {
          name: this.movie_dico.name,
          running_time: this.get_time_string,
          director: this.movie_dico.director,
          release_date: this.get_date_string
        }
        for (var key in form_data) {
          formData.append(key, form_data[key])
        }
        this.actor_list.map((dic) => formData.append('actors', dic.id))
        fetch(this.update_bis_url, {
          method: 'post',
          body: formData,
          headers: { 'X-CSRFToken': this.csrf_token },
          credentials: 'same-origin'
        })
          .then(function (response) {
            console.log('response', response)
            return response.json()
          })
          .then(this.handleResponse)
          .catch((error) => {
            console.log('error', String(error))
            this.form_error = ['error']
          })
      },
      handleResponse(response) {
        console.log('json response', response)
        if ('success' in response) {
          if (response['success'] == true) {
            this.form_updated = 'Movie has been updated'
          } else {
            if ('errors' in response) {
              for (const [key, value] of Object.entries(response['errors'])) {
                for (const error of value) {
                  this.form_error.push(`${key}: ${error}`)
                }
              }
            } else {
              this.form_error = [
                'Update failed - An error occurred but do not have more information about it'
              ]
            }
          }
        } else {
          this.form_error = ['Update failed - It has been an error on the form request']
        }
      }
    },
    computed: {
      get_date_string() {
        if (this.date == null) {
          return ''
        } else {
          return this.convert_date_to_string(this.date)
        }
      },
      get_time_string() {
        if (this.time == null) {
          return ''
        } else {
          return `${this.time.hours}:${this.time.minutes}:${this.time.seconds}`
        }
      }
    }
  }
  </script>
  <style src="vue-multiselect/dist/vue-multiselect.css"></style>
  