from model.csvdata import CSVData

class CSVController:
    def __init__(self, csv_file):
        self.csvdata = CSVData(csv_file)
    
    # Retorna a lista de cabecalho que extrai do documento CSV
    def getAllHeader(self):
        return self.csvdata.header
    
    # Retorna os dados que fazem parte da coluna do cabecalho escolhido
    def getByHeader(self, column_name):
        data = []

        for item in self.csvdata.data:
            data.append(item[column_name])
        
        return data
    
    # Retorna o index de um cabecalho, passando o nome
    def getHeaderIndex(self, column_name):
        for i in range(1, len(self.csvdata.header)):
            if (self.csvdata.header[(i-1)] == column_name):
                return i
        
        return 'Não foi possível encontrar "{0}" dentre os valores de cabeçalho.'.format(column_name)

    # Como eh um dicionario, retorna tanto os dados quanto os valores
    def getAll(self):
        return self.csvdata.data
    
    # Retorna somente a lista de todos os valores do dicionario cabecalho/valor
    def getAllData(self):
        data = []

        for item in self.csvdata.data:
            for column in self.csvdata.header:
                data.append(item[column])

        return data

if __name__ == '__main__':
    test = CSVController('C:\\Users\\Vinicius\\Documents\\Vinicius\\Docnuvem\\prjDocSis\\model\\excel.csv')
    test.getHeaderIndex('Número')