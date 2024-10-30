from controller.csvcontroller import CSVController

def tresMotivos(test):
    motivos = test.getByHeader('Tempo Médio do atendimento')

    motivos.sort()
    print(motivos)

    soma = 0
    for i in range(0, len(motivos)-1):
        if motivos[i] == '':
            soma += 0
        else:
            soma += int(motivos[i])

    print(len(motivos))
    print(soma)

if __name__ == '__main__':
    test = CSVController('C:\\Users\\Vinicius\\Documents\\Vinicius\\Docnuvem\\prjDocSis\\model\\excel.csv')
    
    tresMotivos(test)