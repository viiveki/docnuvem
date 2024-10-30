from .database import connect, disconnect, execute_query

# ====
# Lida com as consultas SQL apenas, nao deve lidar com a logica de conexao
# ====

# Atributos
#codigo - integer = PK
#descricao - Character
    # 0-DOCBasic
    # 1-DOCStarter
    # 2-DOCPremium
    # 3-DOCNUVEM - Assinatura

def get_all():
    query = '''
            SELECT *
            FROM docmail.plano;
            '''

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def get_by_id(codigo):
    query = '''
            SELECT *
            FROM docmail.plano
            WHERE codigo = {codigo};
            '''.format(codigo = codigo)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def get_by_plano(descricao):
    query = '''
            SELECT *
            FROM docmail.plano
            WHERE descricao = '{descricao}';
            '''.format(descricao = descricao)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def new_plano(codigo, descricao):
    query = '''
            INSERT INTO docmail.plano VALUES (
                {codigo},
                '{descricao}'
            );
            '''.format(codigo = codigo, descricao = descricao)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def replace_plano(codigo, descricao):
    query = '''
            UPDATE docmail.plano SET
                codigo = {codigo},
                descricao = '{descricao}'
            WHERE codigo = {codigo};
            '''.format(codigo = codigo, descricao = descricao)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def delete_plano(codigo):
    query = '''
            DELETE FROM docmail.plano
            WHERE codigo = {codigo}
            '''.format(codigo = codigo)
    
    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result