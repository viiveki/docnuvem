import psycopg2
import configparser

# ====
# Lida com a configuracao e conexao com a base de dados
# ====

DBFILE = 'model/database.ini'
DBSECTION = 'postgresql'

# Faz a leitura do arquivo .ini de configuracao com o banco de dados
def get_db_config(filename=DBFILE, section=DBSECTION):
    parser = configparser.ConfigParser()
    data = {}

    # Trata erro ao tentar decoficar o formato (UTF-8) do arquivo em filename
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            parser.read_file(file)
    except UnicodeDecodeError as error:
        print('Error decoding file "{0}": {1}'.format(filename, error))
        return data

    try:
        if parser.has_section(section):
            params = parser.items(section)

            for param in params:
                data[param[0]] = param[1]
    except Exception as error:
        print('Section {0} not found in {1} file'.format(section, filename))

    return data

# Faz a conexao com o banco de dados PostgreSQL
def connect():
    try:
        config = get_db_config()
        connection = psycopg2.connect(**config)
        connection.autocommit = True

        print('Connected to the PostgreSQL server')
        return connection
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Defaz a conexao com o banco de dados PostgreSQL
def disconnect(connection):
    try:
        if connection is not None:
            connection.close
            print('Disconnected to the PostgreSQL server')
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Funcao que executa uma consulta no banco
def execute_query(connection, query):
    try:
        print(query)

        cursor = connection.cursor()
        cursor.execute(query)
        
        rows = cursor.fetchall()
        
        cursor.close()
        return rows
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Se esse arquivo config for o principal, executa as funcoes abaixo
if __name__ == '__main__':
    connection = connect()
    disconnect(connection)