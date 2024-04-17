<template>
    <div>
        This is the course details coming from django, displayed in vue. <br>
    </div>

    <div>
        <form method="post" class="form"></form>
        <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token" /> 
        <p>
        <label for="id_name">Name:</label>
        <input type="text" name="name" value="" maxlength="100" required="" id="id_name" />
      </p>
    </div>
</template>
    
<script>
    export default { 
        name: 'App', 
        components: {
        },
        data: function() {
            return {
            }
        },
        methods: {
        }, 
    }
</script>