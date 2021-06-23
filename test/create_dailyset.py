import os

class DailyGen:
    def __init__(self):
        for i in range(24): # 0 - 23
            for j in range(60): #  0 - 59
                if j // 10 == 0:
                    cur_time = str(i) + str(0) + str(j)
                else:
                    cur_time = str(i) + str(j)
                command = "echo this is D%s > D%s.csv" % (cur_time, cur_time)
                os.system(command)


if __name__ == "__main__":
    dg = DailyGen()
