# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header=1)
'''
The parameter 'delimiter="," ' is set because the file that we are opening has extension CSV(Comma Separated Values)

The parameter 'skip_header=1' is set because the first row of the data(which is called header) contains string values but in our numpy array we need only integers(Remember numpy array can only store data of a single data type)
'''
print(data)
print('--'*30)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data,new_record),axis=0)
print(census)

#Code starts here



# --------------
#Code starts here

age = census[:,:1]

max_age = np.max(age)
min_age = np.min(age)

age_mean = np.mean(age)
age_std = np.std(age)


# --------------
#Code starts here

race_0=census[census[:,2]==0]
print(race_0)
print('--'*50)

race_1=census[census[:,2]==1]
print(race_1)
print('--'*50)

race_2=census[census[:,2]==2]
print(race_2)
print('--'*50)

race_3=census[census[:,2]==3]
print(race_3)
print('--'*50)

race_4=census[census[:,2]==4]
print(race_4)
print('--'*50)

# Calculating length of each array
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minimum = min(len_0,len_1,len_3,len_4)
if minimum==len_0:
    minority_race =0
elif minimum==len_1:
    minority_race=1
elif minimum==len_2:
    minority_race=2
elif minimum==len_3:
    minority_race=3
else:
    minority_race=4



# --------------
#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]
print(senior_citizens)

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here

# Creating two subset arrays
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]

print(avg_pay_high)
print(avg_pay_low)


