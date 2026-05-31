class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        return f"Ciao sono {self.nome} {self.cognome}, {self.ruolo}"

class Studente(Persona):
    def __init__(self,nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi
    
    def saluta(self):
        corsiString = "di"
        for i in self.corsi:
            corsiString = f"{corsiString} {i}"

        return f"{ Persona.saluta(self)}, e frequento i corsi: {corsiString}"

    
class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi
    
    def saluta(self):
        return f"{Persona.saluta(self)}, docente dei corsi {self.corsi}"



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
    

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    
    def __str__(self):
        return f"{super().__str__()}, NUMERO PORTE: {self.numero_porte}"

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def __str__(self):
        return f"{super().__str__()}, TIPO: {self.tipo}"

#! es1
# studente = Studente("Devin", "Donadoni", ["Analisi", "Programmazione", "R"])
# print(studente.saluta())


#! es2
# auto = Auto("Fiat", "Punto", 2009, 5)
# auto.accellerare()
# print(auto.__str__())
# moto = Moto("KAWASAKY", "Ninja H2R", 2015, "Sportiva")
# moto.accellerare()
# print(moto.__str__())






