from enum import Enum
import pandas as pd
pd.options.display.max_columns = None

class Columns(str, Enum):
    YEAR = 'Year'
    STATE = 'LocationAbbr'
    CITY = 'LocationDesc'
    NUMBER_OF_CASES = 'Data_Value'
    UNIT = 'Data_Value_Unit'



# group by year and location
def explore_strokes(df, parameter):
    df[Columns.NUMBER_OF_CASES] = pd.to_numeric(df[Columns.NUMBER_OF_CASES], errors='coerce')
    mask = df.groupby([Columns.YEAR, Columns.STATE, Columns.CITY])[Columns.NUMBER_OF_CASES]
    select_action = {
        "max": mask.max().to_frame(),
        "min": mask.min().to_frame(),
        "mean": mask.mean().to_frame(),
    }
    df = select_action.get(parameter, "unknown")
    df = df.reset_index()
    return df