## Problem:
The more flexible a machine learning method is the easier it is to be overfitted to the training data.
This situation is when the model has low bias(because it fits the Training Data well), but high variance because it does a bad performance with test data(New data)

# Solution
Use the techniques called regularization.
It reduces the sensitive of the model on the training data.
In other words, the bias will be increased a little with greater decrease in variance.

## L2 Regularization (Ridge/Squared regularization)
L2 regularization works by minizing this value:
SSR + lambda*(slope of the regression model)^2

## L1 Regularization (Lasso/Absolute Value regularization)
L1 regularization minizies this value:
SSR+lambda*|slope|

## Difference between L1 and L2 regularization
Lasso regularization can exclude useless variables from the model \
and, in general, tends to perform well when we need to remove a lot of \
useless variable from the model \
\
\
In contrast, Ridge regularization tends to perform better when most of the variables are useful. 