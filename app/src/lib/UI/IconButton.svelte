<script lang="ts">
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let size = 20;
  export let icon;

  let color = "black";
</script>

<div
  style="cursor: pointer; width:{size}px; height:{size}px; color: var(--onbackground); display: flex; justify-content: center; align-items: center;"
  on:mouseover={() => {
    color = "gray";
  }}
  on:focus={() => {
    color = "gray";
  }}
  on:mouseout={() => {
    color = "black";
  }}
  on:blur={() => {
    color = "black";
  }}
  on:click={() => {
    dispatch("click");
  }}
>
  <i class="fa {icon}" aria-hidden="true" />
</div>

<style>
</style>
