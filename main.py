import graphviz #Utilizado para visualizar o autômato.
import json #Para carregar o autômato a partir de um arquivo .json.
from collections import defaultdict #Um tipo de dicionário que inicializa automaticamente valores padrão.
import tkinter as tk #biblioteca para interface gráfica (tkinter é a biblioteca principal, messagebox e filedialog são módulos auxiliares).
from tkinter import messagebox, filedialog
import re #Biblioteca para expressões regulares (não está sendo usada no código, pode ser um resquício de código antigo).
from src.AFe_to_AFN import convert_afe_to_afn, visualize_automaton #Funções importadas de um módulo (src.AFe_to_AFN), que convertem autômatos e os visualizam.

#Carrega os dados do autômato a partir de um arquivo JSON.
def load_automaton_from_json(filepath):
    #Abre o arquivo JSON (filepath) em modo leitura ('r'), garantindo compatibilidade com caracteres especiais (utf-8).
    with open(filepath, 'r', encoding='utf-8') as file:
        #Usa json.load(file) para carregar o conteúdo do arquivo em um dicionário Python.
        data = json.load(file)
    #Retorna as transições do autômato, o estado inicial e os estados finais (convertidos em um set).
    return data['transitions'], data['start_state'], set(data['final_states'])

#Abre uma janela para seleção de arquivos JSON e executa a conversão do AFe para AFN.
def select_file():
    #Abre uma caixa de diálogo para o usuário selecionar um arquivo .json
    filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    #Verifica se um arquivo foi selecionado.
    if filepath:
        #Carrega o autômato do arquivo JSON.
        afe_transitions, start_state, final_states = load_automaton_from_json(filepath)
        
        #Exibe no console as transições do AFe, o estado inicial e os estados finais.
        print("Transições do AFe:")
        print(afe_transitions)
        print("\nEstado Inicial:", start_state)
        print("\nEstados Finais:", final_states)
        
        #Gera e exibe um gráfico do AFe.
        visualize_automaton(afe_transitions, start_state, final_states, f"Automato - AFe")
        
        #Converte o AFe para AFN chamando convert_afe_to_afn().
        afn_transitions, afn_final_states = convert_afe_to_afn(afe_transitions, start_state, final_states)
        
        #Exibe no console as transições do AFN e seus estados finais.
        print("\nTransições do AFN:")
        print(afn_transitions)
        print("\nEstados Finais do AFN:", afn_final_states)

        #Gera e exibe um gráfico do AFN.
        visualize_automaton(afn_transitions, start_state, afn_final_states, f"Automato - AFN")

    
#Cria a interface gráfica para o conversor de AFe para AFN.
def main():
    #Cria a janela principal (Tk()) e define o título.
    root = tk.Tk()
    root.title("Conversor de AFe para AFN")

    #Cria um frame dentro da janela principal, com espaçamento interno e externo de 10 pixels.
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    #Adiciona um rótulo (Label) com a instrução para selecionar um arquivo JSON.
    label = tk.Label(frame, text="Selecionar arquivo JSON com o AFe")
    label.pack(pady=5)

    #Adiciona um botão que, quando clicado, chama select_file().
    button = tk.Button(frame, text="Selecionar arquivo", command=select_file)
    button.pack(pady=5)

    #Mantém a janela aberta aguardando interação do usuário.
    root.mainloop()

#Verifica se o script está sendo executado diretamente (__name__ == "__main__").
#Se for, chama main() para iniciar a interface gráfica.
if __name__ == "__main__":
    main()