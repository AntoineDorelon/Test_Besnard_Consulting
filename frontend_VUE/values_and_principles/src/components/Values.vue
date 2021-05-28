<template>
  <div class="list-group">
    <h2> List of Values</h2>
    <small class="text-muted">Number of values : {{Object.keys(values).length}} / 4</small>

    <ValueItem class="list-group-item"
               v-for="value in values"
               :key="value.id"
               :value="value"
               @value-edit="valueEdit($event)"
               @value-delete="valueDelete($event)"
    />
    <br>
    <ValueEdit
        v-if="editedValue"
        :value="editedValue"
    />

    <h5 v-if="Object.keys(values).length < 4">
      <font-awesome-icon class="plus" icon="plus"  />
      Click here the + icon to add another principle
    </h5>
  </div>
</template>

<script>
import ValueItem from "./ValueItem";
import ValueEdit from "./ValueEdit";

export default {
  name: "Values",
  components: {
    ValueEdit,
    ValueItem,
  },
  data() {
    return {
      values: [],
      editedValue: null
    }
  },
  methods: {
    valueEdit(value_id) {
      console.log("movie to edit has id", value_id)
      this.editedValue = this.values.find( value => value.id === value_id)
    },
    valueDelete(value_id) {
      console.log("movie to delete has id", value_id)
      fetch(`http://127.0.0.1:8000/api/values/${value_id}/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then( () => {
        this.values =this.values.filter( value => value.id !== value_id)
      })
      .catch( error => console.log(error))
    },
    getValues() {
      fetch('http://127.0.0.1:8000/api/values/', {
        method: 'GET'
      }).then(response => response.json())
          .then(response => {
            this.values = response;
            if (this.editedValue) {
              this.values.find(value => value.id === this.editedValue);
            }
          })
          .catch(error => console.log(error))
    }
  },
  created() {
    this.getValues()
  }
}
</script>

<style scoped>
.list-group{
  padding-left: 2rem;
  padding-right: 2rem;
}
h5 {
  text-align: left;
  margin-bottom: 0px;
  /*vertical-align: middle;*/
}
.plus {
  color: green;
  font-size: 200%;
  vertical-align: middle;

}
</style>