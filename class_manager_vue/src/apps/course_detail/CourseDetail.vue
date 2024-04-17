
<template>
  <a :href="this.course_list_url">Course List</a><br />
  <a :href="this.course_update_url">Update course</a><br />
  <a :href="this.course_delete_url">Delete course</a><br />
  <h1>{{ this.course.name }}</h1>
  Teacher: {{ this.course.teacher }}<br />
  Grade Level: {{ this.course.grade }}<br />
  Students:<br />
  <span v-for="student in this.course.students"> {{ student.name }}<br /></span>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
        course_error: [],
        course_id: ext_course_id,
      course_detail_js_url: ext_course_detail_js_url,
      course_list_url: window.ext_course_list_url,
      course_update_url: window.ext_course_update_url,
      course_delete_url: window.ext_course_delete_url,
      course: {} 
    }
  },
  methods: {
    course_error: [],
      get_course_info() {
        fetch(this.course_detail_js_url, {
            method: 'get',
            credentials: 'same-origin'
        })
        .then(function (response) {
            console.log('response', response)
            return response.json()
        })
        .then(this.assign_course)
        .catch((error) => {
            console.log('error', error)
            this.course_error = ['error when loading course information']
        })
    },
    assign_course(course_json) {
      console.log('json', course_json)
      this.course = course_json['course']
    },
  },
  beforeMount() {
    this.get_course_info()
  }
}
</script>
