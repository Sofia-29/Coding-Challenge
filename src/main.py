from model.RegressionModel import RegressionModel
from model.Graphs import Graphs

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

graph = Graphs()

def linear_multiple_regression_controller():

    global graph

    linear_multiple_regression_model = LinearRegression()
    model  = RegressionModel(linear_multiple_regression_model)

    dataset = datasets.load_iris()

    #split data intro traning (70 %), validation(15 %) and test data(15 %)
    model.split_data(dataset.data, dataset.target, 0.70, 0.15, 0.15)

    #fit data to model
    model.fit_data()

    validation_data = model.get_validation_data()
    predicted_data = model.predict_data(validation_data)
    validation_data_target = model.get_validation_data_targets()

    test_data = model.get_test_data()
    predicted_data_test = model.predict_data(test_data)
    test_data_target = model.get_test_data_targets()

    print("Mean squared error using validation data: " + str(model.get_mean_squared_error(predicted_data, validation_data_target)))
    mse_test_data = round(model.get_mean_squared_error(predicted_data_test, test_data_target), 4)

    graph.setup_plot(test_data, test_data_target, predicted_data_test, 
       "Iris Species" + "\n" + "Iris Setosa = 0 Iris Versicolor = 1 Iris Virginica = 2 \n Mean squared error using test data: " + str(mse_test_data),
        "Iris id", "Predicted values")
    
    graph.show_plot()


def logistic_regression_controller():
    
    global graph

    logistic_regression_model = LogisticRegression()
    model  = RegressionModel(logistic_regression_model)

    dataset = datasets.load_breast_cancer()

    #split data intro traning (70 %), validation(15 %) and test data(15 %)
    model.split_data(dataset.data, dataset.target, 0.70, 0.15, 0.15)

    #fit data to model
    model.fit_data()

    validation_data = model.get_validation_data()
    predicted_data = model.predict_data(validation_data)
    validation_data_target = model.get_validation_data_targets()

    test_data = model.get_test_data()
    predicted_data_test = model.predict_data(test_data)
    test_data_target = model.get_test_data_targets()

    print("F1 score using validation data: " + str(model.get_f1_score(predicted_data, validation_data_target)))
    f1_score = round(model.get_f1_score(predicted_data_test, test_data_target), 4)

    confusion_matrix = model.get_confusion_matrix(predicted_data_test, test_data_target)
    graph.setup_heatmap(confusion_matrix, "Breast cancer dataset prediction analysis \n F1 Score using test data: " + str(f1_score))
    graph.get_heatmap()


def show_menu():
    menu = "Enter the number of the option you want to select: \n"
    menu += "1. Linear multiple regression model with Iris dataset. \n" 
    menu += "2. Logistic regression model with breast cancer dataset. \n"
    menu += "3. Exit. \n"
    menu += "Option: "

    while True:
        option = int(input(menu))
        if option == 1:
            linear_multiple_regression_controller()
        elif option == 2:
            logistic_regression_controller()
        elif option == 3: 
            break
        else:
            print("Enter a valid number \n")


def main():
   show_menu()
   
if __name__ == '__main__':
    main()