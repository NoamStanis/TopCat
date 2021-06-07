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

class Monthly:
    def __init__(self):
        self.today = date(2021,6,11)

        today = self.today
        self.Year = today.year
        self.Month = today.month-1
        self.LastMonth =today.month-2                                # handle the first week overlap with the previous month data
        if self.Month==1:                                            # January exception case when running in february
            self.LastMonth = 12
        if self.Month ==0:                                           # December exception case when running in january
            self.Month = 12
            self.LastMonth = 11
            self.Year = today.year-1
        self.dfin= monthrange(self.Year,int(self.Month))[1]                    # finds the date range of the month being analyzed
        self.dfinprev= monthrange(self.Year,int(self.LastMonth))[1]            # finds the daterange of the previous month
        #cal = calendar.TextCalendar(calendar.SUNDAY)           # Finds the date of the
        if self.dfin % 7 == 0:                                       # finds how many days are in that month
            squaremonth = True                                    # case for a prefectly rectangular month ( only feburary on non leap year)
        else:
            squaremonth = False

        for k in range(1,10):                                   # Loops thru to find the date of the first sunday of the month
            if k !=0:
                day = date(self.Year,self.Month,k)
                if day.weekday()==6:
                    self.sun_1 = k              # found it
                    break

        if not squaremonth:
            self.run()

        else:
            self.square_month()

# Case 1: Default
    def run(self):

        self.dfin -= 1
        for i in range (self.sun_1, self.dfin, 7):
            F1 = "Weekof%s%s%s.csv" %(self.Year,self.Month,i)
            F2 = "Weekof%s%s%s.csv" %(self.Year,self.Month,(i+7))
            cmd1 = "cat %s %s >temp.csv"%(F1, F2)
            os.system(cmd1)
            cmd2 = "rm %s"%F1
            os.system(cmd2)
            cmd3 = "rm %s"%F2
            os.system(cmd3)
            cmd4 = " mv temp.csv %s"%F2
            os.system(cmd4)
            print("i = ", i, "F1 = ", F1, "F2 = ", F2)

        F3 = sp.getoutput('hostname')
        cmd5 = "mv Weekof%s%s%s.csv %s_USRDAT_%s_%s.csv"%(self.Year, self.Month, self.dfin, F3, calendar.month_name[self.Month], self.Year) #works
        os.system(cmd5)



# Case 2: Used the basic logic of the code, only rund in february on a non leap self.Year when the month is perfectly rectangular
    def square_month(self):
        for i in range (self.sun_1, self.dfin, 7):          #Loop increments in 7 from the first sunday landing on each subsequent sunday until the end of the month
            F01 = "Weekof%s%s%s.csv" %(self.Year,self.Month,i)
            F02 = "Weekof%s%s%s.csv" %(self.Year,self.Month,(i+7))
            cmd01 = "cat %s %s >temp.csv"%(F01, F02)
            os.system(cmd01)
            cmd02 = "rm %s"%F01
            os.system(cmd02)
            cmd03 = "rm %s"%F02
            os.system(cmd03)
            cmd04 = " mv temp.csv %s"%F02
            os.system(cmd04)

        F03 = sp.getoutput('hostname')
        cmd05 = "mv Weekof%s%s%s.csv %s_USRDAT_%s_%s.csv"%(self.Year,self.Month,self.dfin, F03, calendar.month_name[self.Month], self.Year) #works
        os.system(cmd05)

if __name__ == "__main__":
    month = Monthly()
