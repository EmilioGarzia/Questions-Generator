# Questions Generator
# 
# @usage python question_generator.py -q CSV\path\file_name.CSV
# @author Emilio Garzia

import random as r
import os
from pandas import read_csv, DataFrame
from rich import print
from rich import console
import argparse as ap
import sys

# check the OS to define a command for clear screen
OS = os.name
clear_command = "cls" if OS=="nt" else "clear"

# Define argparser
parser = ap.ArgumentParser()
parser.add_argument("-q", "--questions", default="data.csv" ,help="Define CSV file that contains the questions, default='data.csv'")
parser.add_argument("-d", "--difficulty", default=-1, help="Specify the difficulty of the questions, default=-1", type=int)
parser.add_argument("-r", "--no_repeat", action="store_true", help="Questions are shown only once")
args = vars(parser.parse_args())

difficulty = args["difficulty"]

# Refresh screen when answer is showed
def refresh_console(question, answer=None, hint=None):
       os.system(clear_command)
       print("[bold yellow]Question Generator developed by Emilio Garzia")
       print("[bold red]Q: [italic white]" + question)

       if answer:
              if hint != None: print("[bold blue]H: [italic white]" + hint)
              print("[bold green]A: [italic white]" + answer)
       elif hint:
              print("[bold blue]H: [italic white]" + hint)

# Show the answer
def show_answer(questions, hint=None):
       # check if the answer is available in CSV file
       if(questions["answer"][choice] == ''):
              questions["answer"][choice] = "[bold blue]WARNING: No answer in CSV file for this question!"

       refresh_console(question=questions["question"][choice], answer=questions["answer"][choice], hint=hint)

# Show the Hint
def show_hint(questions):
       # check if the hint is available in CSV file
       if(questions["hint"][choice] == ''):
              questions["hint"][choice] = "[bold blue]WARNING: No hint in CSV file for this question!"

       refresh_console(question=questions["question"][choice], hint=questions["hint"][choice])

# init the questions by the difficulty
def init_questions(questions):
       q = DataFrame(columns=["question", "answer", "hint", "difficulty"])

       for i in range(len(questions)):
              if questions["difficulty"][i] == difficulty:
                     q = q._append({
                            "question": questions["question"][i],
                            "answer": questions["answer"][i],
                            "hint": questions["hint"][i],
                            "difficulty": questions["difficulty"][i]
                     }, ignore_index=True)
       return q

def pop_from_dict(dict, index):
       for element in dict:
              if index in dict[element]:
                     del dict[element][index]
                     

# driver code
if __name__ == "__main__":
       questions = read_csv(args["questions"]).to_dict()
       #questions = init_questions(questions)
       #n_tuple = questions.shape[0]

       pop_from_dict(questions, 0)
       print(questions)

       """# Print questions (and answers)
       option = ""
       while option != "q":
              # Clear the screen and print logo
              os.system(clear_command)
              print("[bold yellow]Question Generator developed by Emilio Garzia")

              choice = r.randint(a=0, b=n_tuple-1)

              if args["no_repeat"]:
                     questions = questions.drop(choice)
                     n_tuple = n_tuple-1

              try:
                     # print question
                     print("[bold red]Q: [italic white]" + questions["question"][choice])
                     option = console.Console().input("Press 'ENTER' for next question or 'a' to show answer (press 'q' to exit) [bold yellow]-> ")
                     
                     # Print answer if request
                     if(option == 'a'):
                            show_answer(questions=questions)
                            option = console.Console().input("Press 'ENTER' for next question (press [bold]'q' to exit) [bold yellow]-> ")
                     # Print hint if request
                     elif(option == 'h'):
                            show_hint(questions=questions)
                            option = console.Console().input("Press 'ENTER' for next question or 'a' to show answer (press [bold]'q' to exit) [bold yellow]-> ")
                            if(option == 'a'):
                                   show_answer(questions=questions, hint=questions["hint"][choice])
                                   option = console.Console().input("Press 'ENTER' for next question (press [bold]'q' to exit) [bold yellow]-> ")
              except:
                     print("Ciao")"""
       