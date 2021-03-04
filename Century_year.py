def centuryFromYear(year):
    century_aux = year / 100
    century = year // 100

    if century_aux > century:
        century += 1

    return century

print(centuryFromYear(1700))