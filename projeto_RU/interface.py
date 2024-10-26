import PySimpleGUI as sg

# Define o layout do menu
layout_menu = [
    [sg.Text('MENU', font=('Helvetica', 16, 'bold'))],
    [sg.Button('Cadastrar receitas/ Despesas', size=(50, 0))],
    [sg.Button('Remover receitas/ Despesas', size=(50, 0))],
    [sg.Button('Listar Receitas e Despesas', size=(50, 0))],
    [sg.Button('Pesquisar Receitas/Despesas', size=(50, 0))],
    [sg.Button('Gerar PDF',key='gerar_pdf',size=(50,0))],
    [sg.Button('Sair', key='-SAIR-', size=(50, 0))]
]
# Cria uma janela para o menu
janela_menu = sg.Window('Gerenciador financeiro', layout_menu, size=(500, 500), element_justification='center' )


# Loop principal para a interface do menu
while True:
    event, values = janela_menu.read()
    # Verifica se a janela foi fechada ou o botão 'Sair' foi pressionado
    if event == sg.WIN_CLOSED or event == '-SAIR-':
        break

    # Trata os eventos dos botões do menu
    elif event == 'Cadastrar receitas/ Despesas':
        interface_cadastro()

    elif event == 'Remover receitas/ Despesas':
        interface_remover()

    elif event == 'Listar Receitas e Despesas':
        # Obtém a lista de receitas e despesas
        x_receitas = listagem_receitas()
        x_despesas = listagem_despesas()
        # Cria uma tabela com os dados
        criar_tabela_dados(x_receitas, x_despesas)

    elif event == 'Pesquisar Receitas/Despesas':
        # Chama a interface de pesquisa
        interface_pesquisa()

    elif event == 'gerar_pdf':
        imprimir_pdf()

# Fecha a janela do menu ao sair do loop
janela_menu.close()