import graphviz
import json
from collections import defaultdict
import tkinter as tk
from tkinter import messagebox, filedialog
import re
from src.AFe_to_AFN import convert_afe_to_afn, visualize_automaton

def load_automaton_from_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['transitions'], data['start_state'], set(data['final_states'])

def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if filepath:
        afe_transitions, start_state, final_states = load_automaton_from_json(filepath)
        visualize_automaton(afe_transitions, start_state, final_states, f"Automato - AFe")
        afn_transitions, afn_final_states = convert_afe_to_afn(afe_transitions, start_state, final_states)
        visualize_automaton(afn_transitions, start_state, afn_final_states, f"Automato - AFN")

def main():
    root = tk.Tk()
    root.title("Conversor de AFe para AFN")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Selecionar arquivo JSON com o AFe")
    label.pack(pady=5)

    button = tk.Button(frame, text="Selecionar arquivo", command=select_file)
    button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()