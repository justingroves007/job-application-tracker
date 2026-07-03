"""
Justin Groves
7/3/26
"""

class Job_application_tracker:
  def __init__(self):
    self.app_list = []

  def add_app(self, application):
    self.app_list.append(application)

  def view_app(self):
    print(self.app_list)
