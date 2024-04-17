<template>

    <div>
        <a :href="this.student_list_url">Student List</a><br/>
        <a :href="this.student_update_url">Update Student</a><br/>
        <a :href="this.student_delete_url">Delete Student</a><br/>
        <h1>{{ this.student.name }}</h1>
        OSIS: {{ this.student.osis }}<br/>
        Grade: {{ this.student.grade }}<br/>
        GPA: {{ this.student.gpa }}<br/>
    </div>

</template>
    
<script>
    export default { 
        name: 'App', 
        data: function() {
            return {
                student_error: [],
                student_id: window.ext_student_id,
                student_detail_js_url: window.ext_student_detail_js_url,
                student_list_url: window.ext_student_list_url,
                student_update_url: window.ext_student_update_url,
                student_delete_url: window.ext_student_delete_url,
                student: {},
            }
        },
        methods: {
            get_student_info() {
                fetch(this.student_detail_js_url,
                    {
                        method: "get",
                        credentials: 'same-origin'
                    }
                ).then(function(response) {
                    console.log('response', response)
                    return response.json()}).then(this.assign_student).catch(
                        (error) => { 
                        console.log('error', error)
                        this.student_error=["Error when loading student information"]
                })
            },
            assign_student(student_json) {
                console.log('json', student_json)
                this.student = student_json['student']
            },
            beforeMount() {
                this.get_student_info()
            },
        }, 
    }
</script>