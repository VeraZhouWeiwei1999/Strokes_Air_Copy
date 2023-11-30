# to be deleted

import pandas as pd
pd.options.display.max_columns = None

def get_data(route):
    df = pd.read_csv(route)
    return df

df_air = get_data("./data for project/combined/air_mean_per_year.csv")
# ,state_id,state_name,city_ascii,Year,AQI
df_strokes = get_data("./data for project/combined/strokes_per_year.csv")
# ,Year,LocationAbbr,LocationDesc,Data_Value

combined_df = df_air.merge(df_strokes, left_on = ['state_id','city_ascii','Year'], right_on=['LocationAbbr', 'LocationDesc', 'Year'], how='left')
combined_df = combined_df.rename({'Data_Value': 'Strokes_mortality'}, axis=1)

def save_data(df_name, directory, name):
    df_name.to_csv{f"{Settings.base_path}{directory}/{name}.csv")
    print(f"The data saved to {directory}")
    return
save_data(combined_df, "combined", "strokes_and_air")
print(combined_df)