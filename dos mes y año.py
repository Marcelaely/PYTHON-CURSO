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

1900 -> year= 1900
biciesto= False
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


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
