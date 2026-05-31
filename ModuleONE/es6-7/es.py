from datetime import datetime, date

class CSVFile():
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Il nome del file deve essere una stringa")
        self.name = name

    def get_data(self, start=None, end=None):
        try:
            with open(f"files/{self.name}", "r") as file:
                listToIterate = []
                finalList = []
                templist = []
                for line in file.readlines(): 
                    templist.append(line)

                if start == None and end == None: 
                    start = 1
                    end = len(templist)
                
                try:
                    for i in range(start-1, end):
                        listToIterate.append(templist[i])
                except IndexError:
                    raise IndexError(f"index error, file has {len(templist)} line/s")

                for item in listToIterate: 
                    elements = item.split(",")
                    newList = []
                    for element in elements:
                        newList.append(element.strip())
                    finalList.append(newList)
                return finalList
        except FileNotFoundError:
            raise FileNotFoundError(f"Errore: Il file 'files/{self.name}' non esiste.")

class NumericalCSVFile(CSVFile):
    def __init__(self, filename):
        super().__init__(filename)

    def get_data(self, *args, **kwargs):
        list = super().get_data(*args, **kwargs)
        newList = []
        for item in list:
            newList.append(self.convertToFloat(item))
        return newList


    def convertToFloat(self, elements):
        try:
            elements[2] = float(elements[2])
            elements[3] = float(elements[3])
            elements[4] = float(elements[4])
            return elements
        except ValueError:
            return f"Error while trying to convert the {elements[0]}"

#! es1
# csv = CSVFile("shampoo.csv")
# print(csv.get_data())

#! es2-es3
# if __name__ == "__main__":
#     try:
#         numericalCSVFile = NumericalCSVFile("shampoo.csv")
#         dati = numericalCSVFile.get_data(1,7)
#         print(dati)
#     except FileNotFoundError as e:
#         print(f"Errore: {e}")
#         # Se vogliamo terminare il programma qui senza traceback:
#         exit(1) # Esce con un codice di errore
#     except TypeError as e:
#         print(f"Errore: {e}")
#         # Se vogliamo terminare il programma qui senza traceback:
#         exit(1) # Esce con un codice di errore
#     except ValueError as e:
#         print(f"Errore: {e}")
#         # Se vogliamo terminare il programma qui senza traceback:
#         exit(1) # Esce con un codice di errore
#     except IndexError as e:
#         print(f"Errore: {e}")
#         # Se vogliamo terminare il programma qui senza traceback:
#         exit(1) # Esce con un codice di errore



#! es5
def counter_to_birth(month, day):
    yearNow = datetime.now().year
    monthNow = datetime.now().month
    dayNow = datetime.now().day
    hourNow = datetime.now().hour
    minuteNow = datetime.now().minute
    secondNow = datetime.now().second
    dateNow = datetime(yearNow, monthNow, dayNow, hourNow, minuteNow, secondNow)
    my_birthday = datetime(yearNow, month, day)
    if(my_birthday < dateNow):
        my_birthday = datetime(yearNow + 1, month, day)
    timeRemaing = my_birthday-dateNow
  
    return timeRemaing


# print(counter_to_birth(int(input("BirthDay month: ")), int(input("BirthDay day: "))))




#! es6
# is_number = False
# while(not is_number):
#     try:
#         number = int(input("Inserisci un numero: "))
#         is_number = True
#         print(number*number)
#     except ValueError as e:
#         print("DEVE ESSERE UN NUMERO")