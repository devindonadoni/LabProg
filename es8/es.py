
#! es1
# list = [x**2 for x in range(1, 21) if x**2%4 == 0]
# print(list)

#! es2
# parole = ["Python", "Laboratorio", "Programmazione", "AI", "Studente"]
# final_dict = {x:len(x) for x in parole}
# print(final_dict)

#! es3
# temperature_c = [15, 22, 18, 25, 30, 12, 21]
# taskA = list(filter(lambda x: x>20, temperature_c ))
# taskB = list(map(lambda x: x+273.15, taskA))
# print(taskA)
# print(taskB)

#! es4

class ContoAllaRovescia:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > 0: 
            self.n -= 1
            return self.n + 1
        else:
            raise StopIteration
        
    
for numero in ContoAllaRovescia(5):
    print(numero)