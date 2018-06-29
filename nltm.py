from task import Task
"""
Accept user commands on a loop
If what they type is not any predefined command, assume it is a task
Predefined commands are:
view [DATE]
history [from DATE]
quit
help
"""
taskStore = set()

if __name__ == '__main__':
  while True:
    cmd = input().lower()

    if cmd == 'help':
      print('OPTIONS: quit | history [from DATE] | view [DATE] | help | type any task')
    elif cmd == 'quit':
      quit()
    else:
      try:
        first, *rest = cmd.split()
        if first == 'view':
          for task in taskStore:
            print(task)
        elif first == 'history':
          print('Not yet implemented')
        else:
          taskStore |= {Task.processTask(cmd)}
      except ValueError:
        continue 
