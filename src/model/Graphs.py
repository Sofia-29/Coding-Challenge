import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay

class Graphs:

    def __init__(self) -> None:
        pass
    
    def setup_plot(self, x_axis_data:list, y_axis_data, title:str, x_label:str, y_label:str):
        plt.scatter(x_axis_data, y_axis_data, color = 'black')
        plt.plot(x_axis_data, y_axis_data, color = "green")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    
    def show_plot(self):
        plt.show()

    def setup_heatmap(self, matrix:list, title:str):
        matrix_display = ConfusionMatrixDisplay(confusion_matrix = matrix, display_labels = [False, True])
        matrix_display.plot(cmap='Greens')
        plt.title(title)

    def get_heatmap(self):
        plt.show()
    
    