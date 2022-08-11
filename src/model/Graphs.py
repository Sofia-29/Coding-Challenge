import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay

class Graphs:

    def __init__(self) -> None:
        pass

    def setup_plot(self, x_axis_data:list, y_axis_data, title:str, x_label:str, y_label:str):
        '''
            Setup scatterplot graph for showing data

            PARAMS

            x_axis_data:list, list containing x axis data
            y_axis_data, list containing y axis data
            title:str, title of graph
            x_label:str, x label of graph
            y_label:str, y label of graph

        '''
        plt.scatter(x_axis_data, y_axis_data, color = 'black')
        plt.plot(x_axis_data, y_axis_data, color = "green")
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
    
    