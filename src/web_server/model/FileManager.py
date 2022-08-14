from csv import reader

class FileManager:
    def __init__(self) -> None:
        pass

    def read_csv(self, file:str):
        '''
            Reads csv given file name

            PARAMS

            file:str, file name

        '''
        data_list = []
        file_path = "media/" + file

        with open(file_path, "r", encoding="utf-8") as my_file:
            file_reader = reader(my_file)
            for index in file_reader:
                value = None
                if len(index) != 1:
                    value = self.cast_list(index)
                else:
                    value = float(index[0])
                data_list.append(value)
            return data_list
    
    def cast_list(self, list:list):
        '''
            Cast a list of char to float

            PARAMS

            list:list, list of char

        '''
        new_list = []
        for index in list:
            new_list.append(float(index))
        return new_list
        

    
