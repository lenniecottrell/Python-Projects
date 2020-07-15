from datetime import datetime
import pytz
from pytz import timezone    



##PDXtime = datetime.now()
##print(PDXtime.hour)
##
##NYCtime = PDXtime.hour + 3
##print(NYCtime)
##
##Londontime = PDXtime.hour + 8
##print(Londontime)



Londontz = timezone('Europe/London')
Londonlocaltime = datetime.now(Londontz)
print(Londonlocaltime)
print(Londonlocaltime.strftime('%H')) #just the hour in 24 hr format


PDXtz = timezone('America/Los_Angeles')
PDXlocaltime = datetime.now(PDXtz)
print(PDXlocaltime)
print(PDXlocaltime.strftime('%H'))

NYCtz = timezone('America/New_York')
NYClocaltime = datetime.now(NYCtz)
print(NYClocaltime)
print(NYClocaltime.strftime('%H'))
