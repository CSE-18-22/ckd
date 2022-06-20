<script lang="ts">
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  export let value = "test";
  export let placeholder = "";
  export let label = "test";

  let focused = (node) => {
    node && typeof node.select === "function" && node.select();
  };
</script>

<div class="input">
  <div class="label">{label}</div>
  <input
    type="number"
    bind:value
    {placeholder}
    class="textbox"
    on:change={(e) => {
      dispatch("changed", value);
    }}
    on:focus={(e) => {
      focused(e.target);
    }}
  />
</div>

<style>
  .textbox {
    width: 100%;
    margin: 10px 0;
    padding: 10px;
    box-shadow: 0 0 15px 4px rgba(0, 0, 0, 0.06);
    border-radius: 5px;
    font-family: inherit;
    font-size: inherit;
  }
  .input {
    display: grid;
    grid-template-columns: 1fr 3fr;
  }
  .label {
    font-size: 40;
    font-weight: 600;
    transform: translateY(30%);
  }
</style>
