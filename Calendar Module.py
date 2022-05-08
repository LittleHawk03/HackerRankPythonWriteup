

from calendar import calendar, weekday
import calendar

z = list(map(int, input().split()))
calendar.TextCalendar(firstweekday=calendar.SUNDAY)

print(calendar.day_name[calendar.weekday(int(z[2]),int(z[0]),int(z[1]))].upper())