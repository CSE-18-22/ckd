<script>
  import Input from "../UI/Input.svelte";
  import Alert from "../UI/Alert.svelte";
  import Paper from "../UI/Paper.svelte";
  import Button from "../UI/Button.svelte";
  let pop = false;
  let sg = 1;
  let htn = 1;
  let hemo = 1;
  let dm = 1;
  let al = 1;
  let appet = 1;
  let rc = 1;
  let pc = 1;
  let result = null;
  const submit = async () => {
    pop = true;
    let response = await fetch("https://ckd-flask-app.herokuapp.com/predict", {
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
    result = await response;
  };
</script>

<Paper>
  <div class="note">All Values are set to 1 by default!</div>
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
  <div class="btn"><Button label="Submit" on:click={submit} /></div>

  {#if result != null}
    {#if result.result == "1"}
      <Alert
        title="Prediction"
        msg={`Good news!\n You don't have CKD. Have fun!!!`}
        on:ok={() => {
          result = null;
        }}
      />
    {:else}
      <Alert
        title="Prediction"
        msg={`Sorry to say this,\n You might have to see a doctor.\n There's a chance for you to get CDK.\n Take care!!!`}
        on:ok={() => {
          result = null;
        }}
      />
    {/if}
  {/if}
  {#if pop}
    <Alert
      title="Error"
      msg={`Sorry!\n Our API is encountering some error. Try later!!!`}
      on:ok={() => {
        result = null;
      }}
    />
  {/if}
</Paper>

<style>
  .btn {
    margin-top: 20px;
    position: relative;
    left: 40vw;
  }
  .note {
    font-size: 20px;
    font-weight: bold;
    opacity: 0.3;
  }
</style>
