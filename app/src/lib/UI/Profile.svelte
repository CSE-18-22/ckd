<script>
  import Card from "./Card.svelte";
  export let profile = {
    name: "name",
    img: "imgurl",
    title: "title",
    description: "description",
  };
</script>

<div>
  <Card>
    <div class="card">
      <div class="contianer"><img src={profile.img} alt="" class="img" /></div>
      <div class="details">
        <div class="name">{profile.name}</div>
        <div class="title">{profile.title}</div>
        <div class="description">{profile.description}</div>
      </div>
    </div>
  </Card>
</div>

<style>
  .card {
    display: flex;
  }
  .img {
    width: 200px;
    height: 300px;
  }
  .name {
    font-size: 30px;
    font-weight: bold;
    padding: 20px;
  }
  .title {
    font-size: 20px;
    color: rgb(21, 21, 20);
    padding-left: 20px;
  }
  .description {
    padding: 20px;
    width: 100%;
    height: auto;
  }
</style>
