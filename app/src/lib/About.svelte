<script>
  import Profile from "./Profile.svelte";
  let profiles = [
    {
      name: "Vinod Reddy",
      img: "profile/vinod.jpg",
      title: "Team Leader",
      description: "Nothing to say",
    },
    {
      name: "Shakib Shaik",
      img: "profile/shakib.jpeg",
      title: "UI Developer",
      description: "Nothing to say",
    },
    {
      name: "Attar Fazulul Rehman",
      img: "profile/fazulul.jpeg",
      title: "UI Developer",
      description: "Nothing to say",
    },
    {
      name: "Saleem",
      img: "profile/saleem.jpeg",
      title: "UI Developer",
      description: "Nothing to say",
    },
  ];
</script>

{#each profiles as profile}
  <Profile {profile} />
{/each}
