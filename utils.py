import pandas as pd
import utils
from settings import Settings

pd.options.display.max_columns = None


def upload_data(file, columns, key):
    df = utils.upload_csv(file)
    df = utils.set_index(df)
    df = utils.select_columns(df, columns)
    df = utils.drop_na(df, key)
    return df


def upload_csv(file):
    # there are exceptions
    df_name = pd.read_csv(file, header=None, low_memory=False)
    return df_name


# function to set new index
def set_index(df_name):
    df_name.columns = df_name.iloc[0]
    df_name = df_name.drop(0)
    return df_name


# select data we need
def select_columns(df_name, columns_list):
    # add exception
    df_name = df_name[columns_list]
    return df_name


# drop nan values
def drop_na(df_name, column_name):
    df_name = df_name[df_name[f'{column_name}'].notna()]
    return df_name


# join data from several dfs
def join_data(df_fin, df_name):
    df_fin = pd.concat([df_fin, df_name], axis=0)
    return df_fin


def save_data(df_name, directory, file_name):
    df_name.to_csv(f"{Settings.base_path}/{directory}/{file_name}.csv")
    print(f"The data saved to {directory}")
    return


def select_values(df, column_name, value):
    df = df.loc[df[column_name] == value]
    return df
