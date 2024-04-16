<template>
    <div>
        This is the form coming from django, displayed in vue. <br><br>
    </div>
    
    <div v-if="form_error">
        <li v-for="(error, index) in form_error">
            {{error}}
        </li>
    </div>

    <div v-if="form_updated">
        {{ form_updated }}
    </div>

    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token">
            <p>
                <label for="id_name">Name:</label><br>
                <input type="text" name="name" :value="student_name"  maxlength="100" required="" id="id_name">
            </p>
            <p>
                <label for="id_osis">OSIS:</label><br>
                <input type="number" name="osis" :value="student_osis" maxlength="9" required="" id="id_osis">
            </p>
            <p>
                <label for="id_grade">Grade:</label><br>
                <input type="number" name="grade" :value="student_grade"  required="" id="id_grade">
            </p>
            <p>
                <label for="id_gpa">GPA:</label><br>
                <input type="number" name="gpa" :value="student_gpa" required="" id="id_gpa">
            </p>
            <button type="submit" class="btn btn-primary" @click.prevent="submit_form_fetch" :disabled="submitting_form">Submit</button>
        </form>
    </div>

</template>
    
<script>
import Multiselect from 'vue-multiselect'
    export default { 
        name: 'App', 
        components: {
            Multiselect,
        },
        data: function() {
            return {
                submitting_form: false,
                form_error: [],
                form_updated: "",
                csrf_token: window.ext_csrf_token,
                student_list: window.ext_student_list,
                student_list: window.ext_student_name,
                student_osis: window.ext_student_osis,
                student_grade: window.ext_student_grade,
                student_gpa: window.ext_student_gpa,
            }
        },
        methods: {
            submit_form_fetch(){
                this.form_error = []
                this.form_updated = ""
                let formData = new FormData();
                let form_data = {
                        'name': this.movie_dico.name,
                        'running_time': this.get_time_string,
                        'director': this.movie_dico.director,
                        'release_date': this.get_date_string,
                }
                for (var key in form_data) {
                        formData.append(key, form_data[key])
                }
                fetch(this.update_bis_url,
                    {
                        method: "post",
                        body: formData,
                        headers: {'X-CSRFToken': this.csrf_token},
                        credentials: 'same-origin'
                    }
                ).then(function(response) {
                    console.log('response', response)
                    return response.json()}).then(
                        this.handleResponse).catch(
                            (error) => {
                            console.log('error', String(error))
                            this.form_error=["error"]
                    })
            },
            handleResponse(response) {
                console.log('json response', response)
                if ('success' in response){
                        if (response['success'] == true) {
                            this.form_updated = "Movie has been updated"
                        } else {
                            if ('errors' in response){
                                    for (const [key, value] of Object.entries(response['errors'])) {
                                        for (const error of value) {
                                                this.form_error.push(`${key}: ${error}`)
                                        }
                                    }
                            } else {
                                    this.form_error=["Update failed - An error occurred but do not have more information about it"]
                            }
                        }
                } else {
                            this.form_error=["Update failed - It has been an error on the form request"]
                }
    	    },
        }, 
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

