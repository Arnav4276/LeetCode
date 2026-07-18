import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        D = datetime.date(year,month,day)
        d = D.strftime("%A")
        return d