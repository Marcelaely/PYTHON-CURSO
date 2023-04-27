def isYearLeap(year):
#
# your code from LAB 1
#
 def daysInMonth(year, month):
#
# your code from LAB 2
#
  def dayOfYear(year, month, day):
#
# put your new code here
#
   print(dayOfYear(2000, 12, 31))

diasNormales= {1:31,
              2:28,
              3:31,
              4:30,
              5:31,
              6:30,
              7:31,
              8:31,
              9:30,
              10:31,
              11:30,
              12:31
              }

def isYearLeap(year):
    siBiciesto=False
 
    if (year % 4 ==0) and (year % 100 !=0 or year % 400==0):
        siBiciesto=True
        
    print("year=",year)    
    print("biciesto=",siBiciesto)
    return siBiciesto


def daysInMonth(year, month):
    diasMes=0
# si no año biciesto entonces dias normales
# si es año biciesto entonces chequear febrero = 28 dias
# put your new code here

    if isYearLeap(year) and month==2:
        print("si año biciesto")
        diasMes=29
    else:
        diasMes=diasNormales[month]

    return diasMes
