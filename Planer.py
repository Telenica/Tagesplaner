import sys
import os

#todolist = []

dateiname = "List.txt"

if os.path.exists(dateiname):
    with open(dateiname, "r", encoding="utf-8") as f:
        todolist = [zeile.strip() for zeile in f]
        print("Liste geladen:", todolist)
else:
    todolist = []
    print("Keine Datei gefunden. Starte mit leerer Liste.")

def print_start():
    print("\nHallo. Was möchtest du tun?")
    print("1 Liste hinzufügen")
    print("2 Aufgabe hinzufügen")
    print("3 Aufgabe entfernen")
    print("4 To-Do-Liste ansehen")
    print("5 Exit")

def selection():
    while True:
        print_start()
        try:
            auswahl = int(input("\nWas wollen Sie tun? "))
            if 1 <= auswahl <= 5:
                return auswahl
            else:
                print("Keine gültige Auswahl. Bitte 1 bis 5 eingeben.")
        except ValueError:
            print("Das ist keine Ganzzahl!")

while True:
    auswahl = selection()

    if auswahl == 1:
        filename = input("Name der Liste: ")
        todolist.append(filename)
        print(f"Liste '{name}' wurde hinzugefügt.")

    elif auswahl == 2:
        name = input("Name der Aufgabe: ")
        todolist.append(name)
        print(f"Aufgabe '{name}' wurde hinzugefügt.")

    elif auswahl == 3:
        name = input("Welche Aufgabe möchtest du löschen? ").strip().lower()
        if name == "alles":
            todolist.clear()
            print(f"Alle Aufgaben die in der To-Do-Liste enthalten waren, wurden gelöscht")
        elif name in todolist:
            todolist.remove(name)
            print(f"Aufgabe '{name}' wurde entfernt.")
        else:
            print(f"'{name}' ist nicht in der Liste.")

    elif auswahl == 4:
        if not todolist:
            print("Die To-Do-Liste ist leer.")
        else:
            print("To-Do-Liste:")
            for i, item in enumerate(todolist, 1):
                print(f"{i}. {item}")

    elif auswahl == 5:
        print("Liste Speichern")
        f = open("List.txt","a",encoding="utf-8")
        for i in todolist:
            f.write(i + "\n")
        f.close()
        print("Programm wird beendet.")
        sys.exit(0)