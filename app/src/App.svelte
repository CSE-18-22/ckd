<script>
  import Tab from "./lib/UI/Tab.svelte";
  import Home from "./lib/Components/Home.svelte";
  import About from "./lib/Components/About.svelte";
  import Project from "./lib/Components/Project.svelte";

  let items = [
    { label: "Home", value: 1, component: Home },
    { label: "Project", value: 2, component: Project },
    { label: "About", value: 3, component: About },
  ];
</script>

<div class="navbar">
  <h1>Chronic Kidney Disease</h1>
</div>
<Tab {items} />

<style>
  :root {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  }
  .navbar {
    width: 100%;
    height: 60px;
    border-bottom: 2px;
    border-bottom-color: rgba(228, 139, 31, 0.8);
  }
</style>
