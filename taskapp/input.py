#! /usr/bin/env python
"""
Generate sample task data
"""
import json

def generate_input(num_of_tasks=1):
    """
    Create tasks for test cases.
    """
    task_list = []
    for i in range(num_of_tasks):
        task_list.append({"id": i, "name": "task num_{}".format(i)})

    with open('input.txt', 'w') as f:
        json.dump(task_list, f)
        
if __name__ == '__main__':
    generate_input(num_of_tasks=10)
        
