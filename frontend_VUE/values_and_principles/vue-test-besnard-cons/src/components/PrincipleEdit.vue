<template>
  <div v-if="principle" style="overflow: hidden">
    <p>
      <span style="text-decoration: underline">Principle :</span>&nbsp;
      <label for="description">{{ principle.description }}</label>
      <br />
      <input
        id="description"
        placeholder="Description"
        v-model="localPrinciple.description"
      />
      <button @click="savePrinciple()" type="button" class="btn btn-primary">
        Save the modifications
      </button>
    </p>
  </div>
</template>

<script>
export default {
  name: "PrincipleEdit",
  props: ["principle"],
  data() {
    return {
      localPrinciple: { ...this.principle },
    };
  },
  watch: {
    value: function (newval, oldval) {
      if (newval !== oldval) {
        this.localPrinciple = { ...this.principle };
      }
    },
  },
  methods: {
    savePrinciple() {
      if (this.principle.id) {
        console.log("Principle to edit is :", this.principle.description);
        fetch(`http://127.0.0.1:8000/api/principles/${this.principle.id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            description: this.localPrinciple.description,
          }),
        })
          .then((response) => response.json())
          .then((response) => {
            this.$emit("principleUpdated");
            console.log(response);
          })
          .catch((error) => console.log(error));
      } else {
        fetch(`http://127.0.0.1:8000/api/principles/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            description: this.localPrinciple.description,
          }),
        })
          .then((response) => response.json())
          .then((response) => {
            this.$emit("principleUpdated");
            console.log(response);
          })
          .catch((error) => console.log(error));
      }
    },
  },
};
</script>

<style scoped>
p {
  text-align: left;
}

button {
  margin-left: 2rem;
  margin-bottom: 1rem;
  margin-top: 1rem;
}
</style>
