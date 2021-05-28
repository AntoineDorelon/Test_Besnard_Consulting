<template>
  <div id="app">
    <Header />
    <br/>
    <div class="layout">
      <Values />
      <Principles />
    </div>
  </div>
</template>

<script>
import Header from "./components/Header";
import Values from "./components/Values";
import Principles from "./components/Principles";

export default {
  name: 'App',
  components: {
    Principles,
    Values,
    Header,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 6px;
}
.layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
