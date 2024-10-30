from .database import connect, disconnect, execute_query

# ====
# Lida com as consultas SQL apenas, nao deve lidar com a logica de conexao
# ====

# Atributos
#codigo - integer = PK
#email - Character

def get_all():
    query = '''
            SELECT *
            FROM docmail.email;
            '''

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def get_by_id(codigo):
    query = '''
            SELECT *
            FROM docmail.email
            WHERE codigo = {codigo};
            '''.format(codigo = codigo)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def get_by_email(email):
    query = '''
            SELECT *
            FROM docmail.email
            WHERE email = {email};
            '''.format(email = email)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def new_email(codigo, email):
    query = '''
            INSERT INTO docmail.email VALUES (
                {codigo},
                {email}
            );
            '''.format(codigo = codigo, email = email)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def replace_email(codigo, email):
    query = '''
            UPDATE docmail.email SET
                codigo = {codigo},
                email = {email}
            WHERE codigo = {codigo};
            '''.format(codigo = codigo, email = email)

    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result

def delete_cliente(codigo):
    query = '''
            DELETE FROM docmail.email
            WHERE codigo = {codigo}
            '''.format(codigo = codigo)
    
    connection = connect()
    result = execute_query(connection, query)
    disconnect(connection)

    return result