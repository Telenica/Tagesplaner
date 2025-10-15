import sys

def print_start():
    print("Hallo. Was möchtest du tun?")
    print("1 Aufgabe hinzufügen\n2 Aufgabe entfernen\n3 To-Do-Liste ansehen\n4 Exit")

def selection():
    auswahl = ""
    while auswahl == "":
        print_start()
        try:
            auswahl = int (input("\nWas wollen sie tun?\n"))
        except:
            print ("Das ist keine Ganzzahl!")
            continue
        if auswahl < 1 or auswahl > 4:
            print("Keine der vorhandener Menüpunkt")
            auswahl = ""
        else:
            return auswahl

auswahl = selection()
todolist = []

if auswahl == 1:
    name = input("Name der Aufgabe: ")
    todolist.append(name)

    selection()

if auswahl == 2:
    name = input("Was möchtest du löschen?")
    todolist.remove(name)
    
    selection()

if auswahl == 3:
    print(todolist)
    
    selection()

if auswahl == 4:
    sys.exit(1)