from collections import defaultdict, deque

def task_manager(tasks):
    
    tasks_dict = defaultdict(deque)

    for _task, server_name, priority in tasks:
        if priority == False:
            tasks_dict[server_name].append(_task)
        else:
            tasks_dict[server_name].appendleft(_task)
            
    return tasks_dict


tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
print(task_manager(tasks))