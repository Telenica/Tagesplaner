import sys

def print_start():
    print("Hallo. Was möchtest du heute tun?")
    print("1 Aufgabe hinzufügen\n2 Aufgabe entfernen\n3 To-Do-Liste ansehen\n4 Exit")

def selection():
    auswahl = ""
    while auswahl == "":
        print_start
        try:
            auswal = int (input("\nWas wollen sie tun?\n"))
        except:
            print ("Das ist keine Ganzzahl!")
            continue
        if auswahl < 1 or auswahl > 3:
            print("Keine der vorhandener Menüpunkt")
            auswahl = ""
        else:
            return auswahl

auswahl = selection()
todolist = {}

if auswahl == 1:
    name = input("Name der Aufgabe: ")

    todolist[name] = input("Aufgabenbeschreibung: ")
    selection()

if auswahl == 2:
    print("Dieser Menüpunkt ist noch nciht ausgebaut.")
    selection()

if auswahl == 3:
    print(todolist)
    selection()

if auswahl == 4:
    sys.exit(1)