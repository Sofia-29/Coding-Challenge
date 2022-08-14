import base64
from io import BytesIO
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
        plt.switch_backend('AGG')
        plt.figure(figsize=(5, 5))
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
        plt.switch_backend('AGG')
        plt.figure(figsize=(3, 3))
        display = []
        for index in range(len(matrix)):
            if index % 2 == 0:
                display.append(False)
            else:
                display.append(True)
        matrix_display = ConfusionMatrixDisplay(confusion_matrix = matrix, display_labels = display)
        matrix_display.plot(cmap='Greens')
        plt.title(title)

    def get_heatmap(self):
        '''
            Shows heatmap graph previously set
        '''
        plt.show()
    
    def get_graph(self):
        '''
            Returns graph previously set as an image
        '''
        plt.tight_layout()
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
        return graph