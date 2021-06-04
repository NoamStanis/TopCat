#-------------------------------------------------------------------------------------
#_____________________________________________________________________________________
# Written by: Elizabethann Cook May 2021
# Concatenates all the weekly csv files into one monthly file
# Naming convention for input files Weekof[YYYYMMDD].csv 
# Naming conventrion for final resultant file [HOSTNAME]_USERDAT_[MONTH]_[YEAR].csv
# Runs onthe 11'th of the month and concatenates the previous months data
#_____________________________________________________________________________________
#-------------------------------------------------------------------------------------
 
##################################################################################
#import commands
import os
import subprocess as sp
import calendar
from calendar import  monthrange
from datetime import date
#date set variables
today = date.today()
Year = today.year
Month = today.month-1                           
LastMonth =today.month-2                                # handle the first week overlap with the previous month data 
if Month==1:                                            # January exception case when running in february
    LastMonth = 12
if Month ==0:                                           # December exception case when running in january
    Month = 12                                   
    LastMonth = 11
    Year = today.year-1
dfin= monthrange(Year,int(Month))[1]                    # finds the date range of the month being analyzed
dfinprev= monthrange(Year,int(LastMonth))[1]            # finds the daterange of the previous month 
#cal = calendar.TextCalendar(calendar.SUNDAY)           # Finds the date of the 
if dfin % 7 == 0:                                       # finds how many days are in that month 
    squaremonth = 0                                     # case for a prefectly rectangular month ( only feburary on non leap year) 
else:
    squaremonth = 1                                
for k in range(1,10):                                   # Loops thru to find the date of the first sunday of the month
    if k !=0:
        day =date(Year,Month,k) 
        if day.weekday()==6:
            sun_1 = k              # found it!

# Case 1: Default
###########################################################################################################################################################################
if squaremonth == 1:
    start_day = (sun_1-7)+dfinprev                      # (first sunday - 7) = -#  --> (-#) + number of final day of last month = last sunday of previous month 
    F1 = "Weekof%s%s%s.csv" %(Year,LastMonth,start_day) # handle the overlap of the first week
    F2 = "Weekof%s%s%s.csv" %(Year,Month,sun_1)
    cmd1 = "cat %s %s >temp.csv"%(F1, F2)
    os.system(cmd1)
    cmd2 = "rm %s"%F1
    os.system(cmd2)
    cmd3 = "rm %s"%F2
    os.system(cmd3)
    cmd4 = " mv temp.csv %s"%F2
    os.system(cmd4)
    # code above is for handling overlap within the previous month in the first week 
    for i in range (sun_1, dfin, 7):
        F3 = "Weekof%s%s%s.csv" %(Year,Month,i)
        F4 = "Weekof%s%s%s.csv" %(Year,Month,(i+7))
        cmd5 = "cat %s %s >temp.csv"%(F3, F4)
        os.system(cmd5)
        cmd6 = "rm %s"%F3
        os.system(cmd6)
        cmd7 = "rm %s"%F4
        os.system(cmd7)
        cmd8 = " mv temp.csv %s"%F4
        os.system(cmd8)
    F5 = sp.getoutput('hostname')      
    cmd9 = "mv Weekof%s%s%s.csv %s_USRDAT_%s_%s.csv"%(Year, Month, dfin, F5, calendar.month_name[Month], Year) #works
    os.system(cmd9) 
###########################################################################################################################################################################

# Case 2: Used the basic logic of the code, only rund in february on a non leap year when the mopnth is perfectly rectangular
###########################################################################################################################################################################           
if squaremonth == 0:
    for i in range (sun_1, dfin , 7):          #Loop increments in 7 from the first sunday landing on each subsequent sunday until the end of the month 
        F01 = "Weekof%s%s%s.csv" %(Year,Month,i)
        F02 = "Weekof%s%s%s.csv" %(Year,Month,(i+7))
        cmd01 = "cat %s %s >temp.csv"%(F01, F02)
        os.system(cmd01)
        cmd02 = "rm %s"%F01
        os.system(cmd02)
        cmd03 = "rm %s"%F02
        os.system(cmd03)
        cmd04 = " mv temp.csv %s"%F02
        os.system(cmd04)
    F03 = sp.getoutput('hostname')      
    cmd05 = "mv Weekof%s%s%s.csv %s_USRDAT_%s_%s.csv"%(Year,Month,dfin, F03, calendar.month_name[Month], Year) #works
    os.system(cmd05) 
###########################################################################################################################################################################
