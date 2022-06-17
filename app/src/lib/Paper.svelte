<script lang="ts">
</script>

<div class="paper">
  <slot />
</div>

<style>
  .paper {
    width: 100%;
    height: 100%;
    padding: 10px;
    box-shadow: 0 2px 2px 0 rgb(0 0 0 / 14%), 0 3px 1px -2px rgb(0 0 0 / 12%),
      0 1px 5px 0 rgb(0 0 0 / 20%);
    box-shadow: 0 0 5px #000;
    box-sizing: border-box;
    border-radius: 5px;
    position: relative;
    background-color: var(--surface);
    color: var(--onsurface);
    margin-bottom: 10px;
  }
</style>
