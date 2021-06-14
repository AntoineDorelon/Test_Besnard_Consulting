<template>
  <div class="list-group">
    <h2>List of Values</h2>
    <small class="text-muted"
      >Number of values : {{ Object.keys(values).length }} / 4</small
    >

    <ValueItem
      class="list-group-item"
      v-for="value in values"
      :key="value.id"
      :value="value"
      @ValueEdit="valueEdit($event)"
      @ValueDelete="valueDelete($event)"
    />
    <br />
    <ValueEdit
      v-if="editedValue"
      :value="editedValue"
      @ValueUpdated="refreshValues()"
    />

    <h5 v-if="Object.keys(values).length < 4">
      <font-awesome-icon class="plus" :icon="PlusIcon" @click="newValue()" />
      Click the "+" icon to add another value
    </h5>
  </div>
</template>

<script>
import ValueItem from "./ValueItem";
import ValueEdit from "./ValueEdit";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faPlus } from "@fortawesome/free-solid-svg-icons";

export default {
  name: "Values",
  components: {
    ValueEdit,
    ValueItem,
    FontAwesomeIcon,
  },
  data() {
    return {
      values: [],
      editedValue: null,
      PlusIcon: faPlus,
    };
  },
  methods: {
    valueEdit(value_id) {
      console.log("value to edit has id ", value_id);
      this.editedValue = this.values.find((value) => value.id === value_id);
    },
    newValue() {
      this.editedValue = { title: "" };
    },
    valueDelete(value_id) {
      console.log("value to delete has id ", value_id);
      fetch(`http://127.0.0.1:8000/api/values/${value_id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then(() => {
          this.values = this.values.filter((value) => value.id !== value_id);
        })
        .catch((error) => console.log(error));
    },
    getValues() {
      return fetch("http://127.0.0.1:8000/api/values/", {
        method: "GET",
      }).then((response) => response.json());
    },
    refreshValues: async function () {
      this.values = await this.getValues();
    },
  },
  async created() {
    await this.refreshValues();
  },
};
</script>

<style scoped>
.list-group {
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
  cursor: pointer;
}
</style>
