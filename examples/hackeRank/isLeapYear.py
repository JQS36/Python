#know if the year is leap year
#leap year -> año bisiestro

def isLeap(year):
    leap = False
    if year%4==0 and (year%100!=0 or year%400==0):
        leap = True
    return leap

year = int(input("Enter year: "))
print(isLeap(year))