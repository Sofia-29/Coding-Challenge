from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from .forms import DataForm
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from model.RegressionModel import RegressionModel
from model.Graphs import Graphs
from model.FileManager import FileManager



def index(response):
    if response.method == 'POST':   
        form = DataForm(response.POST, response.FILES)
        if form.is_valid(): 
            
            data = form.cleaned_data["data"]
            targets = form.cleaned_data["targets"]
            model_type = form.cleaned_data["model_type"]
            file_system = FileSystemStorage()
            file_system.save(data.name, data)
            file_system.save(targets.name, targets)
            graph_test, graph_validation = controller(data.name, targets.name, model_type)
            
            return render(response, "main/results.html", {"chart_test": graph_test, "chart_validation":graph_validation})
    else:
        form = DataForm()
    return render(response, "main/home.html", {"form":form})

def results(response):
    return render(response, "main/results.html", {})

def controller(data:str, target:str, model_type:str):
    
    model = None
    graph = Graphs()
    file_manager = FileManager()
    if model_type == "1":
        model = LinearRegression()
    else:
        model = LogisticRegression()
    
    model  = RegressionModel(model)
    data = file_manager.read_csv(data)
    target = file_manager.read_csv(target)
    model.split_data(data, target, 0.70, 0.15, 0.15)

    # #fit data to model
    model.fit_data()

    validation_data = model.get_validation_data()
    predicted_validation_data = model.predict_data(validation_data)
    validation_target = model.get_validation_data_targets()

    test_data = model.get_test_data()
    test_target = model.get_test_data_targets()
    predicted_data_test = model.predict_data(test_data)

    if model_type =="1":
        mse_test_data = round(model.get_mean_squared_error(predicted_data_test, test_target), 4)
        graph.setup_plot(test_data, test_target, predicted_data_test, 
            "Iris Species" + "\n" + "Iris Setosa = 0 Iris Versicolor = 1 Iris Virginica = 2 \n Mean squared error using test data: " + str(mse_test_data),
                "Iris id", "Predicted values")
        graph_test = graph.get_graph()

        mse_validation_data = round(model.get_mean_squared_error(predicted_validation_data, validation_target), 4)
        graph.setup_plot(validation_data, validation_target, predicted_validation_data, 
            "Iris Species" + "\n" + "Iris Setosa = 0 Iris Versicolor = 1 Iris Virginica = 2 \n Mean squared error using validation data: " + str(mse_validation_data),
                "Iris id", "Predicted values")
        graph_validation = graph.get_graph()
    else:
        f1_score_test = round(model.get_f1_score(predicted_data_test, test_target), 4)
        confusion_matrix = model.get_confusion_matrix(predicted_data_test, test_target)
        graph.setup_heatmap(confusion_matrix, "Breast cancer dataset prediction analysis \n F1 Score using test data: " + str(f1_score_test))

        f1_score_validation = round(model.get_f1_score(predicted_validation_data, validation_target), 4)
        confusion_matrix = model.get_confusion_matrix(predicted_validation_data, validation_target)
        graph.setup_heatmap(confusion_matrix, "Breast cancer dataset prediction analysis \n F1 Score using validation data: " + str(f1_score_validation))

    return graph_test, graph_validation
