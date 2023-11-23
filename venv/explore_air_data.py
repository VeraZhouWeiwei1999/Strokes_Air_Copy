from enum import Enum
import utils
import pandas as pd
from settings import Settings
import matplotlib.pyplot as plt
pd.options.display.max_columns = None

from enum import Enum
class Columns(str, Enum):
    DATE = 'Date'
    AQI = 'AQI'
    CATEGORY = 'Category'
    DEF_PARAMETER = 'Defining Parameter'
    CITY = 'city_ascii'
    STATE = 'state_id'
    POPULATION = 'population'
    YEAR = 'year'
    MONTH = 'month'


def select_dates(f, s, df):
    years = range(f, s, 1)
    df_dates = pd.DataFrame(
        columns=[Columns_air.DATE, Columns_air.AQI, Columns_air.CATEGORY, Columns_air.DEF_PARAMETER, \
                Columns_air.CITY, Columns_air.STATE])
    for year in years:
        start_date = f'{year}-01-01'
        end_date = f'{year}-12-31'
        mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
        df_selected = df.loc[mask]
        df_dates = pd.concat([df_dates, df_selected], ignore_index=True)
    df_dates[Columns_air.DATE] = df_dates[Columns_air.DATE].astype('datetime64[ns]')
    df_dates[Columns_air.YEAR] = df_dates[Columns_air.DATE].dt.year
    df_dates[Columns_air.MONTH] = df_dates[Columns_air.DATE].dt.month
    return df_dates

# write documentation to the function
def explore_data(df, parameter):
    mask = df.groupby([Columns_air.STATE, Columns_air.CITY, Columns_air.YEAR], axis = 0)[Columns_air.AQI]
    select_action = {
        "max": mask.max().to_frame(),
        "min": mask.min().to_frame(),
        "mean": mask.mean().to_frame(),
    }
    df_grouped = select_action.get(parameter, "unknown")
    df_grouped = df_grouped.reset_index()
    return df_grouped
