# AMMI2021_Bootcamp_project  ----- GROUP 3
This repo consists of the final project for the AMMI 2021 students

* Soona
* Lawrence
* Stephen

## Basic Note (Model Approach)

Based on the visualizations on checking features relationship we were able to discovered some features with high correlation with the target.

This features contains some marginal point which separate the two classes. Hence we use this point has threshold (generated from train data) to predict the correct label.
The following are the features and their respective threshholds that would give the highest possible score:
1. f1--0.35
2. f3--0.34
3. f4--0.23
4. f7--0.3
5. f8--0.3

with this info,we build 5 different models and did a majority vote based on their predictions.

**performance**:we had a score of 0.86 on train dataset and score of 0.93 on test




