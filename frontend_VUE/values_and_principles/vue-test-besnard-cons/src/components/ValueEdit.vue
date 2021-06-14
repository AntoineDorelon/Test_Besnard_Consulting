<template>
  <div v-if="value">
    <p>
      <span style="text-decoration: underline">Value :</span> &nbsp;
      <label for="title">{{
        value.title.charAt(0).toUpperCase() + value.title.slice(1)
      }}</label>
      <br />
      <input id="title" placeholder="Title" v-model="localValue.title" />
      <button @click="saveValue()" type="button" class="btn btn-primary">
        Save the modifications
      </button>
    </p>
  </div>
</template>

<script>
export default {
  name: "ValueEdit",
  props: ["value"],
  data() {
    return {
      localValue: { ...this.value },
    };
  },
  watch: {
    value: function (newval, oldval) {
      if (newval !== oldval) {
        this.localValue = { ...this.value };
      }
    },
  },
  methods: {
    saveValue() {
      if (this.value.id) {
        console.log("Value to edit is :", this.value.title);
        fetch(`http://127.0.0.1:8000/api/values/${this.value.id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ title: this.localValue.title }),
        })
          .then((response) => response.json())
          .then((response) => {
            this.$emit("ValueUpdated");
            console.log(response);
          })
          .catch((error) => console.log(error));
      } else {
        fetch(`http://127.0.0.1:8000/api/values/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ title: this.localValue.title }),
        })
          .then((response) => response.json())
          .then((response) => {
            this.$emit("ValueUpdated");
            console.log(response);
          })
          .then((this.value = { title: "" }))
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
