class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            with open(f"files/{self.name}", "r") as file:
                finalList = []

                for line in file.readlines():
                    fileLinesList = []
                    try: 
                        elements = line.split(",")
                        elements[0].split("-")
                        int(elements[1])

                        if(len(elements) == 2):
                            fileLinesList.append(elements[0].strip())
                            fileLinesList.append(int(elements[1].strip()))
                            finalList.append(fileLinesList)
                    except Exception as e:
                        pass

                return finalList
        except FileNotFoundError:
            raise ExamException("Errore file non trovato")

class ExamException(Exception):
    pass


def same_year(year, item):
    if year == item[0][0:4]:
        return True
    else:
        return False


def groupby_year(year, firstList):
    yearList = []
    for item in firstList:
        if item[0][0:4] == str(year):
            yearList.append(item[1])
    return yearList

def dict_year(time_serires):
    yearlist = []
    newDict = {}
    for item in time_serires:
        yearlist.append(item[0][0:4])
    yearSet = set(yearlist)

    for item in yearSet:
        newDict[item] = groupby_year(item, time_series)
    return newDict

def calcolaMedia(dict):   
    newdict = {} 
    for item in dict:
        totale = 0
        n = 0
        for valore in dict.get(item):
            n += 1
            totale += valore
        newdict[item] = round(totale/n, 2)
    
    return newdict
            
                    


def compute_variations(time_series, first_year, last_year):
    media_passenger_per_year_dict = calcolaMedia(passenger_per_year_dict)
    
    newDict = {}
    j = 0
    start = first_year
    for i in range(start, last_year+ 1):
        yearList = []
        mediaList = []
        for item in range(start, start + 1):
            yearList.append(item)
            mediaList.append(media_passenger_per_year_dict.get(item))
            print(yearList)
            print(mediaList)

        newDict[f"{yearList[0]}-{yearList[1]}"] = mediaList[0] - mediaList[1] 
    return newDict


    


csv = CSVTimeSeriesFile("data.csv")
time_series = csv.get_data()
passenger_per_year_dict = dict_year(time_series)
media_passenger_per_year_dict = calcolaMedia(passenger_per_year_dict)

print(compute_variations(time_series, 1949, 1950))