#Aufgabe erstellen und als fertig oder nicht fertig markieren
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
    
    #Aufgabe fertig
    def mark_completed(self):
        self.completed = True

    #Aufgabe nicht fertig
    def mark_uncompleted(self):
        self.completed = False