import os


for i in range(12): # 0 - 23
    for j in range(60): #  0 - 59
        if j // 10 == 0:
            cur_time = str(i) + str(0) + str(j)
        else:
            cur_time = str(i) + str(j)
        command = "echo this is D%s > D%s.csv" % (cur_time, cur_time)
        os.system(command)


# os.system("echo this is D1 >D1.csv")
# os.system("echo this is D2 >D2.csv")
# os.system("echo this is D3 >D3.csv")
# os.system("echo this is D4 >D4.csv")
# os.system("echo this is D5 >D5.csv")
# os.system("echo this is D6 >D6.csv")
# os.system("echo this is D7 >D7.csv")
# os.system("echo this is D8 >D8.csv")
# os.system("echo this is D9 >D9.csv")
# os.system("echo this is D10 >D10.csv")
# os.system("echo this is D11 >D11.csv")
# os.system("echo this is D12 >D12.csv")
# ^one day
