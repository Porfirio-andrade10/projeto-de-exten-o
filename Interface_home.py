import PySimpleGUI as sg
from projeto_RU import Database,Estoque
from fpdf import * 

sg.theme('DarkBlue')


db= Database()
Est = Estoque(db)


class Updd_estoque_Interface:
    def __init__(self, estoque: Estoque):
        self.estoque = estoque
        # Layout da interface gráfica
        self.nomes_tabelas = ["alimentos_nao_pereciveis", "carne", "hortifruti","descartaveis"]

        self.layout = [
            [sg.Text("Nome da tabela:"), sg.Combo(self.nomes_tabelas, key="nome_tabela", readonly=True)],
            [sg.Text("Nome do Produto:"), sg.InputText(key="nome_produto")],
            [sg.Text("Quantidade:"), sg.InputText(key="quantidade")],
            [sg.Multiline(size=(60, 5), key='-LISTAR_TABELA-')],
            [sg.Button("Adicionar Produto"), sg.Button("Listar Estoque")],
            [sg.Button("Fechar")]
        ]

        # Criação da janela
        self.window = sg.Window("Atualizar Estoque", self.layout)

    def adicionar_produto(self, nome_tabela, nome_produto, quantidade):
        """
        Função para adicionar um produto ao estoque no banco de dados.
        """
        if nome_produto and quantidade:
            # Corrigir chamada para usar self.estoque
            self.estoque.atualizar_estoque(nome_tabela, nome_produto, quantidade)
            sg.popup("Produto atualizado com sucesso!")
        else:
            sg.popup_error("Por favor, preencha todos os campos.")

    def listar_estoque(self, nome_tabela):
        """
        Função para listar todos os produtos do estoque.
        """
        try:
            # Consultar o estoque
            resultado = self.estoque.listar_estoque(nome_tabela)
            self.window['-LISTAR_TABELA-'].update('')

            if resultado:
                self.window['-LISTAR_TABELA-'].print([f"Nome: {row[2]}, Quantidade: {row[4]}, Data de validade : {row[5]}" for row in resultado])
                
            else:
                sg.popup("Estoque", "Nenhum produto encontrado.")
        except Exception as e:
            sg.popup_error(f"Erro: {e}")

    def fechar_app(self):
        """
        Função para fechar a aplicação.
        """
        self.window.close()

    def executar(self):
        """
        Função principal que roda o loop de eventos da interface.
        """
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == "Fechar":
                self.fechar_app()
                break
            elif event == "Adicionar Produto":
                nome_tabela = values["nome_tabela"]
                nome_produto = values["nome_produto"]
                quantidade = int(values["quantidade"])
                self.adicionar_produto(nome_tabela, nome_produto, quantidade)
            elif event == "Listar Estoque":
                nome_tabela = values["nome_tabela"]
                self.listar_estoque(nome_tabela)

class Add_estoque_Interface:
    def __init__(self, estoque: Estoque):
        self.estoque = estoque
        # Layout da interface gráfica
        self.nomes_tabelas = ["alimentos_nao_pereciveis", "carne", "hortifruti","descartaveis"]
        self.unidade_medida = ["KG", "PACT", "UN","MACO"]

        self.layout = [
            [sg.Text("Nome da tabela:"), sg.Combo(self.nomes_tabelas, key="nome_tabela", readonly=True)],
            [sg.Text("Nome do Produto:"), sg.InputText(key="nome_produto")],
            [sg.Text("Unidade de medida:"), sg.Combo(self.unidade_medida, key="unidade_medida", readonly=True)],
            [sg.Text("Quantidade:"), sg.InputText(key="quantidade")],
            [sg.Text("Custo:"), sg.InputText(key="custo")],
            [sg.Text("Data de validade:"), sg.InputText(key="data_validade")],
            [sg.Multiline(size=(60, 5), key='-LISTAR_TABELA-')],
            [sg.Button("Adicionar Produto"), sg.Button("Listar Estoque")],
            [sg.Button("Fechar")]
        ]

        # Criação da janela
        self.window = sg.Window("Adicionar Novo Alimento", self.layout)

    def adicionar_novo_produto(self, nome_tabela, nome_produto, unidade_medida, custo, quantidade, data_validade):
        """
        Função para adicionar um produto ao estoque no banco de dados.
        """
        if nome_produto and quantidade and unidade_medida and data_validade:
            # Corrigir chamada para usar self.estoque
            self.estoque.adicionar_no_estoque(nome_tabela, nome_produto, unidade_medida, custo, quantidade, data_validade)
            sg.popup("Produto adicionado com sucesso!")
        else:
            sg.popup_error("Por favor, preencha todos os campos.")

    def listar_estoque(self, nome_tabela):
        """
        Função para listar todos os produtos do estoque.
        """
        try:
            # Consultar o estoque
            resultado = self.estoque.listar_estoque(nome_tabela)
            self.window['-LISTAR_TABELA-'].update('')

            if resultado:
                self.window['-LISTAR_TABELA-'].print([f"Nome: {row[2]}, Quantidade: {row[4]}, Data de validade : {row[5]}" for row in resultado])
                
            else:
                sg.popup("Estoque", "Nenhum produto encontrado.")
        except Exception as e:
            sg.popup_error(f"Erro: {e}")

    def fechar_app(self):
        """
        Função para fechar a aplicação.
        """
        self.window.close()

    def executar(self):
        """
        Função principal que roda o loop de eventos da interface.
        """
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == "Fechar":
                self.fechar_app()
                break
            elif event == "Adicionar Produto":
                nome_tabela = values["nome_tabela"]
                nome_produto = values["nome_produto"]
                quantidade = int(values["quantidade"])
                unidade_medida = values["unidade_medida"]
                data_validade = values["data_validade"]
                custo = values["custo"]
                self.adicionar_novo_produto(nome_tabela, nome_produto, unidade_medida, custo, quantidade, data_validade)
            elif event == "Listar Estoque":
                nome_tabela = values["nome_tabela"]
                self.listar_estoque(nome_tabela)

class Rem_estoque_Interface:

    def __init__(self, estoque: Estoque):
        self.estoque = estoque
        # Layout da interface gráfica
        self.nomes_tabelas = ["alimentos_nao_pereciveis", "carne", "hortifruti","descartaveis"]

        self.layout = [
            [sg.Text("Nome da tabela:"), sg.Combo(self.nomes_tabelas, key="nome_tabela", readonly=True)],
            [sg.Text("Nome do Produto:"), sg.InputText(key="nome_produto")],
            [sg.Multiline(size=(60, 5), key='-LISTAR_TABELA-')],
            [sg.Button("Remover da tabela"), sg.Button("Listar Estoque")],
            [sg.Button("Fechar")]
        ]

        # Criação da janela
        self.window = sg.Window("Remover alimento Estoque", self.layout)

    def remover_do_estoque(self, nome_tabela, nome_produto):
        """
        Função para adicionar um produto ao estoque no banco de dados.
        """
        if nome_produto:
            # Corrigir chamada para usar self.estoque
            self.estoque.remover_do_estoque(nome_tabela, nome_produto)
            sg.popup("Produto Removido com sucesso!")
        else:
            sg.popup_error("Por favor, preencha todos os campos.")

    def listar_estoque(self, nome_tabela):
        """
        Função para listar todos os produtos do estoque.
        """
        try:
            # Consultar o estoque
            resultado = self.estoque.listar_estoque(nome_tabela)
            self.window['-LISTAR_TABELA-'].update('')

            if resultado:
                self.window['-LISTAR_TABELA-'].print([f"Nome: {row[2]}, Quantidade: {row[4]}, Data de validade : {row[5]}" for row in resultado])
                
            else:
                sg.popup("Estoque", "Nenhum produto encontrado.")
        except Exception as e:
            sg.popup_error(f"Erro: {e}")

    def fechar_app(self):
        """
        Função para fechar a aplicação.
        """
        self.window.close()

    def executar(self):
        """
        Função principal que roda o loop de eventos da interface.
        """
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == "Fechar":
                self.fechar_app()
                break
            elif event == "Remover da tabela":
                nome_tabela = values["nome_tabela"]
                nome_produto = values["nome_produto"]
                self.remover_do_estoque(nome_tabela, nome_produto)
            elif event == "Listar Estoque":
                nome_tabela = values["nome_tabela"]
                self.listar_estoque(nome_tabela)

def Relatorio():
    
    alimentos_nao_pereciveis= Est.listar_estoque("alimentos_nao_pereciveis")
    
    
    tabela_alimentos_nao_pereciveis = [
    ("iten", "Unidade", "Nome","Custo","Estoque","Data de validade")
    ]
    for x in alimentos_nao_pereciveis:
        iten,unidade,nome,custo,estoque,data_validade = x
        aux_iten=f"{iten}"
        aux_cust =f"{custo}"  
        aux_data_validade =f"{data_validade}".replace("-", "/")
        aux_esto= f"{estoque}"
        tabela_alimentos_nao_pereciveis.append((aux_iten,unidade,nome,aux_cust,aux_esto,aux_data_validade))


    carne= Est.listar_estoque("carne")
    
    
    tabela_carne = [
    ("iten", "Unidade", "Nome","Custo","Estoque","Data de validade")
    ]
    for x in carne:
        iten,unidade,nome,custo,estoque,data_validade = x
        aux_iten=f"{iten}"
        aux_cust =f"{custo}"  
        aux_data_validade= f"{data_validade}".replace("-", "/")
        aux_esto= f"{estoque}"
        tabela_carne.append((aux_iten,unidade,nome,aux_cust,aux_esto,aux_data_validade))
    
    hortifruti= Est.listar_estoque("hortifruti")
    

    tabela_hortifruti = [
    ("iten", "Unidade", "Nome","Custo","Estoque","Data de validade")
    ]
    for x in hortifruti:
        iten,unidade,nome,custo,estoque,data_validade = x  
        aux_iten=f"{iten}"
        aux_cust =f"{custo}"  
        aux_data_validade= f"{data_validade}".replace("-", "/")
        aux_esto= f"{estoque}"
        tabela_hortifruti.append((aux_iten,unidade,nome,aux_cust,aux_esto,aux_data_validade))


    descartaveis= Est.listar_estoque("descartaveis")
    
    tabela_descartaveis = [
    ("iten", "Unidade", "Nome","Custo","Estoque")
    ]
    for x in descartaveis:
        iten,unidade,nome,custo,estoque = x
        aux_iten=f"{iten}"
        aux_cust =f"{custo}"  
        aux_esto= f"{estoque}"
        tabela_descartaveis.append((aux_iten,unidade,nome,aux_cust,aux_esto))
    
    
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times','', size=16)
    pdf.cell(w=0, h=16, txt='UNIVERSIDADE ESTADUAL DA PARAÍBA', ln=True, align='C')
    pdf.cell(w=0, h=16, txt='CENTRO DE CIÊNCIAS BIOLÓGICAS E SOCIAIS APLICADAS', ln=True, align='C')

    pdf.set_font("Times", "B",size=14)
    pdf.cell(w=0, h=14, txt='1. Géneros alimentícios  não perecíveis', ln=True, align='L')
    pdf.set_font("Times","",size=10)
    with pdf.table() as table:
        for data_row in tabela_alimentos_nao_pereciveis:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.ln()

    pdf.set_font("Times", "B",size=14)
    pdf.cell(w=0, h=14, txt='1. Géneros alimentícios  carnes', ln=True, align='L')
    pdf.set_font("Times","",size=10)
    with pdf.table() as table:
        for data_row in tabela_carne:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    pdf.ln()

    pdf.set_font("Times", "B",size=14)
    pdf.cell(w=0, h=16, txt='1. Géneros alimentícios  Hortifruti', ln=True, align='L')
    pdf.set_font("Times","",size=10)
    with pdf.table() as table:
        for data_row in tabela_hortifruti:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    
    pdf.ln()

    pdf.set_font("Times", "B",size=14)
    pdf.cell(w=0, h=16, txt='1. Géneros alimentícios  descartaveis', ln=True, align='L')
    pdf.set_font("Times","",size=10)
    with pdf.table() as table:
        for data_row in tabela_descartaveis:
            row = table.row()
            for datum in data_row:
                row.cell(datum)



    pdf.ln()
    pdf.output('RELATORIO_ESTOQUE.pdf')


def main_interface():


    # Define o layout do menu
    layout_menu = [
        [sg.Text('MENU', font=('Helvetica', 16, 'bold'))],
        [sg.Button('Cadastrar Novo Alimento', size=(50, 0))],
        [sg.Button('Remover Alimento', size=(50, 0))],
        [sg.Button('Atualizar ao Estoque', size=(50, 0))],
        [sg.Button('Listar Alimentos', size=(50, 0))],
        [sg.Button('Pesquisar Estoque', size=(50, 0))],
        [sg.Button('Gerar PDF',key='gerar_pdf',size=(50,0))],
        [sg.Button('Sair', key='-SAIR-', size=(50, 0))]
    ]
    # Cria uma janela para o menu
    janela_menu = sg.Window('Gerenciador Estoque ', layout_menu, size=(500, 500), element_justification='center' )


    # Loop principal para a interface do menu
    while True:
        event, values = janela_menu.read()
        # Verifica se a janela foi fechada ou o botão 'Sair' foi pressionado
        if event == sg.WIN_CLOSED or event == '-SAIR-':
            break

        # Trata os eventos dos botões do menu
        elif event == 'Cadastrar Novo Alimento':
            app = Add_estoque_Interface(Est)
            app.executar()

        
        elif event == 'Atualizar ao Estoque':
            app = Updd_estoque_Interface(Est)
            app.executar()

        elif event == 'Remover Alimento':
            app = Rem_estoque_Interface(Est)
            app.executar()

        elif event == 'Listar Tabelas':
            app = Updd_estoque_Interface(Est)
            app.executar()

        elif event == 'Pesquisar Receitas/Despesas':
        # Chama a interface de pesquisa
            app = Updd_estoque_Interface(Est)
            app.executar()

        elif event == 'gerar_pdf':
            Relatorio()

    # Fecha a janela do menu ao sair do loop
    janela_menu.close()

if __name__ == "__main__":

    main_interface()

