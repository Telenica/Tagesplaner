import sys
import os

from storage import Storage
from planner import Planner

def main():
    planner = Planner()

    #Liste wählen oder erstellen
    print("Welche Liste möchtest du beartbeiten?")
    list_name = input("Liste: ")
    planner.select_list(list_name)

    #Wählen was zu tun ist
    while True:
        print("\n1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als fertig markieren")
        print("4. Aufgabe als unfertig markieren")
        print("5. Aufgabe löschen")
        print("6. Alle Aufgaben löschen")
        print("7. Beenden")

        #Was gewählte Option tut
        choice = input("Wähle was tun tun möchtest: ")

        if choice == "1":
            title = input ("Name der Aufgabe: ")
            planner.add_task(title)

        elif choice == "2":
            tasks = planner.get_tasks()
            for i, task in enumerate(tasks):
                status = "erledigt" if task.completed else "unerledigt"
                print(f"{i}. {task.title} [{status}]")
        
        elif choice == "3":
            index = int(input("Index der Aufgabe: "))
            planner.complete_task(index)
        
        elif choice == "4":
            index = int(input("Index der Aufgabe: "))
            planner.uncomplete_task(index)

        elif choice == "5":
            index = int(input("Index der Aufgabe: "))
            planner.delete_task(index)
        
        elif choice == "6":
            planner.delete_all()
        
        elif choice == "7":
            break

if __name__ == "__main__":
    main()