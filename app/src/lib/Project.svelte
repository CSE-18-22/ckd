<script>
  import Input from "./Input.svelte";
  let sg;
  let htn;
  let hemo;
  let dm;
  let al;
  let appet;
  let rc;
  let pc;
  let submit = () => {
    alert("Functionality not implemented yet!");
  };
</script>

<Input
  label="Specific Gravity"
  placeholder="Ex: (1.005,1.010,1.015,1.020,1.025)"
  on:changed={(value) => {
    sg = value.detail;
  }}
/>
<Input
  label="Hyper Tension"
  placeholder="Yes = 1, No=0"
  on:changed={(value) => {
    htn = value.detail;
  }}
/>
<Input
  label="Hemoglobin"
  placeholder="in gms"
  on:changed={(value) => {
    hemo = value.detail;
  }}
/>
<Input
  label="Diabetes Mellitus"
  placeholder="Yes = 1, No=0"
  on:changed={(value) => {
    dm = value.detail;
  }}
/>
<Input
  label="Albumin"
  placeholder="(0,1,2,3,4,5)"
  on:changed={(value) => {
    al = value.detail;
  }}
/>
<Input
  label="Appetite"
  placeholder="Good = 1, Poor = 0"
  on:changed={(value) => {
    appet = value.detail;
  }}
/>
<Input
  label="Red Blood Cell Count"
  placeholder="in Millions/cmm"
  on:changed={(value) => {
    rc = value.detail;
  }}
/>
<Input
  label="Pus Cell"
  placeholder="Normal = 0, Abnormal = 1"
  on:changed={(value) => {
    pc = value.detail;
  }}
/>
<button class="btn" on:click={submit}>submit</button>

<style>
  .btn {
    margin-top: 20px;
    position: relative;
    left: 40vw;
    height: 50px;
    width: 100px;
    background-color: aqua;
    border-radius: 5px;
    border-width: 0px;
  }
</style>
