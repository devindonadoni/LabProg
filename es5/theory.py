
#! PUBLIC, PROTECTED & PRIVATE

# PUBLIC      --> nome            tutti                           accessibile ovunque

# PROTECTED   --> _nome           classe e sottoclassi            accessibile, ma sconsigliato

# PRIVATE     --> __nome          solo classe                     peraccedere = _NomeClasse__nome (name manling)

#es..
    # class Banca:
    #     def __init__(self, saldo):
    #         self.__saldo = saldo

    # b = Banca(100)
    # print(b.__saldo)  #ERRORE
    # print(b._Banca__saldo)   #FUNZIONA



#! CLASS METHOD
#Un metodo di clsse appartenente alla classe stessa e non ad una specifica istanza

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
  
    @classmethod
    def da_stringa(cls, stringa_dati):
        nome, eta = stringa_dati.split(',')
        return cls(nome, int(eta))
  
p = Persona.da_stringa("Mario,30")



#!EREDITARIETA'
#Permette di creare una classe figlia (SOTTOCLASSE) che estende o modifica la classe padre (SUPERCLASSE)
#*      override = sottoclasse puo riscrivere un metodo del padre per personalizzarlo
#*      super()  = funzione per accedere ai metodi della classe padre 

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print(f"Ciao, sono {self.nome} {self.cognome}")
class Studente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__(nome, cognome)
        self.corsi = corsi
    def saluta(self):
        super().saluta()
        print(f"Frequento: {', '.join(self.corsi)}")
corsi_mat = ["Analisi", "Programmazione"]
s = Studente("Decin", "Donadoni", corsi_mat)
s.saluta()



