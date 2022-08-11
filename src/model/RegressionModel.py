from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

class RegressionModel:
    
    def __init__(self, regression_model):
        self.__regression_model = regression_model
        self.__training_data = []
        self.__training_data_targets = []
        self.__validation_data = []
        self.__validation_data_targets = []
        self.__test_data = []
        self.__test_data_targets = []

    def get_training_data(self):
        return self.__training_data
    
    def get_validation_data(self):
        return self.__validation_data
    
    def get_test_data(self):
        return self.__test_data

    def get_training_data_targets(self):
            return self.__training_data_targets
    
    def get_validation_data_targets(self):
        return self.__validation_data_targets
    
    def get_test_data_targets(self) -> list:
        return self.__test_data_targets

    def split_data(self, data, targets, training_data_percentage:int, validation_data_percentage:int, test_data_percentage:int):
        test_size = validation_data_percentage + test_data_percentage
        #Split training data
        self.__training_data, self.__validation_data, self.__training_data_targets, self.__validation_data_targets = train_test_split(
            data, targets, test_size = test_size, train_size = training_data_percentage)
        #Split validation and test data
        self.__validation_data, self.__test_data, self.__validation_data_targets, self.__test_data_targets = train_test_split(
            self.__validation_data, self.__validation_data_targets,  test_size = 0.50)
        
    def fit_data(self):
        self.__regression_model.fit(self.__training_data, self.__training_data_targets)
  
    def predict_data(self, data:list):
        return self.__regression_model.predict(data)
    
    def get_mean_squared_error(self, predicted_data:list, true_data:list):
        return mean_squared_error(predicted_data, true_data)
    
    def get_f1_score(self, predicted_data:list, true_data:list):
        return f1_score(true_data, predicted_data, average='micro')

    def get_confusion_matrix(self, predicted_data:list, true_data:list):
        return confusion_matrix(true_data, predicted_data)