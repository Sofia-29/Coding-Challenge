from cProfile import label
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import numpy as np

class Graphs:

    def __init__(self) -> None:
        pass

    def setup_plot(self, x_axis_data:list, y_axis_data, predicted_data:list, title:str, x_label:str, y_label:str):
        '''
            Setup scatterplot graph for showing data

            PARAMS

            x_axis_data:list, list containing x axis data
            y_axis_data, list containing y axis data
            predicted_data:list, list containing all predicted data by the model
            title:str, title of graph
            x_label:str, x label of graph
            y_label:str, y label of graph

        '''
        plt.scatter(np.arange(0, len(x_axis_data), 1), y_axis_data, color = 'black')
        plt.plot(np.arange(0, len(x_axis_data), 1), predicted_data, color = "green")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    
    def show_plot(self):
        '''
            Shows scatterplot graph previously set
        '''
        plt.show()

    def setup_heatmap(self, matrix:list, title:str):
        '''
            Setup heatmap for showing data

            PARAMS

            x_axis_data:list, list containing x axis data
            y_axis_data, list containing y axis data
            title:str, title of graph
        '''
        matrix_display = ConfusionMatrixDisplay(confusion_matrix = matrix, display_labels = [False, True])
        matrix_display.plot(cmap='Greens')
        plt.title(title)

    def get_heatmap(self):
        '''
            Shows heatmap graph previously set
        '''
        plt.show()
    
    