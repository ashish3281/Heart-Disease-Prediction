# Heart-Disease-Prediction
<p>A heart attack which is analogous to acute myocardial infarction (AMI) is one of the most serious diseases in the segment of cardiovascular disease. It occurs due to the interruption of blood circulation to muscle of the heart which damages the heart the muscle. Diagnosing heart disease is also a crucial task. The symptoms, physical examination, and understanding of the different signs of this disease are required to diagnose heart disease. Different factors including cholesterol, genetic heart disease, high blood pressure, low physical activity, obesity, and smoking can be reasons for the occurrence of heart disease. The major reason for heart attacks is the stoppage of blood to the coronary arteries. The red blood cells (RBC) start getting low when blood flow is reduced; due to this the human body stops getting necessary oxygen and loses consciousness. The early diagnosis through symptoms and signs can help prevent patients of heart attacks if the prediction is accurate enough. Figure 1 shows different symptoms of a heart attack. The work presented takes 13 features/attributes as input having number values. It has been stated that little modifications in lifestyle including quitting smoking/alcohol/tobacco, having healthy food habits, and routine exercises can help in the prevention of heart attacks. Any person living a healthy lifestyle with early treatment after diagnosis can greatly increase the positive results. However, it is difficult to identify the high risk of heart disease where different risks like diabetes, high blood pressure, and cholesterol problems are present. In these types of scenarios, ML can help in the early diagnosis of disease</p>
<h2>Import libraries</h2>
<p>I imported several libraries for the project:</p>
<ul>
  <li>numpy: To work with arrays</li>
<li>pandas: To work with csv files and dataframes</li>
<li>matplotlib: To create charts using pyplot, define parameters using rcParams and color them with cm.rainbow</li>
<li>warnings: To ignore all warnings which might be showing up in the notebook due to past/future depreciation of a feature</li>
<li>train_test_split: To split the dataset into training and testing data</li>
<li>StandardScaler: To scale all the features, so that the Machine Learning model better adapts to the dataset</li>

  
  <h2>Import dataset</h2>
<li>After downloading the dataset from Kaggle, I saved it to my working directory with the name dataset.csv. Next, I used read_csv() to read the dataset and save it to the dataset variable.</li>
