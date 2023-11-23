import pandas as pd
import utils
import explore_air_data
import explore_strokes_data
from enum import Enum
from fastapi import FastAPI

pd.options.display.max_columns = None

if __name__ == "__main__":

    # Step 1 upload data
    folder_strokes = "Strokes_data"
    file_list_strokes = ["strokes_2013", "strokes_2014", "strokes_2016"]
    columns_for_strokes = [explore_strokes_data.Columns.YEAR, explore_strokes_data.Columns.STATE,
                           explore_strokes_data.Columns.CITY, explore_strokes_data.Columns.NUMBER_OF_CASES,
                           explore_strokes_data.Columns.UNIT]
    key_strokes = explore_strokes_data.Columns.NUMBER_OF_CASES

    folder_air = "Air_data"
    file_air = "US_AQI"
    columns_for_air = [explore_air_data.Columns.DATE, explore_air_data.Columns.AQI,
                       explore_air_data.Columns.CATEGORY, explore_air_data.Columns.DEF_PARAMETER,
                       explore_air_data.Columns.CITY, explore_air_data.Columns.STATE,
                       explore_air_data.Columns.POPULATION]
    key_air = explore_air_data.Columns.AQI
    
    df_strokes = pd.DataFrame()
    for file in file_list_strokes:
        df = utils.upload_data(folder_strokes, file, columns_for_strokes, key_strokes)
        df_strokes = utils.join_data(df_strokes, df)
    utils.save_data(df_strokes, folder_strokes, "df_strokes")
    print(df_strokes)

    # # Step 3 Explore strokes data
    strokes_mean_year = explore_strokes_data.explore_strokes(df_strokes, "mean")


    df_air = utils.upload_data(folder_air, file_air, columns_for_air, key_air)
    # utils.save_data(df_air, folder_air, "df_air")
    print(df_air)
    # Step 2 Explore air data
    # 2.1 select years range
    first = 1999
    second = 2020
    df_air = explore_air_data.select_dates(first, second, df_air)
    # 2.2 calculate mean
    air_mean_year = explore_air_data.explore_data(df_air, "mean")
    utils.save_data(air_mean_year, "combined", "air_mean_year")
    

    

    