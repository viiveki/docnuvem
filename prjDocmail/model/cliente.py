from .database import connect, disconnect, execute_query

# ====
# Lida com as consultas SQL apenas, nao deve lidar com a logica de conexao
# ====

# Atributos
#cnpj_cpf - integer = PK
#cliente - Character
#url    - Character  :: url da instancia

def get_all():
    query = '''
            SELECT *
            FROM docmail.cliente;
            '''

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def get_by_id(cnpj_cpf):
    query = '''
            SELECT *
            FROM docmail.cliente
            WHERE cnpj_cpf = {cnpj_cpf};
            '''.format(cnpj_cpf = cnpj_cpf)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def get_by_name(cliente):
    query = '''
            SELECT *
            FROM docmail.cliente
            WHERE cliente = {cliente};
            '''.format(cliente = cliente)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def get_by_url(url):
    query = '''
            SELECT *
            FROM docmail.url
            WHERE url = {url};
            '''.format(url = url)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def new_cliente(cnpj_cpf, cliente, url):
    query = '''
            INSERT INTO docmail.cliente VALUES (
                {cnpj_cpf},
                {cliente},
                {url}
            );
            '''.format(cnpj_cpf = cnpj_cpf, cliente = cliente, url = url)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def replace_cliente(cnpj_cpf, cliente, url):
    query = '''
            UPDATE docmail.cliente SET
                cnpj_cpf = {cnpj_cpf},
                cliente = {cliente},
                url = {url},
            WHERE cnpj_cpf = {cnpj_cpf};
            '''.format(cnpj_cpf = cnpj_cpf, cliente = cliente, url = url)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def delete_cliente(cnpj_cpf):
    query = '''
            DELETE FROM docmail.cliente
            WHERE cnpj_cpf = {cnpj_cpf}
            '''.format(cnpj_cpf = cnpj_cpf)
    
    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result