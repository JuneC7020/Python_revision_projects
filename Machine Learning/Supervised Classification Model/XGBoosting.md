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
Calculate the Gain for other sets of groups using different thresholds \
Compare the Gain of the groups and choose the one with the largest Gain \
Then from the chosen tree split the leaves using the same method \
4. Set gamma, if the gain of the branch is smaller than the gamma prune the branch (Don't remove the root)

5. The Final tree is made!
predicted value + learning rate * the tree
= new predicted value \
Then build another tree based on the new prediction with its new residual.


