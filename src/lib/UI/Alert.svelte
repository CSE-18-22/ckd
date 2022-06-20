<script lang="ts">
  import Button from "./Button.svelte";
  import Modal from "./Modal.svelte";

  export let title = "Confirm?";
  export let msg = "";
  export let ok = "OK";

  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
</script>

<div class="white">
  <Modal
    {title}
    open={msg != ""}
    height={"250px"}
    width={"500px"}
    on:close={() => {
      msg = "";
      dispatch("cancel");
    }}
  >
    <div class="alert">
      <div>
        {msg}
      </div>

      <div class="buttons">
        {#if ok != ""}
          <div class="opacity" style="float:right;">
            <Button
              label={ok}
              on:click={() => {
                msg = "";
                dispatch("ok");
              }}
            />
          </div>
        {/if}
      </div>
    </div>
  </Modal>
</div>

<style>
  .buttons {
    position: absolute;
    bottom: 0px;
    left: 10px;
    right: 10px;
    text-align: right;
  }

  .opacity {
    opacity: 0;
  }
  .alert:hover .opacity {
    opacity: 1;
  }
  .white {
    background-color: rgb(250, 249, 249);
  }
</style>
