class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1971.1.1 is Friday
        months = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
        leap_months = [31,29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        
        years = year - 1971
        leaps = len([x for x in range(1972, year) if x % 4 == 0])
            
        diff = ((years * 365) + leaps)
        
        for m in range(month-1):
            if year % 4 == 0:
                diff += leap_months[m]
            else:
                diff += months[m]
        
        diff+=day-1
        return days[diff % 7]
"""
from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A")
"""