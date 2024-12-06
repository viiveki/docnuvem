from controller.csvcontroller import CSVController
from controller.datatreatment import DataTreatment

def tresMotivos(csv_controller):
    tempo = csv_controller.getByHeader('Tempo Médio do atendimento')
    soma = 0

    for t in tempo:
        if t != '':
            soma += int(t)
    
    print('O total de tempo de suporte em min. foi: {0}'.format(soma))
    print('O tempo médio de suporte em min. foi: {0:.2f}'.format((soma/len(tempo))))

# Usando a coluna "Problemas" do csv, separa somente o que foi chamado de suporte do que foi chamado de implantacao
def chamadosSuporte(csv_controller):
    problemas = csv_controller.getByHeader('Problemas')
    problemas.sort()

    implantacao = DataTreatment.separateValueInList('implantação - '.upper(), problemas)

    print('Quantidade de chamados de suporte: {0}'.format((len(problemas) - len(implantacao))))
    print('Quantidade de chamados de implantacao: {0}'.format(len(implantacao)))
    print(problemas)

# Usando a coluna "Situacao" do csv, separa o status de chamados
def statusChamados(csv_controller):
    situacao = csv_controller.getByHeader('Situação')

    em_espera = DataTreatment.separateValueInList('Em espera'.upper(), situacao)
    em_atendimento = DataTreatment.separateValueInList('Em atendimento'.upper(), situacao)
    desenvolvimento = DataTreatment.separateValueInList('Aguardando resposta do desenvolvimento'.upper(), situacao)
    concluido = DataTreatment.separateValueInList('Concluído'.upper(), situacao)

    print('Quantidade de chamados "Em espera": {0}\n'
          'Quantidade de chamados "Em atendimento": {1}\n'
          'Quantidade de chamados "Aguardando resposta do desenvolvimento": {2}\n'
          'Quantidade de chamados "Concluído": {3}\n'
          .format(len(em_espera), len(em_atendimento), len(desenvolvimento), len(concluido)))

# Usando a coluna "Apoio ao atendimento" do csv, separa quem atendeu os chamados
def chamadosAtendidos(csv_controller):
    atendimento = csv_controller.getByHeader('Apoio ao atendimento')

    vinicius = DataTreatment.separateValueInList('Vinícius Alves de Araújo'.upper(), atendimento)
    breno = DataTreatment.separateValueInList('Breno Nunes Batista'.upper(), atendimento)

    print('Quantidade de chamados pelo Vinícius: {0}'.format(len(vinicius)))
    print('Quantidade de chamados pelo Breno: {0}'.format(len(breno)))
    #print(vinicius)
    #print(breno)

def clientes(csv_controller):
    solicitantes = csv_controller.getByHeader('Solicitante')

    clientes = DataTreatment.separeteClienteInSolicitante(solicitantes)

    print(clientes)

if __name__ == '__main__':
    test = CSVController('C:\\Users\\Vinicius\\Documents\\Vinicius\\My\\docnuvem\\prjDocSis\\atendimentos.csv')
    
    #tresMotivos(test)
    #chamadosSuporte(test)
    #statusChamados(test)
    #chamadosAtendidos(test)
    clientes(test)
