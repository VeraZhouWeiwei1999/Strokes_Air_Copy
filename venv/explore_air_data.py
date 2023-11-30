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
        columns=[Columns.DATE, Columns.AQI, Columns.CATEGORY, Columns.DEF_PARAMETER, \
                Columns.CITY, Columns.STATE])
    for year in years:
        start_date = f'{year}-01-01'
        end_date = f'{year}-12-31'
        mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
        df_selected = df.loc[mask]
        df_dates = pd.concat([df_dates, df_selected], ignore_index=True)
    df_dates[Columns.DATE] = df_dates[Columns.DATE].astype('datetime64[ns]')
    df_dates[Columns.YEAR] = df_dates[Columns.DATE].dt.year
    df_dates[Columns.MONTH] = df_dates[Columns.DATE].dt.month
    return df_dates

# write documentation to the function
def explore_data(df, parameter):
    mask = df.groupby([Columns.STATE, Columns.CITY, Columns.YEAR], axis = 0)[Columns.AQI]
    select_action = {
        "max": mask.max().to_frame(),
        "min": mask.min().to_frame(),
        "mean": mask.mean().to_frame(),
    }
    df_grouped = select_action.get(parameter, "unknown")
    df_grouped = df_grouped.reset_index()
    return df_grouped
