from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from .forms import DataForm

from model.Controller import Controller

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
            controller = Controller()
            graph_test, graph_validation = controller.model_controller(data.name, targets.name, model_type)
            model_type = True if model_type == "1" else False
            return render(response, "model_view/results.html", {"model_type":model_type,"chart_test": graph_test, "chart_validation":graph_validation})
    else:
        form = DataForm()
    return render(response, "model_view/home.html", {"form":form})

def results(response):
    return render(response, "model_view/results.html", {})
