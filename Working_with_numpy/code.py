# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]


#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((np.array(data), np.array(new_record)))



# --------------
#Code starts here
age = census[:,0]

max_age = max(age)

min_age = min(age)

age_mean = sum(age)/len(age)

age_std = np.std(np.array(age))


# --------------
#Code starts here
race = census[:,2]
lengths = []

race_0_bool = census[:,2] == 0
race_0 = census[race_0_bool]
len_0 = len(race_0)
lengths.append(len_0)

race_1_bool = census[:,2] == 1
race_1 = census[race_1_bool]
len_1 = len(race_1)
lengths.append(len_1)

race_2_bool = census[:,2] == 2
race_2 = census[race_2_bool]
len_2 = len(race_2)
lengths.append(len_2)

race_3_bool = census[:,2] == 3
race_3 = census[race_3_bool]
len_3 = len(race_3)
lengths.append(len_3)

race_4_bool = census[:,2] == 4
race_4 = census[race_4_bool]
len_4 = len(race_4)
lengths.append(len_4)



minority_race = lengths.index(min(lengths))



# --------------
#Code starts here
senior_citizens_bool = census[:,0] > 60
senior_citizens = census[senior_citizens_bool]

working_hours_sum = sum(senior_citizens[:,6])

senior_citizens_len = len(senior_citizens[:,6])

avg_working_hours = working_hours_sum / senior_citizens_len

print(avg_working_hours)



# --------------
#Code starts here
high_bool = census[:,1] > 10
high = census[high_bool]

low_bool = census[:,1] <= 10
low = census[low_bool]

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)

avg_pay_high > avg_pay_low


