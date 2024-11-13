import PySimpleGUI as sg

sg.theme('Black')

def front():
    flayout = [
        [sg.Text('Bem Vindo')],                  # ROW 1
        [sg.Button("ENTRAR"), sg.Button("SAIR")] # ROW 2
    ] ## As janelas são implementadas por linhas
    
    window = sg.Window('Human Resources APP', flayout, size=(500, 100), element_justification='center') #Janela, título, layout, tamanho e justification da tela
    button, values = window.read() # Sempre que aperta um botão, é atribuido a button e sepre que algo é escrto, vai para values
    
    if button == 'ENTRAR':
        window.close()
    
    if button == 'SAIR':
        window.exit() # Fecha tudo e não guarda nada na memória
        
        
layout = [
    [sg.Text('Digite o nom do funcionário'), sg.InputText('', key='-NAME-')],# Input na mesma linha, text e input (texto, -key-)
    [sg.Button('Adicionar')],
    [sg.Text('')],
    [sg.Text('Funcionários cadastrados')],
    [sg.Listbox('NAME', size=(50, 10), key='-BOX-')],
    [sg.Button('Deletar'), sg.Button('Sair')]
]
front()

window = sg.Window('Main', layout)
button , values = window.read()
