<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo">Costo</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo"
                    v-model="departamento.costo"
                    v-validate="'required'"
                    name="costo"
                    placeholder="Ingres costo"
                    :class="{'is-invalid': errors.has('departamento.costo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="numero_cuartos">numero_cuartos</label>
                <input
                    type="text"
                    class="form-control"
                    id="numero_cuartos"
                    v-model="departamento.numero_cuartos"
                    v-validate="'required'"
                    name="numero_cuartos"
                    placeholder="Ingrese numero_cuartos"
                    :class="{'is-invalid': errors.has('departamento.numero_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero_cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="numero_banos">numero_banos</label>
                <input
                    type="text"
                    class="form-control"
                    id="numero_banos"
                    v-model="departamento.numero_banos"
                    v-validate="'required'"
                    name="numero_banos"
                    placeholder="Ingrese numero_banos"
                    :class="{'is-invalid': errors.has('departamento.numero_banos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero_banos.
                </div>
            </div>

            <div class="form-group">
                <label for="valor_alicuota">valor_alicuota</label>
                <input
                    type="text"
                    class="form-control"
                    id="valor_alicuota"
                    v-model="departamento.valor_alicuota"
                    v-validate="'required'"
                    name="valor_alicuota"
                    placeholder="Ingrese valor_alicuota"
                    :class="{'is-invalid': errors.has('departamento.valor_alicuota') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid valor_alicuota.
                </div>
            </div>


            <div class="form-group">
                <label for="propietario">propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
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
            departamento: {
                costo: '',
                numero_cuartos: '',
                numero_banos: '',
                valor_alicuota: '',
                propietario: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getpropietariosList(),
        axios.get('http://127.0.0.1:8000/api/departamentos/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.departamento = response.data
        });
    },
    methods: {
      getpropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietarios/')
            .then(response => {
                this.propietariosList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/departamentos/${this.departamento.id}/`,
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
