<script>
  import Card from "./Card.svelte";
</script>

<div class="parent">
  <div class="home">
    <div class="img">
      <img style="height:500px;" src="images/ckd.jpeg" alt="#" />
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
    <h1>Chronic Kidney disease</h1>
    <div>
      We'll be using Machine Learning to predict the Chronic Kidney Disease
      condition.
    </div>
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
            Chronic kidney disease can affect almost every part of your body.
            Potential complications include:
          </p>
          <ul>
            <li>
              Fluid retention, which could lead to swelling in your arms and
              legs, high blood pressure, or fluid in your lungs (pulmonary
              edema)
            </li>
            <li>
              A sudden rise in potassium levels in your blood (hyperkalemia),
              which could impair your heart's function and can be
              life-threatening
            </li>
            <li>Anemia</li>
            <li>Heart disease</li>
            <li>Weak bones and an increased risk of bone fractures</li>
            <li>
              Decreased sex drive, erectile dysfunction or reduced fertility
            </li>
            <li>
              Damage to your central nervous system, which can cause difficulty
              concentrating, personality changes or seizures
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
              Pregnancy complications that carry risks for the mother and the
              developing fetus
            </li>
            <li>
              Irreversible damage to your kidneys (end-stage kidney disease),
              eventually requiring either dialysis or a kidney transplant for
              survival
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
              <b>Follow instructions on over-the-counter medications.</b> When using
              nonprescription pain relievers, such as aspirin, ibuprofen (Advil,
              Motrin IB, others) and acetaminophen (Tylenol, others), follow the
              instructions on the package. Taking too many pain relievers for a long
              time could lead to kidney damage.
            </li>
            <li>
              <b>Maintain a healthy weight.</b>
              If you're at a healthy weight, maintain it by being physically active
              most days of the week. If you need to lose weight, talk with your doctor
              about strategies for healthy weight loss.
            </li>
            <li>
              <b
                >Don't smoke. Cigarette smoking can damage your kidneys and make
                existing kidney damage worse.</b
              >
              If you're a smoker, talk to your doctor about strategies for quitting.
              Support groups, counseling and medications can all help you to stop.
            </li>
            <li>
              <b>Manage your medical conditions with your doctor's help.</b>
              If you have diseases or conditions that increase your risk of kidney
              disease, work with your doctor to control them. Ask your doctor about
              tests to look for signs of kidney damage.
            </li>
          </ul></Card
        >
      </div>
    </div>
    <div>
      <Card>
        <h1>Chronic Kidney Disease Prediction</h1>
        <p>
          Chronic Kidney Disease (CKD) or chronic renal disease has become a
          major issue with a steady growth rate. A person can only survive
          without kidneys for an average time of 18 days, which makes a huge
          demand for a kidney transplant and Dialysis. It is important to have
          effective methods for early prediction of CKD. Machine learning
          methods are effective in CKD prediction. This work proposes a workflow
          to predict CKD status based on clinical data, incorporating data
          prepossessing, a missing value handling method with collaborative
          filtering and attributes selection. Out of the 11 machine learning
          methods considered, the extra tree classifier and random forest
          classifier are shown to result in the highest accuracy and minimal
          bias to the attributes. The research also considers the practical
          aspects of data collection and highlights the importance of
          incorporating domain knowledge when using machine learning for CKD
          status prediction.
        </p>
      </Card><Card>
        <h2>Prediction of chronic kidney disease using Machine Learning</h2>
        <div>
          Machine learning methods are effective in CKD prediction. This work
          proposes a workflow to predict CKD status based on clinical data,
          incorporating data prepossessing, a missing value handling method with
          collaborative filtering and attributes selection.
        </div>
      </Card>
    </div>
    <div>
      <Card>
        <h1>Proposed System</h1>
        <p>
          This part describes the dataset and contains block diagrams, flow
          diagrams, evaluation matrices, and the study’s procedure and
          methodology. Figure 1 depicts the block diagram of the proposed
          system. The framework utilizes the CKD prediction dataset. After
          preprocessing and feature selection, the DT, KNN, and logistic
          regression algorithms have been used. All the components of this
          diagram have been discussed in the following sub sections.
        </p>
        <img src="images/proposed_system.png" alt="#" />
      </Card>
    </div>
    <div>
      <Card>
        <h2>Dataset</h2>
        <p>
          The research was conducted using the CKD dataset [26]. There are 400
          rows and 14 columns in this dataset. The output column “class” has a
          value of either “1” or “0.” The value “0” indicates that the patient
          is not a CKD patient, while the value “1” shows that the patient is a
          CKD patient. Before preprocessing, Figure 2 displays the total number
          of CKD and non-CKD entries in the output column. The overall number of
          CKD data is 250, whereas the total number of non-CKD data is 150.
        </p>
      </Card>
    </div>
    <div>
      <Card
        ><h2>Data preprocessing</h2>
        <p>
          The research was conducted using the CKD dataset [26]. There are 400
          rows and 14 columns in this dataset. The output column “class” has a
          value of either “1” or “0.” The value “0” indicates that the patient
          is not a CKD patient, while the value “1” shows that the patient is a
          CKD patient. Before preprocessing, Figure 2 displays the total number
          of CKD and non-CKD entries in the output column. The overall number of
          CKD data is 250, whereas the total number of non-CKD data is 150.
        </p>
        <img src="images/preprocess.png" alt="#" /></Card
      >
    </div>
    <div>
      <Card
        ><h2>Feature Selection</h2>
        <p>
          In the heat map, the absolute values of the correlations between
          features and the class label show that blood pressure, albumin, sugar,
          blood urea, serum creatinine, potassium, white blood cell count, and
          hypertension all have positive links. Figures 4 and 5 show the feature
          correlation value and heat map, respectively.
        </p>
        <img src="images/feature1.png" alt="#" />
        <img src="images/feature2.png" alt="#" />
        <p>
          All the positively correlated features are considered for further
          prediction. Each albumin molecule has just five distinct sets of
          values. The quantity of albumin is assessed using a urine protein
          test. A high protein level in the urine means that the filtration
          units in the kidneys have been damaged by disease, fever, or intense
          activity. Numerous tests should be performed over many weeks to
          establish the diagnosis. The term serum creatinine is used
          interchangeably with blood creatinine and creatinine. Creatinine is
          the byproduct of muscle breakdown of the chemical creatine. The
          kidneys eliminate creatinine from the body. This test is done to find
          out how much creatinine is in your blood. Creatine is an element of
          the metabolic cycle that produces the energy needed for muscle
          contraction. The body produces both creatine and creatinine at the
          same rate. Creatinine levels in the blood can rise due to a
          high-protein diet, congestive heart failure, diabetic issues, and
          dehydration, among other factors. Creatinine levels in women should be
          between 0.6 and 1.1 mg/dL, while those in males should be between 0.7
          and 1.3 mg/dL. Additionally, hypertension, or high blood pressure,
          develops whenever blood pressure against the walls of blood vessels
          rises. Hypertension can lead to heart attacks, strokes, and chronic
          kidney disease if it is not treated or managed properly. Nonetheless,
          CKD may result in hypertension
        </p></Card
      >
    </div>
    <div>
      <Card
        ><h1>Algorithms</h1>
        <ul>
          <li>Decision tree classifier</li>
          <li>K-nearest neighbor</li>
          <li>Logistic regression</li>
        </ul></Card
      >
    </div>
    <div>
      <Card
        ><h2>Decision Tree</h2>
        <p>
          The DT method is a classification and regression technique that can be
          used to predict both discrete and continuous characteristics. Based on
          the links between input columns in a dataset, the algorithm predicts
          discrete characteristics. It predicts the states of a column that you
          identify as predictable using the values of those columns, known as
          states. The method specifically finds the input columns that are
          associated with the predicted column.
        </p>
        <img src="images/decision_tree.png" alt="#" />
        <p>
          The decision tree is easy to comprehend since it replicates the phases
          that a person goes through while making a real-life decision. It may
          be quite useful in dealing with decision-making issues. It is a good
          idea to consider all potential solutions to an issue. Cleaning data is
          not as important as it is with other methods.
        </p></Card
      >
    </div>
    <div>
      <Card>
        <h2>K-Nearest Neighbor</h2>
        <p>
          Figure 7 depicts the whole KNN model’s flowchart. One of the simplest
          ML algorithms is KNN, which uses the supervised learning approach. A
          new case is assigned to a category based on how closely it resembles
          prior categories. This is known as the KNN technique. With the KNN
          method, you can store all the data you have and then classify new data
          based on how similar it is to the old. This suggests that the KNN
          technique can rapidly classify new data into well-defined categories.
          Though it is often utilized for classification problems, the KNN
          method may be used for regression as well. There are no data
          assumptions made by the KNN technique, which is nonparametric and also
          called a “lazy learner algorithm,” since it does not instantly learn
          from the training set but rather keeps and categorizes the data for
          later. If it receives new data, the KNN classifies it into a category
          that is quite close to the new data that was stored during training.
        </p>
        <img src="images/knn.png" alt="#" />
        <p>
          For classification, one of the most frequently used ML methods is the
          -nearest neighbor classifier. The nonparametric slow learning
          approach, -nearest neighbor, may be used to categorize data. This
          classifier sorts objects according to how far they are from each other
          and how close they are. It prioritizes the immediate surroundings of
          the item above, the dissemination of essential information.
        </p></Card
      >
    </div>
    <div>
      <Card
        ><h2>Logistic Regression</h2>
        <p>
          Binary outcomes are modeled using the statistical method of logistic
          regression, which is well known in the field. Different learning
          methods are used to execute logistic regression in statistical
          research. A variant of the neural network method was used to create
          the LR algorithm. This method resembles neural networks in many ways,
          but it is simpler to set up and use. Figure 8 shows the block diagram
          of LR.
        </p>
        <img src="images/lr.png" alt="#" />
        <p>
          Utilizing logistic regression, the output of a categorical dependent
          variable is predicted. So, the output must be discrete or categorical.
          It may be yes or no, 0 or 1, true or false, etc., but probability
          values between 0 and 1 are given. Logistic regression and linear
          regression are used in very similar ways. Classification problems are
          addressed with logistic regression, and regression problems are
          addressed using linear regression. Instead of a regression line, we
          use an “S” shaped logistic function that predicts two maximum values
          (0 or 1). The logistic function’s curve indicates the probability of
          anything, such as whether cells are malignant or not, or if an animal
          is fat or not. Since it can classify new data using both discrete and
          continuous datasets, logistic regression is a common ML technique.
        </p></Card
      >
    </div>
    <div>
      <Card
        ><h2>Confusion Matrix</h2>
        <p>
          The confusion matrix rates machine learning classification models’
          performance. All models were evaluated using the confusion matrix. The
          confusion matrix illustrates how often our models guess correctly and
          incorrectly. Poorly predicted values received false positives and
          negatives, whereas properly predicted values received genuine
          positives and negatives. The model’s accuracy, precision-recall
          trade-off, and AUC were assessed after grouping all predicted values
          in the matrix.
        </p>
        <img src="images/confusion_matrix.png" alt="#" /></Card
      >
    </div>
    <div>
      <Card
        ><h2>Result and Data Analysis</h2>
        <p>
          In this case, the accuracy is 96.25 percent. This accuracy did not
          improve after fine tuning.
        </p>
        <img src="images/result.png" alt="#" />
        <img src="images/result2.png" alt="#" />
        <p>
          Here, the overall F1-score is 96 percent. Individual F1-scores are 95%
          for non-CKD and 97% for CKD. Also, precision and recall have been
          shown in the above figur
        </p>
        <br />
        <p>
          Figure 12 depicts the DT AUC curve. It demonstrates that the DT
          classifier has an accuracy of 96 percent under the curve.
        </p>
        <img src="images/result3.png" alt="#" />
        <p>
          Figure 13 depicts the decision tree classifier’s prediction. The
          predicted outcome, as well as the model’s calculated performance, is
          shown in the confusion matrix. There were 77 accurate guesses and 3
          erroneous predictions.
        </p>
        <img src="images/result4.png" alt="#" /></Card
      >
    </div>
    <div>
      <Card
        ><h2>K-Nearest Neighbor</h2>
        <p>
          Figure 14 shows the -NN classifier’s classification accuracy. Here,
          the accuracy is lower than with other algorithms. Even after fine
          tuning, this accuracy did not improve further.
        </p>
        <img src="images/knn1.png" alt="#" />
        <img src="images/knn2.png" alt="#" />
        <p>
          The overall performance of KNN is unsatisfactory. The overall F1-score
          obtained here is 71%. Individual F1-scores for non-CKD are 69 percent
          and 73 percent for CKD. Figure 16 depicts the KNN classifier’s AUC
          curve. The KNN classifier has a 73 percent accuracy under the curve.
        </p>
        <img src="images/knn3.png" alt="#" />
        <p>
          Prior to fine-tuning, the -nearest neighbor model predicts, as seen in
          Figure 17. As well as the model’s calculated performance, the
          confusion matrix displays the predicted outcome. There were 57
          accurate predictions, but there were also 23 erroneous predictions.
        </p>
        <img src="images/knn4.png" alt="#" /></Card
      >
    </div>
    <div>
      <Card>
        <h2>Logistic Regression</h2>
        <p>
          The report of the LR model is shown in Figure 18. This model has the
          best accuracy in classifying objects.
        </p>
        <img src="images/lr1.png" alt="#" />
        <p>
          In this case, the total F1-score obtained is 97 percent. Individuals
          without CKD have an F1-score of 96 percent, whereas those with CKD
          have a score of 98 percent. The AUC curve for the logistic regression
          classifier is shown in Figure 19. The accuracy under the curve is 100
          percent in this case.
        </p>
        <img src="images/lr2.png" alt="#" />
        <p>
          Figure 20 shows the final prediction of the logistic regression model.
          As well as the model’s calculated performance, the confusion matrix
          displays the predicted outcome. There were 97 correct forecasts and
          three incorrect forecasts, for a total accuracy of 100 percent.
        </p>
        <img src="images/lr3.png" alt="#" />
      </Card>
    </div>
    <div>
      <Card>
        <h2>Model Comparison</h2>
        <p>
          Table 1 contrasts the new models with those found in prior studies.
          The chart clearly indicates that logistic regression is the best among
          the many models in the framework.
        </p>
        <img src="images/comparision.png" alt="#" />
        <p>
          Using LR, this paper achieved 97 percent accuracy. The DT classifier
          also achieved good accuracy, 96.25 percent. But by using the same
          model, ref. [27] achieved poor accuracy.
        </p></Card
      >
    </div>
    <div>
      <Card
        ><h2>Conclusion</h2>
        <p>
          According to the findings of the study, the decision tree approach and
          logistic regression can be used to predict chronic kidney disease more
          accurately. According to the study, their precision was 96.25 percent,
          and their accuracy was 97 percent. Compared to prior research, the
          accuracy percent of the models used in this investigation is
          considerably higher, indicating that the models used in this study are
          more reliable than those used in previous studies. When
          crossvalidation measurements are used in the prediction of chronic
          kidney disease, the LR method outperforms the other processes. Future
          research may build on this work by developing a web application that
          incorporates these algorithms and using a bigger dataset than the one
          utilized in this study. This will aid in the achievement of improved
          outcomes as well as the accuracy and efficiency with which healthcare
          practitioners can anticipate kidney issues. This will enhance the
          dependability of the framework as well as the framework’s
          presentation. The hope is that it would encourage people to seek early
          treatment for chronic renal disease and to make improvements in their
          lives.
        </p></Card
      >
    </div>
  </div>
</div>

<style>
  .parent {
    width: 90vw;
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
</style>
