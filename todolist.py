# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:54:09 2021

@author: jesss
"""

a = "yes"
to_do = []
number = 0


def add_tasks():  # adds tasks
    print("Type \"end\" to return to menu")
    while 1 == 1:
        task = input("New task: ")
        if task == "end":
            break
        else:
            to_do.append(task)


def print_list(): # prints your to do list
    print("~~~To Do list~~~")
    print(*to_do, sep = "\n")


while 1 == 1:
    print("-----------------------")
    print("What do you want to do?")
    print("1. Add a task")
    print("2. View list")
    print("3. Exit")
    
    try:
        number = int(input("Number: "))
        
        if number == 1:
            add_tasks()
        elif number == 2:
            print_list()
        elif number == 3:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid number (1, 2 or 3)")
    except ValueError:
        print("Please enter a number (1, 2 or 3)")