import json
import os
import tkinter as tk
from tkinter import filedialog
from src.AFe_to_AFN import convert_afe_to_afn, visualize_automaton

def load_automaton_from_json(filepath):
    """
    Load automaton data from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        tuple: Transitions, start state, and final states of the automaton.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data['transitions'], data['start_state'], set(data['final_states'])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")
        return None, None, None

def select_file():
    """
    Open a file dialog to select a JSON file and process the automaton data.
    """
    filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if filepath:
        afe_transitions, start_state, final_states = load_automaton_from_json(filepath)
        if afe_transitions is None:
            return

        print("Transições do AFe:")
        print(afe_transitions)
        print("\nEstado Inicial:", start_state)
        print("\nEstados Finais:", final_states)
        
        image_folder = "generated_images"
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        
        visualize_automaton(afe_transitions, start_state, final_states, os.path.join(image_folder, "Automato_AFe.png"))
        
        afn_transitions, afn_final_states = convert_afe_to_afn(afe_transitions, start_state, final_states)
        
        print("\nTransições do AFN:")
        print(afn_transitions)
        print("\nEstados Finais do AFN:", afn_final_states)

        visualize_automaton(afn_transitions, start_state, afn_final_states, os.path.join(image_folder, "Automato_AFN.png"))

def create_gui():
    """
    Create the GUI for the application.
    """
    root = tk.Tk()
    root.title("Conversor de AFe para AFN")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Selecionar arquivo JSON com o AFe")
    label.pack(pady=5)

    button = tk.Button(frame, text="Selecionar arquivo", command=select_file)
    button.pack(pady=5)

    root.mainloop()

def main():
    """
    Main function to run the application.
    """
    create_gui()

if __name__ == "__main__":
    main()