import pandas as pd


# Reading the input csv file using pandas 
df = pd.read_csv('input_coviddata.csv', usecols = ['date','country','active_cases'])

# Finding the month name and year from the date 
df['date'] = pd.to_datetime(df['date'])
df['Peak'] = df['date'].dt.month_name(locale='English')
df['Year'] = pd.DatetimeIndex(df['date']).year

# Suming all the values based upon the country, monthname and year
df_new = df.groupby(['country','Peak','Year'])['active_cases'].sum().reset_index(name ='Total number of cases reported for the peak month')

# Finding the maximum value using the total number of active cases 
df_new = df_new[df_new.groupby(['country','Year'])['Total number of cases reported for the peak month'].transform('max') == df_new['Total number of cases reported for the peak month']]

# Writing the formed values into cav file
df_new.to_csv('output_covidsurvey.csv', encoding='utf-8', index=False)