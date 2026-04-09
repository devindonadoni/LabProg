class Poligono:
    def __init__(self, numero_lati):
        self.numero_lati = numero_lati

    def __str__(self):
        return f"Sono un poligono con {self.numero_lati} {"lato" if self.numero_lati == 1 else "lati" }"
    
class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
    
    def __str__(self):
        return f"{super().__str__()}, quindi sono un quadrilatero"

class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def __str__(self):
        return f"{super().__str__()}, piu precisamente un rettangolo. --> BASE: {self.base}, ALTEZZA: {self.altezza} "

    def get_perimetro(self):
        return (self.base * self.altezza) * 2
    
    def get_altezza(self):
        return (self.base * self.altezza)

class Triangolo():
    def __init__(self, lati):
        self.lati = lati

    def __str__(self):
        return f"Sono un triangolo e i miei lati sono {self.lati}"
    
    def get_perimeto(self):
        perimetro = 0
        for i in self.lati:
            perimetro += i 
        return perimetro

    def is_equilatero(self):
        last = self.lati[0]
        for i in self.lati:
            if last != i:
                return False
        return True


#--------------------------------------------------------------------------

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
    
    def get_courses(self):
        return self.corsi

    
class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi
    
    def saluta(self):
        return f"{Persona.saluta(self)}, docente dei corsi {self.corsi}"

    def get_courses(self):
        return self.corsi



docente = Docente("Franco", "Rossi", ["analisi", "algebra", "Programmazione"])
studente = Studente("Dev", "Dona", ["analisi", "algebra"])
corsi_docente = docente.get_courses()
corsi_studente = studente.get_courses()

for corsoS in corsi_studente:
    insegna = False
    for corsoD in corsi_docente:
        if corsoS == corsoD:
            insegna = True
    if insegna == False:
        break
print(f"Il docente {"INSEGNA" if insegna else "NON INSEGNA"} in tutti i corsi dello studente")



#! es4
# quad = Quadrilatero()
# rett = Rettangolo(5, 10)
# lati = [3, 3, 3]
# tr = Triangolo(lati)
# print(tr.__str__())
# print(tr.is_equilatero())