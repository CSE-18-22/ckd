<script>
  import Profile from "./Profile.svelte";
  let profiles = [
    {
      name: "Vinod Reddy",
      img: "vinod.jpg",
      title: "Team Leader",
      description: "Nothing to say",
    },
    {
      name: "Shakib Shaik",
      img: "vinod.jpg",
      title: "UI Developer",
      description: "Nothing to say",
    },
  ];
</script>

{#each profiles as profile}
  <Profile {profile} />
{/each}
