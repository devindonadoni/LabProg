class CSVTimeSeriesFile:
    def __init__(self, n):
        self.name = n

    def get_data(self):
        try:
            with open(self.name, "r") as file:
                    finalList = []
                    for line in file.readlines():
                        try:
                            elements = line.split(",")
                            tempList = []
                            passenger_value = int(elements[1].strip())

                            if passenger_value <= 0: 
                                print(f"Generata la seguente eccezione, valore verrà ignorato")
                                continue
                            tempList.append(elements[0].strip())
                            tempList.append(passenger_value)
                            finalList.append(tempList)
                        except Exception as e:
                            print(f"Generata la seguente eccezione {e}, valore verrà ignorato")
                    
                    checkInterity(finalList)
                    return finalList

        except FileNotFoundError:
            raise ExamException("File not found exception")
            

class ExamException(Exception):
    pass

def checkInterity(list):
    last_date = ""

    for line in list:
        current_date = line[0]
        if current_date <= last_date:
            raise ExamException(f"Timestamp fuori ordine o duplicato data {current_date}")
        last_date = current_date

    return True

def group_by_year(year, time_series):
    singleYearList= [item[1] for item in time_series if item[0][0:4]== year]
    return singleYearList

def calcola_media(year_dict):
    media_dict = {}
    for line in year_dict:
        sum = 0
        i = 0
        for item in year_dict.get(line):
            i += 1
            sum += item
        media_dict[line] = sum/i
    return media_dict
    
def compute_variations(time_series, first_year, last_year):
    years_sets = yearCycle(time_series)
    grouped_dict = {item: group_by_year(item, time_series) for item in years_sets}
    # for item in years_sets:
    #     grouped_dict[item] = group_by_year(item, time_series)
    media_dict = calcola_media(grouped_dict)
    media_dict = dict(sorted(media_dict.items()))
    
    
    try:
        year_index2 = list(media_dict.keys())
        first_year_index = year_index2.index(first_year)
        last_year_index = year_index2.index(last_year)
    except Exception as e:
        raise ExamException(f"{e}, controlla che gli anni inseriti siano presenti nel file")

    finalDict = {}
    for i in range(first_year_index, last_year_index):
        year = ""
        media = media_dict.get(list(media_dict)[i]) * 2
        for item in range(i, i + 2):
            media = media - media_dict.get(list(media_dict)[item])
            year =  f"{year}-{list(media_dict)[item]}"

        finalDict[year[1::]] = round(media, 3)

    return finalDict
    
        

def yearCycle(time_series):
    newList = set(line[0][0:4] for line in time_series)
    return newList

try:
    time_series_file = CSVTimeSeriesFile("data.csv")
    time_series = time_series_file.get_data()
except ExamException as e:
    print(f"Raised {e}")
    exit(1)

print(compute_variations(time_series, "2018", "2025"))