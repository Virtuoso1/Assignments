class DateCalculator:
    def __init__(self, year: int, month: int, day: int):
        self.q = day
        if month == 1:
            self.m = 13
            self.Y = year-1
        else:
            if month == 2:
                self.m = 14
                self.Y = year - 1
            else:
                self.m = month
                self.Y = year
        self.K = self.Y % 100
        self.J = self.Y // 100

    def date(self):
        h: int = (self.q + (13*(self.m + 1)//5) + self.K + (self.K//4) + (self.J//4) + 5*self.J) % 7
        res: str = ""
        match h:
            case 0:
                res = "Saturday"
            case 1:
                res = "Sunday"
            case 2:
                res = "Monday"
            case 3:
                res = "Tuesday"
            case 4:
                res = "Wednesday"
            case 5:
                res = "Thursday"
            case 6:
                res = "Friday"
        print(f"It was a {res}")
d: int = int(input("Enter day: "))
m: int = int(input("Enter month: "))
y: int = int(input("Enter year: "))

dc: DateCalculator = DateCalculator(y, m, d)
dc.date()