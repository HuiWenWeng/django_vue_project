<template>
    <div>
        This is the form coming from django, displayed in vue. <br><br>
    </div>

    With fetch this time
    <div v-if="form_error">
        <ul>
            <li v-for="(error, index) in form_error">
                {{error}}
            </li>
        </ul>
    </div>
    <div v-if="form_updated">
        {{ form_updated }}
    </div>

    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token">
            <p>
                <label for="id_name">Name:</label><br>
                <input type="text" name="name" maxlength="100" required="" id="id_name">
            </p>
            <p>
                <label for="id_osis">OSIS:</label><br>
                <input type="number" name="osis" maxlength="9" required="" id="id_osis">
            </p>
            <p>
                <label for="id_grade">Grade:</label><br>
                <input type="number" name="grade" required="" id="id_grade">
            </p>
            <p>
                <label for="id_gpa">GPA:</label><br>
                <input type="number" name="gpa" required="" id="id_gpa">
            </p>
            <!-- <button type="submit" class="btn btn-primary" @click.prevent="submit_form" :disabled="submitting_form">Submit</button> -->
            <button type="submit" class="btn btn-primary" @click.prevent="submit_form_fetch" :disabled="submitting_form">Submit</button>
        </form> 
    </div>

</template>
    
<script>
    export default { 
        name: 'App', 
        data: function() {
            return {
                submitting_form: false,
                form_error: [],
                form_updated: "",
                csrf_token: window.ext_csrf_token,
                form: window.ext_django_form,
                student_dico: window.ext_student_dico,
                student_name: window.ext_student_dico.name,
                student_osis: window.ext_student_dico.osis,
                student_grade: window.ext_student_dico.grade,
                student_gpa: window.ext_student_dico.gpa,
                update_bis_url: window.ext_update_bis_url,
            }
        },
        methods: {
            submit_form(){
                if (this.submitting_form === true) {
                return;
                }
                this.submitting_form = true
                var form = document.createElement('form');
                form.setAttribute('method', 'post');
                let form_data = {
                    'csrfmiddlewaretoken': this.csrf_token,
                    'name': this.student_dico.name,
                    'osis': this.student_dico.osis,
                    'grade': this.student_dico.grade,
                    'gpa': this.student_dico.gpa,
                }
                for (var key in form_data) {
                    var html_field = document.createElement('input')
                    html_field.setAttribute('type', 'hidden')
                    html_field.setAttribute('name', key)
                    html_field.setAttribute('value', form_data[key])
                    form.appendChild(html_field)
                }
                document.body.appendChild(form);
                form.submit()
            },
            submit_form_fetch(){
                this.form_error = []
                this.form_updated = ""
                let formData = new FormData();
                let form_data = {
                    'name': this.student_dico.name,
                    'osis': this.student_dico.osis,
                    'grade': this.student_dico.grade,
                    'gpa': this.student_dico.gpa,
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
                            this.form_updated = "Student has been updated"
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
            }
        },
    }
</script>