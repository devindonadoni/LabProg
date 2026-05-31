import random

class Moneta():
    def __init__(self):
        self.faccia = None
    
    def lancio_random(self):
        randomNumber = random.randint(0,1)
        self.faccia = "testa" if randomNumber == 1 else "croce"

    def __str__(self):
        return f"La moneta è caduta su: {self.faccia}"
    

class Veicolo():
    def __init__(self, marca, modello, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
    
    def __str__(self):
        return f"Dettagli veicolo '{self.marca}', MODELLO: {self.modello}, ANNO: {self.anno}, Speed: {self.speed}"

    def accellerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed
    

class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        with open(f"files/{self.name}", "r") as file:
            finalList = []
            for line in file.readlines():
                elements = line.split(",")
                newList = []
                for element in elements:
                    newList.append(element.strip())
                finalList.append(newList)
            return finalList



#! CSVFILE
# csv = CSVFile("shampoo.csv")
# print(csv.get_data())

#! MONETA
# moneta = Moneta()
# moneta.lancio_random()
# print(moneta)

#! VEICOLO
# veicolo = Veicolo("fiat", "punto", 2009)
# veicolo.accellerare()
# veicolo.accellerare()
# print(veicolo)
# veicolo.frenare()
# print(veicolo.get_speed())
# print(veicolo)
