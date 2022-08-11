# Coding Challenge

## Part 1. Model Construction and Visualization

In this first part you are assigned to build a model (do not worry about complexity, it can be a linear multiple regression model or a logistic regression model, depending on whether you it is a classification or regression. To test your model, you can use one of the multiple scikit-learn toy datasets (https://scikit-learn.org/stable/datasets/toy_dataset.html). For either model, you must focus on: importing data, splitting data into training, validation and test data (70/15/15), constructing your model and, predicting on the test data. Do not focus on creating the best performing classifier or regressor for this challenge.

For a regression model do the following:
1.	Calculate 1 performance metric, for example RMSE, MSE or R^2 (see https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)  
2.	Visualize the model predictions using a scatter plot (perhaps you can find some inspiration here: https://becominghuman.ai/implementing-and-visualizing-linear-regression-in-python-with-scikit-learn-a073768dc688).  

For a classification model:
1.	Report 1 performance metric (accuracy, F1 score or AUC-ROC)
2.	Visualize the results as a confusion matrix, converting it into a nice heatmap (https://www.w3schools.com/python/python_ml_confusion_matrix.asp).  	

## Part 2. Web Application to Run Model with User-Provided Input
Now that you have proven that your model works (a prediction is made, a metric is calculated), and it’s capable of visualizing the outputs, either as a scatterplot or a heatmap-confusion matrix, it is necessary to develop the web application that will be connected to your model. It is expected that your web application will do the following:
1.	Takes user data as input (the x or features and the y or labels)
2.	Asks the user of the task is regression or classification (important to determine the model)
3.	Output the heatmap or scatterplot based on the type of task selected.
