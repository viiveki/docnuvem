from controller.csvcontroller import CSVController

class DataTreatment:
    def __init__(self):
        pass
    
    def separeteClienteInSolicitante(solicitantes):
        cliente = []

        for data in solicitantes:
            data = data.upper()

            # Obtem o primeiro valor index da palavra encontrada com o find
            start_cliente = data.find('cliente:'.upper())
            
            # Quando eh -1, significa que nao encontrou a substring passada no find
            if (start_cliente != -1):
                start_cliente = start_cliente + len('cliente: ')

                cliente.append(data[start_cliente:(len(data)+1)])
        
        return cliente

    def separateVendedorInSolicitante(solicitantes):
        vendedor = []

        for data in solicitantes:
            data = data.upper()

            # Obtem o primeiro valor index da palavra encontrada com o find
            start_vendedor = data.find('vendedor:'.upper())
            end_vendedor = data.find('</br>'.upper())

            # Quando eh -1, significa que nao encontrou a substring passada no find
            if (start_vendedor != -1):
                start_vendedor = start_vendedor + len('vendedor: ')

                vendedor.append(data[start_vendedor:end_vendedor])
            
        return vendedor
    
    # Pode ser usado para separar em status na lista de situacao, parar separar os tipos de problemas em problemas, responsaveis do suporte e etc.
    def separateValueInList(value, list):
        sublist = []

        for data in list:
            data = data.upper()

            if (data.find(value.upper()) != -1):
                sublist.append(data)
        
        return sublist