import graphviz #Biblioteca para gerar visualizações gráficas de autômatos.
from collections import defaultdict #Estrutura de dicionário que inicializa automaticamente valores padrão, útil para evitar KeyError.


#Função para visualizar um autômato finito a partir das transições, estado inicial e estados finais.
def visualize_automaton(transitions, start_state, final_states, title):
    #ver os autômatos:
    dot = graphviz.Digraph(format="png", engine="dot") #Cria um objeto Digraph do graphviz para gerar o grafo em formato PNG.
    dot.attr(rankdir="LR") #Define a direção do grafo da esquerda para a direita

    #Adiciona os estados ao grafo.
    for state in transitions:
        #Se um estado estiver na lista de estados finais, ele recebe a forma de "doublecircle" (indica estado final).
        if state in final_states:
            dot.node(state, shape="doublecircle") 
        else:
            dot.node(state) #Estados comuns são representados normalmente.

    #add qo
    dot.node("start", shape="none") #Cria um nó fictício "start" sem forma (shape="none") para indicar visualmente o estado inicial.
    dot.edge("start", start_state) #Conecta "start" ao start_state com uma aresta.

    #adiciona transições
    #Percorre as transições do autômato.
    for state, moves in transitions.items():
        edges = defaultdict(list) #Usa defaultdict(list) para armazenar transições organizadas por estado origem → destino.
        for symbol, next_states in moves.items(): #Agrupa os símbolos que levam de um estado a outro.
            for next_state in next_states:
                edges[(state, next_state)].append(symbol)
        for (src, dest), symbols in edges.items(): #Para cada transição src -> dest, cria uma aresta com um rótulo contendo os símbolos separados por vírgula.
            dot.edge(src, dest, label=",".join(symbols))
    
    #Define o título do grafo.
    dot.attr(label=title, fontsize="16")
    #Renderiza e exibe o grafo, nomeando o arquivo com base no título.
    dot.render(f"{title.replace(' ', '_')}", cleanup=True, view=True)

#Calcula o fecho-ε (ε-closure) de um estado, ou seja, todos os estados acessíveis apenas por transições vazias (ε).
def e_closure(state, transitions):
    
    #Inicializa uma pilha (stack) e um conjunto (closure) com o estado inicial
    stack = [state]
    closure = set(stack)

    #Enquanto houver estados na pilha, remove o topo (pop()).
    while stack:
        current_state = stack.pop()
        #Para cada estado acessível via transição ε, adiciona ao conjunto closure se ainda não estiver lá.
        #O novo estado é colocado na pilha para continuar a busca recursiva.
        for next_state in transitions[current_state].get("ε", []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    #Retorna o fecho-ε do estado inicial.
    return closure

#Converte um Autômato Finito com ε-transições (AFE) em um Autômato Finito Não Determinístico (AFN).
def convert_afe_to_afn(afe_transitions, start_state, final_states):
    
    #Inicializa a estrutura de transições do AFN, onde cada estado tem um dicionário de símbolos mapeando para conjuntos de estados alcançáveis.
    afn_transitions = defaultdict(lambda: defaultdict(set))

    #calcula o fecho-ε para cada estado no autômato e armazena no dicionário closures.
    closures = {state: e_closure(state, afe_transitions) for state in afe_transitions}

    #Coleta todos os símbolos usados no autômato, excluindo ε.
    all_symbols = set(
        symbol
        for state_transitions in afe_transitions.values()
        for symbol in state_transitions.keys()
        if symbol != "ε"
    )

    #monta o AFN
    #Para cada estado e seu fecho-ε, inicia a análise das transições para cada símbolo.
    for state, closure in closures.items():
        for symbol in all_symbols:
            reachable_states = set()
            #Percorre os estados no fecho-ε e verifica para onde podem ir com determinado símbolo.
            for intermediate_state in closure:
                reachable_states.update(afe_transitions[intermediate_state].get(symbol, []))
            #Para cada estado acessível diretamente, adiciona ao novo autômato o conjunto de estados acessíveis via fecho-ε.
            for reachable_state in reachable_states:
                afn_transitions[state][symbol].update(closures[reachable_state])

        #Se qualquer estado no fecho-ε for um estado final, o estado original também deve ser tratado como final.
        #atualiza os estados finais
        if closure.intersection(final_states):  
            final_states.update(closure)
    #Retorna as transições do AFN e a lista de estados finais atualizada.
    return {state: dict(moves) for state, moves in afn_transitions.items()}, final_states
