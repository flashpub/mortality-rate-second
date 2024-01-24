import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import weibull_min
from scipy.stats import shapiro


# year classifier
def year_classification (year):
    if year < 1970 :
        return "1960-1970"
    elif year < 1980 :
        return "1970-1980"
    elif year < 1990 :
        return "1980-1990"
    elif year < 2000 :
        return "1990-2000"
    elif year < 2010 :
        return "2000-2010"
    elif year < 2020 :
        return "2010-2020"
    else :
        return None
    
# log-linear function
def log_linear_function (x, ln_alpha, beta):
    return ln_alpha + beta * x

# exponential function
def exponential_function(x, a, b):
    return a * np.exp(b * x)

#check distribution and compare genders functions 
def test_distribution_and_compare_sexes(data, value_column, group_column, alpha=0.05):
    
    # Extract the specific column for testing
    data_to_test = data[value_column]
    
    # Perform the Shapiro-Wilk test on the original data
    stat, p = stats.shapiro(data_to_test)
    
    print(f'Shapiro-Wilk test p-value for {value_column}: {p}')

    if p > alpha:
        print(f'{value_column} is normally distributed.')
        
        # Perform a t-test for the difference between sexes
        group_male = data[data[group_column] == 'Male'][value_column]
        group_female = data[data[group_column] == 'Female'][value_column]
        
        t_stat, t_p_value = stats.ttest_ind(group_male, group_female)
        print("T-test for Men and Women:")
        print("T-statistic:", t_stat)
        print("p-value:", t_p_value)
        
        if t_p_value < alpha:
            print("Conclusion: There is a significant difference between Men and Women.")
        else:
            print("Conclusion: There is no significant difference between Men and Women.")
            
    else:
        # Transform the data using the natural logarithm
        log_data = np.log(data_to_test)
        
        # Perform the Shapiro-Wilk test on the log-transformed data
        log_stat, log_p = stats.shapiro(log_data)
        print(f'Shapiro-Wilk test p-value for log-transformed {value_column}: {log_p}')

        if log_p > alpha:
            print(f'Log-transformed {value_column} is approximately normally distributed.')
            
            # Plot a histogram of the initial variable when distribution is log-normal
            plt.figure(dpi = 480)
            plt.hist(data_to_test, bins=20, color='blue', alpha=0.7)
            plt.title(f'Histogram of {value_column}')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.show()
            
            # Perform a t-test for the difference between sexes on the log-transformed data
            group_male_log = log_data[data[group_column] == 'Male']
            group_female_log = log_data[data[group_column] == 'Female']
        
            t_stat_log, t_p_value_log = stats.ttest_ind(group_male_log, group_female_log)
            print("T-test for Men and Women on log-transformed data:")
            print("T-statistic:", t_stat_log)
            print("p-value:", t_p_value_log)
        
            if t_p_value_log < alpha:
                print("Conclusion: There is a significant difference between Men and Women on log-transformed data.")
            else:
                print("Conclusion: There is no significant difference between Men and Women on log-transformed data.")
        else:
            print(f'Log-transformed {value_column} is also not normally distributed.')
            
            # Plot a histogram of the initial variable when non-normal
            plt.figure(dpi = 480)
            plt.hist(data_to_test, bins=20, color='blue', alpha=0.7)
            plt.title(f'Histogram of {value_column}')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.show()
            
            # Perform a Mann-Whitney U-test for the difference between sexes on the initial data
            group_male = data[data[group_column] == 'Male'][value_column]
            group_female = data[data[group_column] == 'Female'][value_column]
        
            mw_stat, mw_p_value = stats.mannwhitneyu(group_male, group_female, alternative='two-sided')
        
            print(f"Mann-Whitney U-test for Men and Women on {value_column}:")
            print("Statistic:", mw_stat)
            print("p-value:", mw_p_value)
        
            if mw_p_value < alpha:
                print("Conclusion: There is a significant difference between Men and Women.")
            else:
                print("Conclusion: There is no significant difference between Men and Women.")



def calculate_statistics(data, age_groups):
    
    grouped_data = data[data['Age Group'].isin(age_groups)].groupby('Age Group')
    
    mean_values = grouped_data['Death rate per 100 000 population'].mean()
    max_values = grouped_data['Death rate per 100 000 population'].max()
    min_values = grouped_data['Death rate per 100 000 population'].min()
    std_values = grouped_data['Death rate per 100 000 population'].std()
    
    return mean_values, max_values, min_values,std_values