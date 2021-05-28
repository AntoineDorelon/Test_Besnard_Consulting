<template>
  <div class="list-group">
    <h2>List of principles</h2>
    <small class="text-muted">Number of principles : {{Object.keys(principles).length}} / 12</small>
    <PrincipleItem
        class="list-group-item"
        v-for="principle in principles"
        :key="principle.id"
        :principle="principle"
        @principle-edit="principleEdit($event)"
        @principle-delete="principleDelete($event)"
    />
    <br/>
    <PrincipleEdit
        v-if="editedPrinciple"
        :principle="editedPrinciple"
        @principle-updated="getPrinciples()"
    />
    <br/>
    <h5 v-if="Object.keys(principles).length < 12">
      <font-awesome-icon class="plus" icon="plus"
      @click="newPrinciple()"/>
      Click here the + icon to add another principle
    </h5>


  </div>
</template>

<script>
import PrincipleItem from "./PrincipleItem";
import PrincipleEdit from "./PrincipleEdit";

export default {
  name: "Principles",
  components: {
    PrincipleEdit,
    PrincipleItem
  },
  data() {
    return {
      principles: [],
      editedPrinciple: null
    }
  },
  created() {
    this.getPrinciples()
  },
  methods: {
    principleEdit(principle_id) {
      this.editedPrinciple = this.principles.find( principle => principle.id === principle_id)
      console.log('principle to edit has id ', principle_id)
    },
    newPrinciple() {
      this.editedPrinciple = {description: ''}
    },
    principleDelete(principle_id) {
      console.log('principle to delete has id ',principle_id)
      fetch(`http://127.0.0.1:8000/api/principles/${principle_id}/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      })
          .then( () => {
            this.principles =this.principles.filter( principle => principle.id !== principle_id)
          })
          .catch( error => console.log(error))
    },
    getPrinciples() {
      fetch('http://127.0.0.1:8000/api/principles/', {
        method: 'GET'
      }).then(response => response.json())
          .then(response => this.principles = response)
          .catch(error => console.log(error))
    }
  }
}
</script>

<style scoped>
.list-group{
  padding-left: 1rem;
  padding-right: 1rem;
}
h5 {
  text-align: left;
  margin-bottom: 0px;
}
.plus {
  color: green;
  font-size: 200%;
  vertical-align: middle;

}
</style>