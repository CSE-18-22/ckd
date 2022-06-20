<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  import Input from "../UI/Input.svelte";
  import Modal from "../UI/Modal.svelte";
  import Alert from "../UI/Alert.svelte";
  let sg = 1;
  let htn = 1;
  let hemo = 1;
  let dm = 1;
  let al = 1;
  let appet = 1;
  let rc = 1;
  let pc = 1;
  // alert("Functionality not implemented yet!");
  let result = null;
  const submit = async () => {
    let response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        sg: sg,
        htn: htn,
        hemo: hemo,
        dm: dm,
        al: al,
        appet: appet,
        rc: rc,
        pc: pc,
      }),
    });
    result = await response.json();
    console.log(result);
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
{#if result}
  <Alert title="Prediction" msg="Good news! You don't have CKD" />
{/if}

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
