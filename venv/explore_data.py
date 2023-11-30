import pandas as pd
import utils
import explore_air_data
import explore_strokes_data
from enum import Enum

# Step 1 upload strokes data strokes
folder_strokes = "Strokes_data_new"
file = "heart_disease"
columns_for_strokes = [explore_strokes_data.Columns.YEAR, explore_strokes_data.Columns.STATE,
                       explore_strokes_data.Columns.CITY, explore_strokes_data.Columns.NUMBER_OF_CASES,
                       explore_strokes_data.Columns.UNIT]
key_strokes = explore_strokes_data.Columns.NUMBER_OF_CASES
selected_value = "per 100,000"
value_column = explore_strokes_data.Columns.UNIT

df_strokes = utils.upload_data(folder_strokes, file, columns_for_strokes, key_strokes)
print(df_strokes)
# select values unit
df_strokes = utils.select_values(df_strokes, value_column, selected_value)
print(df_strokes)
utils.save_data(df_strokes, folder_strokes, "df_strokes")
print(df_strokes)

# Step 2 Explore strokes data
strokes_mean_year = explore_strokes_data.explore_strokes(df_strokes)

# Step 3 Upload air data
folder_air = "Air_data"
file_air = "US_AQI"
columns_for_air = [explore_air_data.Columns.DATE, explore_air_data.Columns.AQI,
                   explore_air_data.Columns.CATEGORY, explore_air_data.Columns.DEF_PARAMETER,
                   explore_air_data.Columns.CITY, explore_air_data.Columns.STATE,
                   explore_air_data.Columns.POPULATION]
key_air = explore_air_data.Columns.AQI
df_air = utils.upload_data(folder_air, file_air, columns_for_air, key_air)
utils.save_data(df_air, folder_air, "df_air")
print(df_air)

# Step 4 Explore air data
# select years range
first = 1999
second = 2020
df_air = explore_air_data.select_dates(first, second, df_air)
# calculate mean
air_mean_year = explore_air_data.explore_data(df_air, "max")