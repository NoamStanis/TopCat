# -------------------------------------------------------------------------------------
# _____________________________________________________________________________________
# Written by: Elizabethann Cook May 2021
# Weekly data concatenation
# Naming convention for input files D[YEARMMDD].csv
# Naming convention for final resultant file Weekof[YYYYMMDD].csv
# Week starts on SUNDAY, run this on SATURDAY, total week is 7 DAYS
# OUTPUT FILE DATE IS BEGINNING SUNDAY
# _____________________________________________________________________________________
# -------------------------------------------------------------------------------------

#######################################################################################
# Import commands
import os
from datetime import date
from calendar import monthrange

class Weekly:

    def __init__(self):
        # date set variables
        today = date(2021,6,5) # CHANGE THIS FOR TESTING DIFFERENT CASES, NOTHING ELSE >:-(
        self.finish = int(today.day)
        self.Year = str(today.year)
        self.Month = str(today.month)
        self.LastMonth = today.month - 1

        self.start = today.day - 6  # the sunday that began that specific week

        if self.LastMonth == 0:  # January exception case
            self.LastMonth = 12
            self.LastYear = today.year - 1


        # int(self.start)
        self.dfin = monthrange(today.year, int(self.LastMonth))[1]

        # Case 1: Runs for data in the first week of a month
        if self.start <= 0 and self.LastMonth != 12:
            self.firstweek(self.Year, self.Month, self.LastMonth)

        # Case 2: Runs on the first week of january
        elif self.start <= 0 and self.LastMonth == 12:
            self.firstJan(self.LastYear, self.LastMonth, self.Year, self.Month)

        # Case 3: Default code logic runs when it is not the first week of a month
        else:
            self.regularweek(self.Year, self.Month)

    def firstweek(self, Year, Month, LastMonth):
            F1 = 0; F2 = 0
            self.start += self.dfin
            for j in range(self.start, self.dfin):
                F1 = "D%s%d%d.csv" % (Year, LastMonth, j)
                F2 = "D%s%d%d.csv" % (Year, LastMonth, j + 1)
                cmd1 = "cat %s %s > temp.csv" % (F1, F2)  # concatenate two csv files into one and renames the resultant file to temp
                os.system(cmd1)
                cmd2 = "rm %s" % F2  # removes the file with the highest number out of the two concatenated
                os.system(cmd2)
                cmd3 = "rm %s" % F1  # removes the other file leaving only the concatenated file
                os.system(cmd3)
                cmd4 = "mv temp.csv %s" % F2  # renames the temp file to the name of the file previopusly removed wit hthe higher value (F2),
                os.system(cmd4)

            # transition
            F3 = "D%s%s%d.csv" % (Year, Month, 1)
            cmd5 = "cat %s %s > temp.csv" % (F2, F3)
            os.system(cmd5)
            cmd6 = "rm %s" % F2  # removes the file with the highest number out of the two concatenated
            os.system(cmd6)
            cmd7 = "rm %s" % F3  # removes the other file leaving only the concatenated file
            os.system(cmd7)
            cmd8 = "mv temp.csv %s" % F3  # renames the temp file to the name of the file previopusly removed wit hthe higher value (F4),
            os.system(cmd8)

            for i in range(1, self.finish):
                F3 = "D%s%s%d.csv" % (Year, Month, i)
                F4 = "D%s%s%d.csv" % (Year, Month, i + 1)
                cmd9 = "cat %s %s > temp.csv" % (
                    F3, F4)  # concatenate two csv files into one and renames the resultant file to temp
                os.system(cmd9)
                cmd10 = "rm %s" % F4  # removes the file with the highest number out of the two concatenated
                os.system(cmd10)
                cmd11 = "rm %s" % F3  # removes the other file leaving only the concatenated file
                os.system(cmd11)
                cmd12 = "mv temp.csv %s" % F4  # renames the temp file to the name of the file previopusly removed wit hthe higher value (F4),
                os.system(cmd12)

            start = int(str(Year) + str(LastMonth) + str(self.start))
            cmd13 = "mv D%s%s%d.csv Weekof%d.csv" % (Year, Month, self.finish, start)  # renames the final concateted file it with the naming convention Weekof[YEARMMDD]
            os.system(cmd13)

    def firstJan(self, LastYear, LastMonth, Year, Month):
            self.start += self.dfin
            for j in range(self.start, self.dfin):
                F01 = "D%s%d%d.csv" % (LastYear, LastMonth, j)
                F02 = "D%s%d%d.csv" % (LastYear, LastMonth, j + 1)
                cmd01 = "cat %s %s > temp.csv" % (F01, F02)  # concatenate two csv files into one and renames the resultant file to temp
                os.system(cmd01)
                cmd02 = "rm %s" % F02  # removes the file with the highest number out of the two concatenated
                os.system(cmd02)
                cmd03 = "rm %s" % F01  # removes the other file leaving only the concatenated file
                os.system(cmd03)
                cmd04 = "mv temp.csv %s" % F02  # renames the temp file to the name of the file previopusly removed wit hthe higher value (F2),
                os.system(cmd04)
            # transition
            F03 = "D%s%s%d.csv" % (Year, Month, 1)
            cmd05 = "cat %s %s > temp.csv" % (F02, F03)
            os.system(cmd05)
            cmd06 = "rm %s" % F02  # removes the file with the highest number out of the two concatenated
            os.system(cmd06)
            cmd07 = "rm %s" % F03  # removes the other file leaving only the concatenated file
            os.system(cmd07)
            cmd08 = "mv temp.csv %s" % F03  # renames the temp file to the name of the file previopusly removed wit hthe higher value (F4),
            os.system(cmd08)

            for i in range(1, self.finish):
                F03 = "D%s%s%d.csv" % (Year, Month, i)
                F04 = "D%s%s%d.csv" % (Year, Month, i + 1)
                cmd09 = "cat %s %s > temp.csv" % (F03, F04)  # concatenate two csv files into one and renames the resultant file to temp
                os.system(cmd09)
                cmd010 = "rm %s" % F04  # removes the file with the highest number out of the two concatenated
                os.system(cmd010)
                cmd011 = "rm %s" % F03  # removes the other file leaving only the concatenated file
                os.system(cmd011)

                cmd012 = "mv temp.csv %s" % F04  # renames the temp file to the name of the file previopusly removed with the higher value (F4),
                os.system(cmd012)
            print(LastYear, LastMonth, self.finish, self.start)
            cmd013 = "mv D%s%s%d.csv Weekof%d%d%d.csv" % (Year, Month, self.finish,
                                                          LastYear, LastMonth, self.start) # cmd 013renames the final concateted file it with the naming convention Weekof[YEARMMDD]
            os.system(cmd013)  # date is the Monday at the beginning of that week

    def regularweek(self, Year, Month):
            for k in range(self.start, self.finish):
                F01 = "D%s%s%d.csv" % (Year, Month, k)
                F02 = "D%s%s%d.csv" % (Year, Month, k + 1)
                cmd01 = "cat %s %s > temp.csv" % (F01, F02)  # concatenate two csv files into one and renames the resultant file to temp
                os.system(cmd01)
                cmd02 = "rm %s" % F01  # removes the file with the highest number out of the two concatenated
                os.system(cmd02)
                cmd03 = "rm %s" % F02  # removes the other file leaving only the concatenated file
                os.system(cmd03)
                cmd04 = "mv temp.csv %s" % F02  # renames the temp file to the name of the file previopusly removed wit hthe higher value (F6),
                os.system(cmd04)  # doing this allows the for loop to function as if it is simpily appending one file continuiously
            start = int(Year + Month + str(self.start))  # creates an intergerr variable start of the form [YYYYMMDD] leading 0's are omitted for months and days 1 thru 9
            cmd14 = "mv D%s%s%d.csv Weekof%s%s%d.csv" % (Year, Month, self.finish,
                                                         Year, Month, self.start)    # cmd14 renames the final concateted file it with the naming convention Weekof[YEARMMDD]
            os.system(cmd14)  # date is the sunday at the beginning of that week


if __name__ == "__main__":
    week = Weekly()
