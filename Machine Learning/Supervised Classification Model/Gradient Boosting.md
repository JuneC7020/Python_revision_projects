## Gradient Boosting

1. First calculate the average of the observed value -> this would be the first prediction.
2. Calculate the Pseudo Residuals for all samples (residual = observed value - predicted value)
3. Build a Tree using features. The leaves of the tree is the predicted residuals
4. average weight(predicted value) + 0.1 * tree's prediction(pseudo residual) = new prediction. Calculate new pseudo residual based on the new prediction
