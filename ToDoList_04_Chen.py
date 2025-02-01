# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:29:15 2025

@author: sharr
"""

# Creates a list so you can hold the tasks in the to do list
task_list = ["Do 2140 homework", "Study of for physics class"]

#==============================================================================================

# Allows the user to view the lsit 
def user_view():
    for i in range(len(task_list)): 
        #Prints the list with using a for loop to print the task number in the list
        print ("Task", i+1, "is", task_list[1])
        
#==============================================================================================
def add_list():
    #Asks the user for a task to add to their list
    add_list=input ("What task do you want to add?")
    #Adds what they want to the list
    task_list.append(add_list)
    
    #Printing the new list of tasks 
    print ("Your new list of task are: ")
    for i in range(len(task_list)):
        print("Task", i+1, "is", task_list[i])

#==============================================================================================
def delete_list():
    #Prints the current task to the user, allowing them to remove the task that they want
    print ("This is the list of tasks")
    for i in range(len(task_list)):
        print("Task", i+1, "is", task_list[i])
        
    #Deltes the task from the list
    delete_taask = eval(input("Which task would you like to delete from the list? 1-3"))
    list_value = delete_task = 1
    task_list.pop(list_value)
    
    #Prints the new list of task after the removal 
    print("Your new list of tasks are: ")
    for i in range(len(task_list)):
        print("Task", i+1, "is", task_list[i])

#==============================================================================================
def main():
    #If the users input is yes in the while loop 
    end_repeat = "y"
    while end_repeat == "y":
        #Asks the user if they want to look at their tasks
        user_ask = input("Do you wnat to look at the list of tasks? (y/n): ")
        if user_ask == "y":
            user_view()
        else: 
            #Asks the user if they want to add another task
            user_add = input("Do you want to add new tasks? (y/n): ")
            if user_add == "y":
                add_list()
            else:
                #Asks the user if they want to delete another task
                user_delete = input("Do you want to delete one of your tasks? (y/n): ")
                if user_delete == "y":
                    delete_list()
    end_repeat = input("Do you want to continue? (y/n): ")
    
#==============================================================================================
main()