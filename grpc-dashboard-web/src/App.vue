<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>

<script>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { GreeterClient } from '@/generated/helloworld.client'
import { HelloReply, HelloRequest } from '@/generated/helloworld';
import { GrpcWebFetchTransport } from '@protobuf-ts/grpcweb-transport';


export default {
  data() {
    return {
      responseMessage: ''
    };
  },
  methods: {
    sayHello() {

      let transport = new GrpcWebFetchTransport({baseUrl: "http://localhost:5050"})

      
      const client = new GreeterClient(transport);
      const helloRequest = HelloRequest.create({"name" : "World!"})
      const result = client.sayHello(helloRequest)

      // async function loadModule() {
      //   const {GreeterClient} = await import('./generated/HelloworldServiceClientPb');
      //   const {HelloRequest} = await import('./generated/helloworld_pb');
      //   const client = new GreeterClient('http://localhost:8080', null, null);

      //   const request = new HelloRequest();
      //   request.setName('World');

      //   client.sayHello(request, {}, (err, response) => {
      //     if (err) {
      //       console.error(err);
      //     } else {
      //       // this.responseMessage = response.getMessage();
      //     }
      //   });
      // }
      // // 모듈 사용
      // loadModule();
    }
  },
  created() {
      this.sayHello();
  },
};

</script>
