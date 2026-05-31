
#! ==========================================================
#! LEZIONI 6-7: GESTIONE ERRORI E INPUT
#! ==========================================================

#! ECCEZIONI E TRACEBACK
# Le eccezioni sono oggetti che segnalano un problema nel flusso del codice[cite: 492, 496].
# Il Traceback rintraccia all'indietro le chiamate che hanno causato l'errore[cite: 556, 557].

#* Tipi Comuni:
# ValueError    --> Valore errato (es. 'Ciao' in float) [cite: 489]
# TypeError     --> Tipo non compatibile [cite: 507]
# IndexError    --> Indice fuori portata [cite: 516]


#! COSTRUTTO TRY-EXCEPT-ELSE-FINALLY
# Gestisce gli errori senza bloccare l'esecuzione[cite: 593, 649].

try:
    num = float(input("Inserisci un numero: ")) # Codice a rischio [cite: 650]
except ValueError:
    print("Errore: devi inserire un valore numerico!") # Gestione errore [cite: 652]
else:
    print("Tutto ok, nessun errore.") # Se non ci sono errori [cite: 654]
finally:
    print("Operazione conclusa.") # Eseguito SEMPRE [cite: 655]


#! SOLLEVARE E CREARE ECCEZIONI
#* raise = lancia manualmente un'eccezione [cite: 582, 753]

#? Creazione eccezione personalizzata:
class InvalidInputError(Exception): # Eredita da Exception [cite: 763, 772]
    pass

def controlla_valore(n):
    if n < 0:
        raise InvalidInputError("Il numero non può essere negativo!") # [cite: 765, 770]


#! CONTROLLO E SANITIZZAZIONE INPUT
# Non fidarsi mai degli input; prevenire o correggere (EAFP: "prima provo, poi chiedo scusa")[cite: 694, 716].

#* isinstance(obj, Classe)  --> Verifica se obj appartiene a quella classe (o sottoclassi) [cite: 733, 789]
#* .strip()                 --> Toglie spazi all'inizio/fine [cite: 817, 830]
#* .upper() / .lower()      --> Uniforma il formato delle stringhe [cite: 806]


#! MODULI E __MAIN__
# Per evitare che il codice venga eseguito quando il file viene importato[cite: 211, 215]:
if __name__ == "__main__":
    # Eseguito solo se lo script viene lanciato direttamente [cite: 222]
    pass