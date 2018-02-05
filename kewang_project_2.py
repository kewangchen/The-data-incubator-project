#         Kewang 2018-02-04                 #
#This code is used to study the crime data  #
import csv
#m is used to count the total number
m=0
with open('Crime_Data_from_2010_to_Present.csv','r',buffering=20000000) as csvfile:
    readCSV=csv.reader(csvfile)
    #skip the title
    next(readCSV)
    # Time and Gender, are selected from the original data.
    newdata=[]
    for row in readCSV:
        m+=1
        temp = [row[3],row[11]]
        newdata.append(temp)
list_sum=[400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,
          1800,1900,2000,2100,2200,2300,100,200,300]
number=[]
F_number=[];M_number=[]
for row in list_sum:
    temp_1 = 0
    F_count = 0
    M_count = 0
    for line in newdata:
        if abs(int(line[0])-int(row))<30:
            if line[1] == 'F':
                F_count += 1
                temp_1 += 1
            elif line[1] == 'M':
                M_count += 1
                temp_1 += 1
    F_number.append(F_count)
    M_number.append(M_count)
    number.append(temp_1)
print(number)
print(sum(number))
print(list_sum)
print(F_number)
print(sum(F_number))
print(M_number)
print(sum(M_number))
print(F_number + M_number)

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

fig = plt.figure()
ax = fig.add_subplot(111)
xs = range(23)
#  style the x-labels
labels = ['04:00',500,600,'07:00',800,900,'10:00',1100,1200,'13:00',1400,1500,'16:00',1700,
          1800,'19:00',2000,2100,'22:00',2300,100,'02:00(+1)',300]

def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''


ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plot
a1, = ax.plot(xs, number, 'g--*')
a2, = ax.plot(xs, F_number, 'r-+')
a3, = ax.plot(xs, M_number, 'b-.')
# annotate the plot:
plt.xlabel("Time", fontsize=18)
plt.ylabel("Number of crimes", fontsize=18)
# plt.legend(["Crime", "Romney"], loc="upper left", fontsize=16)
plt.title("Crime at different time of the day", fontsize=18)
# Add a legend
plt.legend([a1, a2, a3], ["Total", "Female", "Male"])
#  control the size of the figure:
plt.gcf().set_size_inches(9, 6)  # gcf = "get current figure"
#  style the x-labels
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()
fig.savefig('2nd plot.png')