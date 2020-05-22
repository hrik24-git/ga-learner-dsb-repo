# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)




# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis =1 )
#print(banks)
print(banks.isnull().sum())

bank_mode = banks.mode()
print(pd.DataFrame(bank_mode).iloc[0])

banks = banks.fillna(value = pd.DataFrame(bank_mode).iloc[0])
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here
#pd.pivot_table(df,index='Generation',values='Attack',aggfunc='sum')

avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount')
print(avg_loan_amount)

# code ends here



# --------------
# code starts here
# Toatl number of self employed who get the loan
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()['Loan_Status']
#print(loan_approved_se)

# Total number of non self employed who get the loan
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()['Loan_Status']
#print(loan_approved_nse)

total_loan_count = banks['Loan_Status'].count()
#print(total_loan_count)

percentage_se = (loan_approved_se / total_loan_count) * 100
#print(percentage_se)

percentage_nse = (loan_approved_nse / total_loan_count) * 100
#print(percentage_nse)
# code ends here


# --------------
# code starts here
def to_year(x):
    year = x // 12
    return year

loan_term = banks['Loan_Amount_Term'].apply(lambda x: to_year(x))

big_loan_term = loan_term[loan_term >= 25].count()
#print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
print(loan_groupby)

mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


