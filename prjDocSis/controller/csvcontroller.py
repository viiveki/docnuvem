from model.csvdata import CSVData

class CSVController:
    def __init__(self, csv_file):
        self.csvdata = CSVData(csv_file)
    
    def getAllHeader(self):
        return self.csvdata.header
    
    def getHeaderIndex(self, column_name):
        for i in range(1, len(self.csvdata.header)):
            if (self.csvdata.header[(i-1)] == column_name):
                return i
        
        return 'Não foi possível encontrar "{0}" dentre os valores de cabeçalho.'.format(column_name)

    def getAll(self):
        return self.csvdata.data
    
    def getAllData(self):
        data = []

        for item in self.csvdata.data:
            for column in self.csvdata.header:
                data.append(item[column])

        return data
    
    def getByHeader(self, column_name):
        data = []

        for item in self.csvdata.data:
            data.append(item[column_name])
        
        return data

if __name__ == '__main__':
    test = CSVController('C:\\Users\\Vinicius\\Documents\\Vinicius\\Docnuvem\\prjDocSis\\model\\excel.csv')
    test.getHeaderIndex('Número')