## Random forest vs AdaBoost

In Random Forest each time you make a tree, you make a full size tree.
In contrast in AdaBoost the trees are usually just a node and two leaves.
The trees in AdaBoost is called Stumps.

### How AdaBoost Works

1. Give a sample weight that indicates how important(influential) it is to be classified. At first all the samples get the same weight ---> 1/Total number of samples \
This makes all the samples equally important

2. Then we need to make the first Stump in the forest.
This is done by comparing the features seperately and check which does the better classification

3. The Feature with the lowest Gini index will be chosen as the frist stump of the progress. \
Gini Index = 1- sum_of_i_1_to_n((p_i)^2)    \
p_i = probability of an element being classified for distinct class

4. Use the total error to determine the "Amount of Say" the Stump has in the final classification with the following formula: \
Amount of Say = (1/2)*log((1-total_probability_of_error)/total_probability_of_error)

5. Update the sample weights using the "Amount of Say"\
Sample weights of samples Incorrectly predicted using the feature =
Sample weight * e^(Amount of Say)  \
Sample weights of samples correctly predicted = Sample weight * e^(-Aoumt of Say)

6. Then normalize the weights so their total is 1
7. Use the modified sample weights to make the next Stump in the forest.