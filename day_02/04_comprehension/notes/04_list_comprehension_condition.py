tasks = {
    'register': 'high',
    'test': 'medium',
    'refactor': 'low',
}

priority_tasks = [task for task, prio in tasks.items() if prio != 'low']
