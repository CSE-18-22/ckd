<script lang="ts">
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  export let fab = false;
  export let label = "";
  export let icon = "";
  export let disabled = false;
</script>

<button
  {disabled}
  class={fab ? "fab" : "btn"}
  on:click={(e) => {
    dispatch("click", e);
  }}
>
  {#if icon != ""}
    <i class="fa {icon}" aria-hidden="true" />
  {/if}
  {#if label != ""}
    {label}
  {/if}
</button>

<style>
  .btn {
    border: 2px solid gray;
    color: gray;
    background-color: white;
    padding: 8px 20px;
    border-radius: 8px;
    font-size: 20px;
    font-weight: bold;
  }

  .btn:hover {
    background: #47a7f5 radial-gradient(circle, transparent 1%, #47a7f5 1%)
      center/15000%;
    color: #fff;
  }

  .btn:active {
    background-color: #6eb9f7;
    background-size: 100%;
    transition: background 0s;
  }

  .fab {
    background-position: center;
    transition: background 0.8s;
    width: 100%;
    height: 45px;
    border-radius: 4px;
  }

  .fab:hover {
    background: #314352 radial-gradient(circle, transparent 1%, #262b31 1%)
      center/15000%;
    color: #fff;
  }

  .fab:active {
    background-color: #6eb9f7;
    background-size: 100%;
    transition: background 0s;
  }

  button {
    border: none;
    padding: 10px;
    font-size: 16px;
    text-transform: uppercase;
    cursor: pointer;
    color: white;
    background-color: #319af0;
    box-shadow: 0 0 15px 4px rgba(0, 0, 0, 0.06);
    outline: none;
    display: inline-block;
  }
  @media (max-width: 820px) {
    .fab {
      margin-top: 1rem;
    }
  }
</style>
