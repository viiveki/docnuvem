import csv

class CSVData:
    def __init__(self, csv_file):
        self.file = csv_file
        self.header = []
        self.data = []

        self.readFile()
    
    # Le o arquivo, alimenta o cabecalho e recolhe os dados
    def readFile(self):
        file = open(self.file, mode='r', encoding='utf-8')

        try:
            reader = csv.reader(file, delimiter=';')

            self.header = next(reader)

            for line in reader:
                data = {}

                for column in self.header:
                    data[column] = line[self.header.index(column)]
                
                self.data.append(data)
        finally:
            file.close()


if __name__ == '__main__':
    test = CSVData('C:\\Users\\Vinicius\\Documents\\Vinicius\\Docnuvem\\prjDocSis\\model\\excel.csv')
    test.readFile()
    print(test.data)