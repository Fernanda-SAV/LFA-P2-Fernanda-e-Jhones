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
        edges = defaultdict(list)
        for symbol, next_states in moves.items():
            for next_state in next_states:
                edges[(state, next_state)].append(symbol)
        for (src, dest), symbols in edges.items():
            dot.edge(src, dest, label=",".join(symbols))

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

    
    all_symbols = set(
        symbol
        for state_transitions in afe_transitions.values()
        for symbol in state_transitions.keys()
        if symbol != "ε"
    )

    #monta o AFN
    for state, closure in closures.items():
        for symbol in all_symbols:
            reachable_states = set()
            for intermediate_state in closure:
                reachable_states.update(afe_transitions[intermediate_state].get(symbol, []))
            for reachable_state in reachable_states:
                afn_transitions[state][symbol].update(closures[reachable_state])

        #att estados finais
        if state in final_states:
            final_states.update(closure)
    
    return {state: dict(moves) for state, moves in afn_transitions.items()}, final_states

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
'''
afe_transitions ={
    "q0": {"a": ["q0"], "ε": ["q1"]},
    "q1": {"b": ["q1"], "ε": ["q2"]},
    "q2": {"a": ["q2"]}
}
start_state = "q0"
final_states = {"q2"}
'''

afe_transitions = {
      "q0": {"ε": ["q1", "q8", "q16"]},
      "q1": {"a": ["q2"]},
      "q2": {"ε": ["q3"]},
      "q3": {"a": ["q4"]},
      "q4": {"ε": ["q5"]},
      "q5": {"c": ["q6"]},
      "q6": {"ε": ["q7"]},
      "q8": {"a": ["q9"]},
      "q9": {"ε": ["q10"]},
      "q10": {"ε": ["q13", "q11"]},
      "q11": {"b": ["q12"]},
      "q12": {"ε": ["q13"]},
      "q13": {"ε": ["q14", "q10"]},
      "q14": {"c": ["q15"]},
      "q15": {"ε": ["q7"]},
      "q16": {"a": ["q17"]},
      "q17": {"ε": ["q18"]},
      "q18": {"ε": ["q19"]},
      "q19": {"b": ["q20"]},
      "q20": {"ε": ["q21"]},
      "q21": {"ε": ["q22", "q18"]},
      "q22": {"a": ["q23"]},
      "q23": {"ε": ["q7"]}
}
start_state = "q0"
final_states = {"q7"}

#visualiza o AFe
visualize_automaton(afe_transitions, start_state, final_states, "Automato AFe")

#converte p/ AFN
afn_transitions, afn_final_states = convert_afe_to_afn(afe_transitions, start_state, final_states)

#visualiza o AFN
visualize_automaton(afn_transitions, start_state, afn_final_states, "Automato AFN")
