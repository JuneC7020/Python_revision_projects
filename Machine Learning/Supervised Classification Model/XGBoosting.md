## XGBoosting

AdaBoost(Adaptive Boosting) -> Gradient Boosting -> XGBoost(Extreme Gradient Boosting)

1. First step in fitting XGBoost to training data is to make an initial prediction(ex. average of observed value)
2. Create a XGBoost Tree \
Each tree starts with a single leaf and all the residuals go to the leaf \
Calculate the Quality score and Similarity Score of the Residuals \
Similarity Score = {(Sum of Residuals)^2}/(Number of Residuals + lambda) \
lambda = Regularization parameter \
3. Split the residuals into two groups (From all of the residuals of the leaf, split them )\
Calculate the similarity score for the each group \
Calculate the Gain of the splitting the Residuals into groups\
Gain = Left_similiarity + Right_similiarity - Root_similiarity \
Calculate the Gain for set of groups \


