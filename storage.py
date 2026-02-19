import json
from task import Task

#Listen speichern und laden
class Storage:
    def __init__(self, filename="todolist.json"):
        self.filename = filename

    #Speichern
    def save(self, lists):
        data = {}
        for list_name, tasks in lists.items():
            data[list_name] = [{"title": t.title, "completed": t.completed} for t in tasks]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Liste in '{self.filename}' gespeichert.")

    #Laden
    def load(self):
        try:
            with open(self.filename, "r") as f:
                content = f.read().strip()  # Inhalt lesen und whitespace trimmen
                if not content:             # falls leer
                    return {}
                data = json.load(f)
                return {name: [Task(t["title"], t["completed"]) for t in tasks] for name, tasks in data.items()}
        except FileNotFoundError:
            print(f"Keine Datei mit Namen '{self.filename}' gefunden. Starte mit leerer Liste.")
            return{}