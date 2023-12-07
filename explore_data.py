import utils
import explore_air_data
import explore_strokes_data


def process_data(file1, file2):
    # Step 1 upload strokes data 
    columns_for_strokes = [explore_strokes_data.Columns.YEAR, explore_strokes_data.Columns.STATE,
                           explore_strokes_data.Columns.CITY, explore_strokes_data.Columns.NUMBER_OF_CASES,
                           explore_strokes_data.Columns.UNIT]
    key_strokes = explore_strokes_data.Columns.NUMBER_OF_CASES
    selected_value = "per 100,000"
    value_column = explore_strokes_data.Columns.UNIT
    df_strokes = utils.upload_data(file1, columns_for_strokes, key_strokes)
    df_strokes = utils.select_values(df_strokes, value_column, selected_value)
    print(df_strokes)

    # Step 2 Explore strokes data
    strokes_mean_year = explore_strokes_data.explore_strokes(df_strokes, "mean")
    print(strokes_mean_year)

    # Step 3 Upload air data
    columns_for_air = [explore_air_data.Columns.DATE, explore_air_data.Columns.AQI,
                       explore_air_data.Columns.CATEGORY, explore_air_data.Columns.DEF_PARAMETER,
                       explore_air_data.Columns.CITY, explore_air_data.Columns.STATE,
                       explore_air_data.Columns.POPULATION]
    key_air = explore_air_data.Columns.AQI
    df_air = utils.upload_data(file2, columns_for_air, key_air)
    print(df_air)

    # Step 4 Explore air data
    # select years range
    first = 1999
    second = 2020
    df_air = explore_air_data.select_dates(first, second, df_air)
    df_air = utils.select_values(df_air, explore_air_data.Columns.DEF_PARAMETER, "PM2.5")
    # calculate mean
    air_mean_year = explore_air_data.explore_data(df_air, "mean")
    print(air_mean_year)

    return(strokes_mean_year, air_mean_year)
