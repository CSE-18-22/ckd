<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import IconButton from "./IconButton.svelte";
  const dispatch = createEventDispatcher();

  export let title = "My Dialog";
  export let width = "95%";
  export let height = "95%";
  export let open = false;
  export let closable = true;
  $: (() => {
    if (open && animation != "animation-close") {
      setTimeout(() => {
        animation = "animation-open";
      }, 50);
    }
  })();
  $: animation = null;

  const close = () => {
    animation = "animation-close";
    setTimeout(() => {
      open = false;
      dispatch("close");
      animation = null;
    }, 300);
  };
</script>

{#if open}
  <div class="container">
    <div
      class="back-drop"
      class:animation-back-drop-open={animation == "animation-open"}
      class:animation-back-drop-close={animation == "animation-close"}
      on:click={() => {
        close();
      }}
    />

    <div
      class="modal"
      style="width: {width}; height: {height}"
      class:animation-open={animation == "animation-open"}
      class:animation-close={animation == "animation-close"}
    >
      <div style="margin:20px">
        {#if closable}
          <div
            class="close"
            style="position:absolute; right: 40px; top:20px"
            title="Close"
          >
            <IconButton
              icon="fa-times"
              on:click={() => {
                close();
              }}
            />
          </div>
        {/if}
        <h2>{title}</h2>
        <div class="content">
          <slot />
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  .container {
    position: fixed;
    left: 0px;
    right: 0px;
    bottom: 0px;
    top: 0px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
  }

  .content {
    position: fixed;
    left: 20px;
    right: 20px;
    bottom: 20px;
    top: 70px;
    padding: 20px;
    overflow-y: auto;
  }

  .back-drop {
    position: fixed;
    left: 0px;
    right: 0px;
    bottom: 0px;
    top: 0px;
    background-color: rgb(224, 224, 224, 0.2);
    backdrop-filter: blur(2px) opacity(20%);
  }

  .modal {
    background-color: var(--background);
    z-index: 2;
    transform: scale(0.7);
    color: var(--onbackground);
    box-shadow: 0 0 5px #000000;
    border-radius: 0.4em;
  }

  .animation-back-drop-open {
    backdrop-filter: blur(1px) opacity(100%);
    transition: all 0.3s;
  }

  .animation-back-drop-close {
    backdrop-filter: blur(0px) opacity(0%);
    transition: all 0.3s;
  }

  .animation-open {
    transform: scale(1);
    opacity: 1;
    transition: all 0.3s;
  }

  .animation-close {
    transform: scale(0.7);
    opacity: 0.2;
    transition: all 0.3s;
  }
  .close {
    opacity: 0;
  }
  .modal:hover .close {
    opacity: 1;
  }
</style>
