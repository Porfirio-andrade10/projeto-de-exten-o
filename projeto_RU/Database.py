import mysql.connector
from mysql.connector import Error


class Database:
    """
    Classe responsável pela conexão com o banco de dados MySQL.
    Esta classe fornece métodos para executar consultas (query) e 
    buscar dados (fetch) de forma centralizada.
    """

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados MySQL.
        A conexão é estabelecida com os parâmetros fornecidos: host, database, 
        user e password.
        """
        try:
            # Defina as credenciais e o banco de dados ao qual conectar
            self.conexao = mysql.connector.connect(
                host='localhost',
                database='gerenciador_de_estoque',    # Nome do seu banco de dados
                user='root',        # Seu usuário do MySQL
                password='root'       # Sua senha do MySQL
            )
            # Cria um cursor para executar comandos SQL
            self.cursor = self.conexao.cursor()
            print("Conexão estabelecida com sucesso!")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados MySQL: {e}")

    def execute_query(self, query_params):
        """
        Executa uma consulta (INSERT, UPDATE, DELETE) no banco de dados.
        Parâmetros:
        - query: Comando SQL a ser executado.
        - params: Valores a serem substituídos na consulta, se houver.
        """
        try:
            self.cursor.execute(query_params)
            self.conexao.commit()  # Confirma as mudanças no banco
        except Error as e:
            print(f"Erro ao executar query: {e}")

    def fetch_query(self, query_params):
        """
        Executa uma consulta (SELECT) e retorna os resultados.
        Parâmetros:
        - query: Comando SQL a ser executado.
        - params: Valores a serem substituídos na consulta, se houver.
        Retorna:
        - Lista com os resultados da consulta.
        """
        try:
            self.cursor.execute(query_params)
            return self.cursor.fetchall()  # Retorna os dados buscados
        except Error as e:
            print(f"Erro ao buscar dados: {e}")

    def close(self):
        """
        Fecha a conexão com o banco de dados e o cursor.
        Verifica se a conexão está ativa e a encerra corretamente.
        """
        if self.conexao.is_connected():
            self.cursor.close()
            self.conexao.close()
            print("Conexão ao MySQL fechada.")
