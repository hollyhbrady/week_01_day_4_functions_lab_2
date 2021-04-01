import pdb

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]



# MVP

# As a user, to manage my task list I would like a program that allows me to:
# Print a list of uncompleted tasks
def check_to_do_list(list, completed):
    # pdb.set_trace()
    found_tasks = []
    
    for task in list:
        if (task["completed"] == completed):
            found_tasks.append(task["description"])
    return found_tasks

print(check_to_do_list(tasks, False))

# Print a list of completed tasks

def check_to_do_list(list, completed):
    # pdb.set_trace()
    found_tasks = []
    
    for task in list:
        if (task["completed"] == completed):
            found_tasks.append(task["description"])
    return found_tasks

print(check_to_do_list(tasks, True))
# Print a list of all task descriptions

def print_task_descriptions(list):
    descriptions =[]
    for task in tasks:
        descriptions.append(task["description"])
    return descriptions

print(print_task_descriptions(tasks))

# Print a list of tasks where time_taken is at least a given time

def print_task_with_x_time(list, time):
    found_task = []

    for task in tasks:
        if task["time_taken"] <= time:
            found_task.append(task["description"])
    return found_task

print(print_task_with_x_time(tasks, 15))

# Print any task with a given description 

def print_task_with_x_description(list, description):
    found_task = []

    for task in tasks:
        if task["description"] == description:
            found_task.append(task)
    return found_task

print(print_task_with_x_description(tasks, "Feed Cat"))

# Extension

# Given a description update that task to mark it as complete.

def set_task_as_complete(list, updated_task):

    for task in tasks:
        if task["description"] == updated_task:
            task["completed"] = True
    return f'{updated_task} has been completed'

print(set_task_as_complete(tasks, "Feed Cat")) 

# Add a task to the list

#append tasks list with new dictionary
#create new task dictionary
#add new task dictionary to list of tasks 

def add_task_to_list(list, new_task):
    new_task = {"description": new_task, "completed": False, "time_taken": "One does not simply 'complete' Warzone"}
    
    tasks.append(new_task)
    return tasks 

add_task_to_list(tasks, "Warzone")

print(tasks[5])

# Further Extensions

# Use a while loop to display the following menu and allow the use to enter an option.

