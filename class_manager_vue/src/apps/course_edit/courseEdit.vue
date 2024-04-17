<template>
  <div>This is the course form coming from django, displayed in vue. <br /><br /></div>
  <div>
    <form method="post" class="form">
      <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token" />
      <p>
        <label for="id_name">Name:</label>
        <br />
        <input type="text" name="name" value="Course" maxlength="100" required="" id="id_name" />
        <br /><br />
        <label for="id_teacher">Teacher:</label>
        <br />
        <input
          type="text"
          name="teacher"
          value="Teacher"
          maxlength="100"
          required=""
          id="id_teacher"
        />
        <br /><br />
        <label for="id_name">Grade:</label>
        <br />
        <input type="text" name="grade" value="100" maxlength="100" required="" id="id_grade" />
      </p>
      <!-- <p>
        <label for="id_students">Students:</label>
        <select hidden name="students" required="" id="id_students" multiple="">
          <option v-for="student in student_list" :value="student.id" selected=""></option>
        </select>
        <multiselect
          v-model="student_list"
          :options="student_list_source"
          :multiple="true"
          :close-on-select="false"
          :clear-on-select="false"
          :preserve-search="true"
          placeholder="Choose the students"
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
        </p> -->
    </form>

    <button
      type="submit"
      class="btn btn-primary"
      @click.prevent="submit_form"
      :disabled="submitting_form"
    >
      Submit
    </button>
  </div>student
</template>

<script>
import Multiselect from 'vue-multiselect'
export default {
  name: 'App',
  components: {
    Multiselect
  },
  data: function () {
    return {
      // submitting_form: false,
      form_error: [],
      form_updated: '',
      submitting_form: false,
      csrf_token: window.ext_csrf_token,
      form: window.ext_django_form,
      course_dico: window.ext_course_dico,
      course_name: window.ext_voutdr_dico.name,
      course_teacher: window.ext_course_dico.teacher,
      update_bis_url: window.ext_update_bis_url
    }
  },
  methods: {
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
        name: this.course_dico.name,
        teacher: this.course_dico.teacher,
        grade: this.course_dico.grade
      }
      for (var key in form_data) {
        var html_field = document.createElement('input')
        html_field.setAttribute('type', 'hidden')
        html_field.setAttribute('name', key)
        html_field.setAttribute('value', form_data[key])
        form.appendChild(html_field)
        formData.append(key, form_data[key])
      }
    },
    submit_form_fetch() {
      this.form_error = []
      this.form_updated = ''
      let formData = new FormData()
      let form_data = {
        name: this.course_dico.name,
        teacher: this.course_dico.teacher,
        grade: this.course_dico.grade,
      }
      for (var key in form_data) {
        formData.append(key, form_data[key])
      }
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
          this.form_updated = 'course has been updated'
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
  }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>
