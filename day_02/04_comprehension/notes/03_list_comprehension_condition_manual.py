tasks = {
    'register': 'high',
    'test': 'medium',
    'refactor': 'low',
}

priority_tasks = []
for task, prio in tasks.items():
    if prio != 'low':
        priority_tasks.append(task)

print(priority_tasks)
