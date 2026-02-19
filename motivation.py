import random

class Motivation:
    def __init__(self):
        self.list = ["Du schaffst das", "Weiter so!", 
                     "Denk daran: kleine Schritte sind besser als keine Schritte", 
                     "Das Geheimnis des Erfolgs ist anzufangen", 
                     "Ehrgeiz ist die Fähigkeit, die Träume real werden lässt", 
                     "Scheitern ist nicht das Gegenteil von Erfolg. Es ist ein Teil davon",
                     "Tue genau das, was dich auf deinem Weg weiter bringt",
                     "Mach es, bevor du bereust, es nicht getan zu haben",
                     "Wer nicht kämpft, hat schon verloren"]

    def get_random(self):
        zufallselement = random.choice(self.list)
        print (zufallselement)