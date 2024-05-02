# Questions Generator
# 
# @usage python question_generator.py -q json\path\file_name.json
# @author Emilio Garzia

import random as r
import os
import sys
import json
from rich import print
from rich import console
import argparse as ap

# Refresh screen when answer is showed
def refresh_for_answer(question, answer):
       os.system(clear_command)
       print("[bold yellow]Question Generator developed by Emilio Garzia")
       print("[bold red]Q: [italic white]" + question)
       print("[bold green]A: [italic white]" + answer)

# check the OS to define a command for clear screen
OS = os.name
clear_command = "cls" if OS=="nt" else "clear"

# Define argparser
parser = ap.ArgumentParser()
parser.add_argument("-q", "--questions", default="questions.json" ,help="Define JSON file that contains the questions, default='questions.json'")
args = vars(parser.parse_args())

# Read questions and answers from a JSON file
try:
       with open(args["questions"], encoding="utf-8") as json_file:
              questions = json.load(json_file)
except FileNotFoundError as file_not_found:
       print(file_not_found)
       sys.exit(0)

# Print questions (and answers)
option = ""
while option != "q":
       # Clear the screen and print logo
       os.system(clear_command)
       print("[bold yellow]Question Generator developed by Emilio Garzia")

       # Get a random question
       question = (r.choices(list(questions)))[0]
       answer = questions[question]
              
       # print question
       print("[bold red]Q: [italic white]" + question)
       option = console.Console().input("Press 'ENTER' for next question or 'a' to show answer (press 'q' to exit) [bold yellow]-> ")
       
       # Print answer if request
       if(option == 'a'):
              # check if the answer is available in JSON file
              if(answer == ''):
                     answer = "[bold blue]WARNING: No answer in JSON file for this question!"

              refresh_for_answer(question, answer)
              option = console.Console().input("Press 'ENTER' for next question (press [bold]'q' to exit) [bold yellow]-> ")