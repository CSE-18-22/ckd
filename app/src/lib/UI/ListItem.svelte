<script>
  import Card from "./Card.svelte";

  export let skill = {
    name: "skill",
    img: "imgurl",
    role: "role",
    url: "url",
    description: "description",
  };
  let cardopen = false;
</script>

<div style="padding:2px;">
  <Card>
    <div
      class="container"
      on:click={() => {
        cardopen = !cardopen;
      }}
    >
      <div class="txt">
        <h1><a href={skill.url}>{skill.name}</a></h1>
        {#if cardopen}
          <h3 style="padding-left:15px;">{skill.role}</h3>
          <p style="pading-left:20px;">{skill.description}</p>
        {/if}
      </div>
      <img src={skill.img} alt="#" />
    </div>
  </Card>
</div>

<style>
  .container {
    display: flex;
    width: 40vw;
    padding: 5px;
  }
  .txt {
    width: 350px;
  }
  img {
    width: 300px;
    height: 300px;
  }
</style>
