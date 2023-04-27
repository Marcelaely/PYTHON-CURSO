def isYearLeap(year):
    siBiciesto=False
 
    if (year % 4 ==0) and (year % 100 !=0 or year % 400==0):
        siBiciesto=True
        
    print("year=",year)    
    print("biciesto=",siBiciesto)
    return siBiciesto

""" 
year1=4
year2=5
if isYearLeap(year2):
    print("sip")
else:
    print("nop")
"""

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")