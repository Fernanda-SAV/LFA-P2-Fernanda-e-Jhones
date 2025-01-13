from Class_Draw_Automata import Draw
from Func_NFA_Ɛ_TO_NFA import nfa_Ɛ_to_nfa
import os
import time

if __name__ == '__main__':
    exit = False

    while True != exit:
        print("\n\n\n\n")
        print("----------------Awesome Automata-------------------\n")
        print("       *----------Enter_Option-----------*")
        print("1.Draw your Automata")
        print("2.RE->NFA_Ɛ->NFA->DFA")
        print("3.RE->NFA_Ɛ")
        print("4.NAFA_Ɛ->NFA")
        print("5.NFA->DFA")
        print("6.Test_DFA")
        print("7.Exit/Quit")

        x = int(input())

        if x == 1:
            states: input("Enter states: ")
            simbols: input("Enter Simbols: ")
            final_states: input("Enter Final_state: ")
            Inicial_state: input("Enter Initial_State: ")

            paint1 = Draw(states, simbols, final_states, Inicial_state)

        elif x == 4:
            json_name = input("Enter the json File Name from the test_automata_folder: ")
            nfa_Ɛ_to_nfa("images/" + json_name + ".json")
            print("--Conversion complete--")

        elif x == 7:
            print("Good Bye")
            exit = True
