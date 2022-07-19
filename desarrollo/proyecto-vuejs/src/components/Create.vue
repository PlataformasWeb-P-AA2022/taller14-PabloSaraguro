<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.nombre"
                    v-validate="'required'"
                    name="nombre"
                    placeholder="Ingres su nombre"
                    :class="{'is-invalid': errors.has('propietario.nombre') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="apellido">Apellido</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.apellido"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su apellido"
                    :class="{'is-invalid': errors.has('propietario.apellido') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="edad">Cédula</label>
                <input
                    type="text"
                    class="form-control"
                    id="edad"
                    v-model="propietario.edad"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su cédula"
                    :class="{'is-invalid': errors.has('propietario.edad') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid edad.
                </div>
            </div>

            <div class="form-group">
                <label for="ciudadania">ciudadania</label>
                <input
                    type="text"
                    class="form-control"
                    id="ciudadania"
                    v-model="propietario.ciudadania"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su ciudadania"
                    :class="{'is-invalid': errors.has('propietario.ciudadania') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid ciudadania.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            propietario: {
                nombre: '',
                apellido: '',
                ciudadania: '',
                edad: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.ciudadania)
                axios.post('http://127.0.0.1:8000/api/propietarios/',
                        this.propietario
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
