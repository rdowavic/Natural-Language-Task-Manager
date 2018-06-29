"""
This file describes the structure of a Task object, ie how it has a from and till field,
a description, a priority, and things like this.
"""

class Task:
  def __init__(self):
    self.description = ""
    self.duration = None
    self.priority = None
  def description(self):
    return self.description
  def setDescription(self, text):
    # TODO: checkTextConforms()
    self.description = text
  def duration(self):
    print('Not yet implemented')
  def __str__(self):
    return f'8:00-10:00 {self.description}, {self.priority or "high"}'
  
  @classmethod
  def processTask(cls, text):
    """
    text is a string like "study" or "play fifa" or "do homework for tomorrow"
    """
    # In the most basic case, the whole string `s` is the description
    task = cls()
    task.setDescription(text)
    return task
  
   
