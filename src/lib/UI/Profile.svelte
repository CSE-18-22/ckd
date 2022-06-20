<script>
  import Card from "./Card.svelte";
  import Paper from "./Paper.svelte";

  export let profile = {
    name: "name",
    id: "github id",
    link: "github link",
    img: "imgurl",
    title: "title",
    description: "description",
  };
</script>

<div class="profile">
  <Card>
    <div class="card">
      <div class="contianer">
        <img src={profile.img} alt="" class="img" />
      </div>
      <div class="details">
        <div style="display:flex;">
          <div class="name">
            {profile.name}
            <small style="opacity:0.5;"
              ><a href={profile.link}>{profile.id}</a>
            </small>
          </div>
        </div>
        <div class="title">{profile.title}</div>
        <div class="description">{profile.description}</div>
      </div>
    </div>
  </Card>
</div>

<style>
  .profile {
    width: 45vw;
    background-color: aliceblue;
  }
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
