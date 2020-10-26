<template>
  <div class="">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand class="text-white" href="#">Inventory!!</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="login" v-if="token == null">
          <b-form-input
            id="username"
            size="sm"
            class="mr-sm-2"
            v-model="username"
            placeholder="username"
            name="username"
          ></b-form-input>
          <b-form-input
            id="password"
            size="sm"
            class="mr-sm-2"
            placeholder="password"
            type="password"
            v-model="password"
            name="password"
          ></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">
            Login
          </b-button>
        </b-nav-form>

        <b-nav-form @submit.prevent="logout" v-if="token !== null">
          <b-button size="sm" class="my-2 ml-2" type="submit">Logout</b-button>
        </b-nav-form>

        <b-nav-form @submit.prevent="register" v-if="token === null">
          <b-button
            size="sm"
            class="my-2 ml-2"
            type="submit"
            :to="{ name: 'register' }"
            >Register</b-button
          >
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Header",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      token: localStorage.getItem("user-token") || null,
    };
  },

  methods: {
    login() {
      axios
        .post("http://localhost:8000/api/v1/login", {
          username: this.username,
          password: this.password,
        })
        .then((resp) => {
          this.token = resp.data.key;
          console.log(this.username +" logged in with: " + this.token);
          localStorage.setItem("user-token", this.token);
        })
        .catch((err) => {
          console.log(err);
          localStorage.removeItem("user-token");
        });
    },
    logout() {
      axios
        .post("http://localhost:8000/api/v1/logout", {
          key: localStorage.getItem("user-token"),
        })
        .then((resp) => {
          console.log(this.username + " logout in with: " + this.token);
          this.token = resp.data.key;
          localStorage.removeItem("user-token");
          this.token = null;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
