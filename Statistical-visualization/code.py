# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 

data = pd.read_csv(path)

# Replace '-' to 'Agender' in 'Gender' column
data['Gender'].replace('-', 'Agender', inplace=True)

gender_count = data['Gender'].value_counts() # counts the valuee
gender_count.plot(kind='bar', title='Gender Distribution') # plots the graph





# --------------
#Code starts here

alignment = data['Alignment'].value_counts() # ccount the value in Alignment column
labels = alignment.index# Labels for pie chart
plt.pie(alignment, labels = labels, shadow=True)#  Plot the pie chart


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']] # Subset from the DF the columns 

sc_covariance = sc_df.cov().iloc[0,1] # Covariance between Strength and Combat


sc_strength = sc_df['Strength'].std() # Standard Deviation of Strength
sc_combat = sc_df['Combat'].std()# Standard Deviation of Combat

sc_pearson = sc_covariance / (sc_combat * sc_strength ) # Correlation coefficient between Strength and Combat Usig Pearson's Formula


#================================================================================================================


ic_df = data[['Intelligence', 'Combat']]

ic_covariance = ic_df.cov().iloc[0, 1]# Covariance between Intelligence and Combat

ic_intelligence = ic_df['Intelligence'].std()# Standard Deviation of Intelligence
ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance / (ic_combat * ic_intelligence)# Correlation coefficient between Intelligence and Combat Usig Pearson's Formula



# --------------
#Code starts here

total_high = data['Total'].quantile(0.99) # Quantile of column Total

super_best = data[data['Total'] > total_high] # Subset of Data haing the value greater than total_high

super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3)

ax_1.boxplot(data['Intelligence'])

ax_2.boxplot(data['Speed'])

ax_3.boxplot(data['Power'])


