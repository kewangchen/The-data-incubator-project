#         Kewang 2018-02-04                 #
#This code is used to study the crime data  #
import csv
#m is used to count the total number
m=0
with open('Crime_Data_from_2010_to_Present.csv','r',buffering=20000000) as csvfile:
    readCSV=csv.reader(csvfile)
    #skip the title
    next(readCSV)
    # Year, Age, Gender, Place are selected from the original data.
    newdata=[]
    for row in readCSV:
        m+=1
        temp = [row[0], row[10], row[11],row[14]]
        newdata.append(temp)
    print(m)
    count_st=0;count_pl=0;count_mu=0
    count_sw=0;count_sf=0
    Fcount_st=0;Fcount_pl=0;Fcount_mu=0
    Fcount_sw=0;Fcount_sf=0
    Mcount_st=0;Mcount_pl=0;Mcount_mu=0
    Mcount_sw=0;Mcount_sf=0
    for row in newdata:
        if row[3]=='STREET':
            count_st+=1
            if row[2]=='F':
                Fcount_st+=1
            elif row[2]=='M':
                Mcount_st+=1
        if row[3]=='PARKING LOT':
            count_pl+=1
            if row[2]=='F':
                Fcount_pl+=1
            elif row[2]=='M':
                Mcount_pl+=1
        if row[3]=='SIDEWALK':
            count_sw+=1
            if row[2]=='F':
                Fcount_sw+=1
            elif row[2]=='M':
                Mcount_sw+=1
        if row[3]=='MULTI-UNIT DWELLING (APARTMENT, DUPLEX, ETC)':
            count_mu+=1
            if row[2]=='F':
                Fcount_mu+=1
            elif row[2]=='M':
                Mcount_mu+=1
        if row[3]=='SINGLE FAMILY DWELLING':
            count_sf+=1
            if row[2]=='F':
                Fcount_sf+=1
            elif row[2]=='M':
                Mcount_sf+=1
    print(count_st,count_pl,count_mu,count_sw,count_sf)
    print(Fcount_st, Fcount_pl, Fcount_mu, Fcount_sw, Fcount_sf)
    print(Mcount_st, Mcount_pl, Mcount_mu, Mcount_sw, Mcount_sf)

##################################################
#  Plot
##################################################
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 5
female = (Fcount_st, Fcount_pl, Fcount_mu, Fcount_sw, Fcount_sf)
male= (Mcount_st, Mcount_pl, Mcount_mu, Mcount_sw, Mcount_sf)
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.3
opacity = 0.8

rects1 = plt.bar(index, female, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Female')

rects2 = plt.bar(index + bar_width, male, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Male')

plt.xlabel('Place')
plt.ylabel('Crime numbers')
plt.title('Crime in the City of Los Angeles dating back to 2010')
plt.xticks(index , ('Street', 'Parking lot', 'Sidewalk', 'Multi-unit dwelling', 'Single family dwelling'),rotation='45')
plt.legend()

plt.tight_layout()
plt.show()
fig.savefig('plot.png')



