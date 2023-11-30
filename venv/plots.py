


# this was air
def create_plot(df, city):
    df['date'] = df['Month'].map(str) + '-' + df['Year'].map(str)
    df['date'] = pd.to_datetime(df['date'], format='%m-%Y').dt.strftime('%m-%Y')
    # fig, ax = plt.subplots()
    df = df[df['city_ascii'] == city]
    plt.plot_date(df['date'], df['AQI'], linestyle='dashed')
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.title(city)
    plt.tick_params("x", labelrotation=35)

    return plt.show()

def create_plot_yearly(df, city):
    # df['date'] = df['Month'].map(str) + '-' + df['Year'].map(str)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.strftime('%Y')
    # fig, ax = plt.subplots()
    df = df[df['city_ascii'] == city]
    plt.plot_date(df['Year'], df['AQI'], linestyle='dashed')
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.title(city)
    plt.tick_params("x", labelrotation=35)

    return plt.show()

# create_plot(air_mean_per_month_df, "Albuquerque")
create_plot_yearly(air_mean_per_year_df, "Albuquerque")
# different cities can have the same name. Refactor to city and state instead of city.




