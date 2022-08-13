from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

import model.FileManager as FileManager
import model.Graphs as Graphs
import model.RegressionModel as RegressionModel

class Controller:
    def __init__(self) -> None:
        pass

    def model_controller(self, data_name:str, target_name:str, model_type:str):
        model = None
        file_manager = FileManager.FileManager()
        if model_type == "1":
            model = LinearRegression()
        else:
            model = LogisticRegression()
        
        model  = RegressionModel.RegressionModel(model)
        data = file_manager.read_csv(data_name)
        target = file_manager.read_csv(target_name)
        model.split_data(data, target, 0.70, 0.15, 0.15)

        # #fit data to model
        model.fit_data()

        validation_data = model.get_validation_data()
        predicted_validation_data = model.predict_data(validation_data)
        validation_target = model.get_validation_data_targets()

        test_data = model.get_test_data()
        test_target = model.get_test_data_targets()
        predicted_data_test = model.predict_data(test_data)

        if model_type == "1":
            mse_test_data = round(model.get_mean_squared_error(predicted_data_test, test_target), 4)
            print("MSE: " + str(mse_test_data))
            text = data_name + "\n Mean squared error using test data: " + str(mse_test_data)
            graph_test = self.__show_plot(text, test_data, predicted_data_test, test_target)

            mse_validation_data = round(model.get_mean_squared_error(predicted_validation_data, validation_target), 4)
            text = data_name + "\n Mean squared error using test data: " + str(mse_validation_data)
            graph_validation = self.__show_plot(text, validation_data, predicted_validation_data, validation_target)
        else:
            f1_score_test = round(model.get_f1_score(predicted_data_test, test_target), 4)
            print("F1 score: " + str(f1_score_test))
            confusion_matrix = model.get_confusion_matrix(predicted_data_test, test_target)
            graph_test = self.__show_heatmap(data_name + "\n F1 Score using test data: " + str(f1_score_test), confusion_matrix)

            f1_score_validation = round(model.get_f1_score(predicted_validation_data, validation_target), 4)
            confusion_matrix = model.get_confusion_matrix(predicted_validation_data, validation_target)
            graph_validation = self.__show_heatmap(data_name + "\n F1 Score using validation data: " + str(f1_score_validation), confusion_matrix)

        return graph_test, graph_validation

    def __show_plot(self, text:str, data:list, predicted_data:list, targets:list):
        graph = Graphs.Graphs()
        graph.setup_plot(data, targets, predicted_data, text, "Data ID", "Predicted values")
        return graph.get_graph()

    def __show_heatmap(self, text:str, confusion_matrix:list):
        graph = Graphs.Graphs()
        graph.setup_heatmap(confusion_matrix, text)
        return graph.get_graph()
    