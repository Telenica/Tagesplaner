from task import Task
from storage import Storage

#Aufgaben verwalten
class Planner:
    def __init__(self, filename="todolist.json"):
        self.storage = Storage(filename)
        self.lists = self.storage.load()
        self.current_list = None

    #Zu verwendende Liste auswählen
    def select_list(self, list_name):
        if list_name not in self.lists:
            self.lists[list_name] = []
        self.current_list = list_name

    #Aufgabe hinzufügen und benennen
    def add_task(self, title):
        if self.current_list is None:
            raise ValueError("Keine Liste ausgewählt")
        task = Task(title)
        self.lists[self.current_list].append(task)
        self.storage.save(self.lists)
    
    #Aufgaben wiedergeben
    def get_tasks(self):
        if self.current_list is None:
            raise ValueError("Keine Liste ausgewählt")
        return self.lists[self.current_list]
    
    #Aufgabe als fertig markieren
    def complete_task(self, index):
        task = self.get_tasks()
        task[index].mark_completed()
        self.storage.save(self.lists)

    #Aufgabe als nicht fertig markieren
    def uncomplete_task(self, index):
        task = self.get_tasks()
        task[index].mark_uncompleted()
        self.storage.save(self.lists)
    
    #Aufgabe löschen
    def delete_task(self, index):
        task = self.get_tasks()
        del task[index]
        self.storage.save(self.lists)
    
    #Alle Aufgaben löschen
    def delete_all(self):
        task = self.get_tasks()
        for t in task:
            del t
        self.storage.save(self.lists)