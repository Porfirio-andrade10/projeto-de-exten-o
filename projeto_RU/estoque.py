from projeto_RU import Database


class Estoque:
    """
    Classe responsável por gerenciar o estoque de alimentos.
    Ela interage com uma tabela no banco de dados MySQL, cujo nome é fornecido na instância.
    """

    def __init__(self, db: Database):
        """
        :param db: Instância da classe Database para realizar as operações

        """
        self.db = db  # Instância da classe Database para realizar as operações
        

    def adicionar_no_estoque(self,nome_tabela, nome_produto, unidade_medida, custo, quantidade, data_validade):
        """
        Adiciona um novo produto à tabela de estoque no banco de dados.
        """
        query_params = f"INSERT INTO {nome_tabela} (unidade_medida, nome, custo, quantidade_estoque, data_validade) VALUES ('{unidade_medida}', '{nome_produto}', {custo}, {quantidade}, '{data_validade}')"
        self.db.execute_query(query_params)
        print(f"Produto '{nome_produto}' adicionado com sucesso à tabela '{nome_tabela}'.")
        

    def remover_do_estoque(self,nome_tabela,nome_produto):
        """
        Remove um produto da tabela de estoque no banco de dados.
        """
        query_params = f"DELETE FROM {nome_tabela} WHERE nome = '{nome_produto}'"

        self.db.execute_query(query_params)
        print(f"Produto '{nome_produto}' removido com sucesso da tabela '{nome_tabela}'.")

    def atualizar_estoque(self, nome_tabela, nome_produto, nova_quantidade):
        """
        Atualiza a quantidade de um produto no estoque.
        """
        query_params = f"UPDATE {nome_tabela} SET quantidade_estoque = {nova_quantidade} WHERE nome = '{nome_produto}'"
        self.db.execute_query(query_params)
        print(f"Estoque do produto '{nome_produto}' atualizado para {nova_quantidade} na tabela '{nome_tabela}'.")

    def listar_estoque(self,nome_tabela):
        """
        Lista todos os produtos disponíveis na tabela de estoque.
        """
        query = f"SELECT * FROM {nome_tabela}"
        resultado = self.db.fetch_query(query)
        return resultado if resultado is not None else 0

def main():
    db= Database()
    Est = Estoque(db)
    # Criar a aplicação passando a instância de Estoque
    

    db.execute_query()
if __name__ == "__main__":
    main()
