import pandas as pd

# Create the Pandas Series
series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])

# Convert strings to datetime objects
date_objects = pd.to_datetime(series)

# Extract day of month, week number, day of year, and day of week
day_of_month = date_objects.dt.day
week_number = date_objects.dt.week
day_of_year = date_objects.dt.dayofyear
day_of_week = date_objects.dt.dayofweek

# Create a new DataFrame to display the extracted information
date_info_df = pd.DataFrame({
    'Original String': series,
    'Day of Month': day_of_month,
    'Week Number': week_number,
    'Day of Year': day_of_year,
    'Day of Week': day_of_week
})

print(date_info_df)
