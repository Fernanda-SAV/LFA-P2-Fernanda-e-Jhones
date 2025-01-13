import graphviz
from collections import defaultdict

def visualize_automaton(transitions, start_state, final_states, title):
    #ver os autômatos:
    dot = graphviz.Digraph(format="png", engine="dot")
    dot.attr(rankdir="LR")

    #add estados
    for state in transitions:
        if state in final_states:
            dot.node(state, shape="doublecircle")
        else:
            dot.node(state)

    #add qo
    dot.node("start", shape="none")
    dot.edge("start", start_state)

    #add transições
    for state, moves in transitions.items():
        for symbol, next_states in moves.items():
            for next_state in next_states:
                dot.edge(state, next_state, label=symbol)

    dot.attr(label=title, fontsize="16")
    dot.render(f"{title.replace(' ', '_')}", cleanup=True, view=True)


def e_closure(state, transitions):
    
    #calcula o fecho-ε p/ um dado estado
    
    stack = [state]
    closure = set(stack)

    while stack:
        current_state = stack.pop()
        for next_state in transitions[current_state].get("ε", []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return closure


def convert_afe_to_afn(afe_transitions, start_state, final_states):
    
    afn_transitions = defaultdict(lambda: defaultdict(set))

    #calcula o fecho-ε p/ cada estado
    closures = {state: e_closure(state, afe_transitions) for state in afe_transitions}

    #monta o AFN
    for state in afe_transitions:
        for symbol, next_states in afe_transitions[state].items():
            if symbol == "ε":
                continue
            for next_state in next_states:
                for closure_state in closures[next_state]:
                    afn_transitions[state][symbol].add(closure_state)
        
        if state in final_states:
            for closure_state in closures[state]:
                final_states.add(closure_state)
        #for closure_state in closures[state]:
         #   if closure_state in final_states:
          #      final_states.add(state)
    
    #return {state: dict((k, list(v)) for k, v in moves.items()) for state, moves in afn_transitions.items()}, final_states
    return {state: dict(moves) for state, moves in afn_transitions.items()}, final_states
         

'''
        #add transições do fecho-ε p/ os estados finais
        if state in final_states:
            for closure_state in closures[state]:
                final_states.add(closure_state)
'''
    #return {state: dict(moves) for state, moves in afn_transitions.items()}, final_states
   
#entrada do AFe
'''
afe_transitions = {
    "q0": {"ε": ["q1", "q2"]},
    "q1": {"a": ["q1", "q3"]},
    "q2": {"b": ["q2"]},
    "q3": {"ε": ["q4"]},
    "q4": {"c": ["q4"]}
}
start_state = "q0"
final_states = {"q4"}
'''

afe_transitions ={
    "q0": {"a": ["q0"], "ε": ["q1"]},
    "q1": {"b": ["q1"], "ε": ["q2"]},
    "q2": {"a": ["q2"]}
}
start_state = "q0"
final_states = {"q2"}


#visualiza o AFe
visualize_automaton(afe_transitions, start_state, final_states, "Automato AFe")

#converte para AFN
afn_transitions, afn_final_states = convert_afe_to_afn(afe_transitions, start_state, final_states)

#visualiza o AFN
visualize_automaton(afn_transitions, start_state, afn_final_states, "Automato AFN")
