# ===== Dates =====

from datetime import datetime
# Datetime es capaz de agrupar tanto la fecha como la hora
now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp() #Es el momento fijo o actual, es decir, el ahora
print (timestamp)

# ===== Crear una fecha =====

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

year_2026 = datetime(2026, 1, 1) # Para definir un año, es necesario el año, el mes y el día

print_date(year_2026)

from datetime import time # Time es un objeto que no tiene nada, por lo que hay que trabajar sobre él
# Es un objeto que permite encapsular tiempo
# Date es capaz de agrupar el tipo de hora
current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
# Date es capaz de agrupar solo la fecha
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 5, 12)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2026 - now
print(diff)

diff = year_2026.date() - current_date
print(diff)

# ===== Operaciones con fechas =====

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks= 10)
end_timedelta = timedelta(300, 100, 100, weeks= 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)