<template>
  <div class="">
    <form id="register-form" @submit.prevent="CreateUser">
      <p>
        <label for="username"
          >Username
          <input
            class="ml-2"
            type="text"
            name="username"
            id="username"
            v-model="username"
          />
        </label>
      </p>
      <p>
        <label for="email"
          >Email
          <input
            class="ml-2"
            type="email"
            name="email"
            id="email"
            v-model="email"
          />
        </label>
      </p>
      <p>
        <label for="password1"
          >Password
          <input
            class="ml-2"
            type="password"
            name="password1"
            id="password1"
            v-model="password1"
          />
        </label>
      </p>
      <p>
        <label for="password2"
          >Password
          <input
            class="ml-2"
            type="password"
            name="password2"
            id="password2"
            v-model="password2"
          />
        </label>
      </p>
      <p>
        <input class="ml-2" type="submit" value="Submit" />
      </p>
    </form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "register",
  components: {},
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
      token: localStorage.getItem("user-token") || null,
    };
  },
  methods: {
    CreateUser() {
      axios
        .post("http://localhost:8000/api/v1/register", {
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
        })
        .then((resp) => {
          this.token = resp.data.key;
          console.log(this.username + " register with : " + this.token);
        })
        .catch((err) => {
          if (err.response) {
            var resp_error = Object.values(err.response.data);
            console.log("resp_error", resp_error);
            resp_error.forEach((err) => {
              err.forEach((msg) => {
                console.log(msg);
              });
            });
          }
        });
      this.$router.push({ name: "home" });
    },
  },
};
</script>
