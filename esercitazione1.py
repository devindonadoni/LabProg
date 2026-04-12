class MovingAverage:
    def __init__(self, n):
        if isinstance(n, int) and n > 0:
            self.n = n
        else:
            raise ExamException("La finestra DEVE essere un numero intero")
        
    def compute(self, number_list):
        if not isinstance(number_list, list):
            raise ExamException("Errore, deve essere una lista")

        if len(number_list) < self.n:
            raise ExamException(f"La lista deve contenere almeno {self.n} elementi")

        finalList = []

        for start in range(len(number_list) - self.n + 1):
            total = 0
            for i in range(start, start + self.n):
                if not isinstance(number_list[i], (int, float)):
                    raise ExamException("La lista deve contenere solo numeri")
                total += number_list[i]
            finalList.append(total / self.n)
        return finalList


class ExamException(Exception):
    pass


try:
    m = MovingAverage(3) 
    print(m.compute(4))
except ExamException as e:
    print(f"Si e' verificato un errore: {e}")
    exit(1)