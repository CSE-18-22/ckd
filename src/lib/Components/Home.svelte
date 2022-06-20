<script>
  import Card from "../UI/Card.svelte";
  import Paper from "../UI/Paper.svelte";
</script>

<div class="parent">
  <div class="home">
    <div class="img">
      <img style="height:500px;" src="image/ckd.jpeg" alt="#" />
      <div>
        <h1 style="padding:10px;">What is CKD?</h1>
        <p style="padding:20px;">
          Chronic kidney disease, also called chronic kidney failure, involves a
          gradual loss of kidney function. Your kidneys filter wastes and excess
          fluids from your blood, which are then removed in your urine. Advanced
          chronic kidney disease can cause dangerous levels of fluid,
          electrolytes and wastes to build up in your body. <br /> <br />
          In the early stages of chronic kidney disease, you might have few signs
          or symptoms. You might not realize that you have kidney disease until the
          condition is advanced. <br /> <br />
          Treatment for chronic kidney disease focuses on slowing the progression
          of kidney damage, usually by controlling the cause. But, even controlling
          the cause might not keep kidney damage from progressing. Chronic kidney
          disease can progress to end-stage kidney failure, which is fatal without
          artificial filtering (dialysis) or a kidney transplant.
        </p>
      </div>
    </div>
    <div style="padding-top:10px;">
      <Paper>
        <h1>Chronic Kidney disease</h1>
        <div style="display:flex;">
          <div style="flex-grow:3;padding:5px;">
            <Card>
              <h1>Symptoms</h1>
              <ul>
                <li>Nausea</li>
                <li>Vomiting</li>
                <li>Loss of appetite</li>
                <li>Fatigue and Weakness</li>
                <li>Sleep problems</li>
                <li>Urinating more or less</li>
                <li>Decreased mental sharpness</li>
                <li>Muscle cramps</li>
                <li>Swelling of feet and ankles</li>
                <li>Dry, itchy skin</li>
                <li>
                  High blood pressure (hypertension) that's difficult to control
                </li>
                <li>Shortness of breath, if fluid builds up in the lungs</li>
                <li>
                  Chest pain, if fluid builds up around the lining of the heart
                </li>
              </ul></Card
            >
          </div>
          <div style="flex-grow:2;padding:5px;">
            <Card
              ><h1>Risk factors</h1>
              <ul>
                <li>Diabetes</li>
                <li>High blood pressure</li>
                <li>Heart (cardiovascular) disease</li>
                <li>Smoking</li>
                <li>Obesity</li>
                <li>Being Black, Native American or Asian American</li>
                <li>Family history of kidney disease</li>
                <li>Abnormal kidney structure</li>
                <li>Older age</li>
                <li>Frequent use of medications that can damage the kidneys</li>
              </ul></Card
            >
          </div>
        </div>
        <div style="padding:10px;">
          <div>
            <Card>
              <h1>Complications</h1>
              <p>
                Chronic kidney disease can affect almost every part of your
                body. Potential complications include:
              </p>
              <ul>
                <li>
                  Fluid retention, which could lead to swelling in your arms and
                  legs, high blood pressure, or fluid in your lungs (pulmonary
                  edema)
                </li>
                <li>
                  A sudden rise in potassium levels in your blood
                  (hyperkalemia), which could impair your heart's function and
                  can be life-threatening
                </li>
                <li>Anemia</li>
                <li>Heart disease</li>
                <li>Weak bones and an increased risk of bone fractures</li>
                <li>
                  Decreased sex drive, erectile dysfunction or reduced fertility
                </li>
                <li>
                  Damage to your central nervous system, which can cause
                  difficulty concentrating, personality changes or seizures
                </li>
                <li>
                  Decreased immune response, which makes you more vulnerable to
                  infection
                </li>
                <li>
                  Pericarditis, an inflammation of the saclike membrane that
                  envelops your heart (pericardium)
                </li>
                <li>
                  Pregnancy complications that carry risks for the mother and
                  the developing fetus
                </li>
                <li>
                  Irreversible damage to your kidneys (end-stage kidney
                  disease), eventually requiring either dialysis or a kidney
                  transplant for survival
                </li>
              </ul>
            </Card>
          </div>
          <div>
            <Card>
              <h1>Prevention</h1>
              <p>To reduce your risk of developing kidney disease:</p>
              <ul>
                <li>
                  <b>Follow instructions on over-the-counter medications.</b>
                  When using nonprescription pain relievers, such as aspirin,
                  ibuprofen (Advil, Motrin IB, others) and acetaminophen
                  (Tylenol, others), follow the instructions on the package.
                  Taking too many pain relievers for a long time could lead to
                  kidney damage. <br /><br />
                </li>
                <li>
                  <b>Maintain a healthy weight.</b>
                  If you're at a healthy weight, maintain it by being physically
                  active most days of the week. If you need to lose weight, talk
                  with your doctor about strategies for healthy weight loss.
                  <br /><br />
                </li>
                <li>
                  <b
                    >Don't smoke. Cigarette smoking can damage your kidneys and
                    make existing kidney damage worse.</b
                  >
                  If you're a smoker, talk to your doctor about strategies for quitting.
                  Support groups, counseling and medications can all help you to
                  stop.
                  <br /><br />
                </li>
                <li>
                  <b>Manage your medical conditions with your doctor's help.</b>
                  If you have diseases or conditions that increase your risk of kidney
                  disease, work with your doctor to control them. Ask your doctor
                  about tests to look for signs of kidney damage. <br /><br />
                </li>
              </ul></Card
            >
          </div>
        </div>
      </Paper>
    </div>
  </div>
</div>

<style>
  .parent {
    width: 1800px;
    overflow-y: auto;
    overflow-x: hidden;
  }
  .img {
    width: 100%;
    height: 500px;
    background-color: aqua;
    overflow: inherit;
    display: flex;
  }
  .home {
    overflow-y: auto;
    overflow-x: hidden;
    width: 90vw;
  }
  div {
    padding: 5px;
  }
  img {
    padding-left: 5px;
  }
</style>
