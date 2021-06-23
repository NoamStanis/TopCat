#-------------------------------------------------------------------------------------
#_____________________________________________________________________________________
# Written by: Elizabethann Cook & Noam Stanislawski May 2021 - June 2021
# Daily file concatenation from the results of running top once/ minute every minute of the day
# This file should be ran at midnight every night (0:00 in 24 hr time)
# Naming convention for input files D[TIME].csv
# Naming convention for resulting file D[YEARMMDD].csv
#___________________________________________________________________________________
#-------------------------------------------------------------------------------------
###################################################################################################################################################################
import os
from datetime import date

class Daily:
    today = date.today()
    d8= today.strftime("%Y%m%d")
    Day = str(today.day)
    Month = str(today.month)
    Year = str(today.year)

    def cat(self):
        F3 = os.path.abspath("test/D059.csv")
        for i in range(24): # 0 - 23
            for j in range(60): #  0 - 59
                if j  < 9: # minute is sin
                    cur_min = str(i) + str(0) + str(j)
                    next_min = str(i) + str(0) + str(j+1)

                elif j == 9:
                    cur_min = str(i) + str(0) + str(j)
                    next_min = str(i) + str(j+1)

                else:
                    cur_min = str(i) + str(j)
                    next_min = str(i) + str(j+1)

                F1 = os.path.abspath("D%s.csv" %cur_min)
                F2 = os.path.abspath("D%s.csv" %next_min)

                if os.path.isfile('%s'%F1):                                 # checks to see if the first file exists if yes then the below  code can execute
                    if os.path.isfile('%s'%F2):                             #  checks to see if the second file exists
                        cmd1 = "cat %s %s > temp.csv" %(F1 , F2)            # concatenate two csv files into one and renames the resultant file to temp
                        os.system(cmd1)
                        cmd2 = "rm %s" %F2                                  # removes the file with the highest number out of the two concatenated
                        os.system(cmd2)
                        cmd3= "rm %s" %F1                                   # removes the other file leaving only the concatenated file
                        os.system(cmd3)
                        cmd4="mv temp.csv %s" %F2                           # renames the temp file to the name of the file previopusly removed wit hthe higher value (F2),
                        os.system (cmd4)                                    # doing this allows the for loop to function as if it is simpily appending one file continuiously

                    else:                                                   # reached the hour, need to concat with earlier hour
                        if i > 0:                                           # can't conctenate negative hourscd
                            F3 = os.path.abspath("D059.csv")
                            cmd5 = "cat %s >> %s" %(F1, F3)
                            os.system(cmd5)
                            os.system("rm %s" %F1)
                # else:
                #     raise RuntimeError("Cannot find %s" %F1)

        os.system("mv %s D%s%s%s.csv" %(F3, self.Year, self.Month, self.Day))

if __name__ == "__main__":
    d = Daily()
    d.cat()

###################################################################################################################################################################
