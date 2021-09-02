tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]



def incompleted_tasks( list ):
    incompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            incompleted_tasks.append(task)
    return incompleted_tasks

print(incompleted_tasks(tasks))

def completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

print(completed_tasks(tasks)) 


def task_descriptions(list):
    describe_task = []
    for task in list:
        describe_task.append(task["description"])
    return describe_task

print(task_descriptions(tasks))   

def at_least_given_time(list, time_taken):
    given_time = []
    for task in list:
        if task["time_taken"] > time_taken:
            given_time.append(task)

    return given_time

print(at_least_given_time(tasks, 10))

        

               

def given_description(list, description):
    describe_task = []
    for task in list:
        if task["description"] == description:
            describe_task.append(task)

    return describe_task  

print(given_description(tasks, "Wash Dishes"))  

  


        
          

    
 










    


        
