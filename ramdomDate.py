import random
import time
def getrandomdate(startdate,enddate):
    print("printing the random date between",startdate,"and",enddate)
    randomgenerater=random.random()
    dateformat="%m/%d/%Y"
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+randomgenerater*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print(getrandomdate("2/5/2013","7/8/2023"))