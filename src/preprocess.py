'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'], format='%Y-%m-%d')
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    dataframe = dataframe.loc[(dataframe['Date_Plantation'] >= str(start)) & (dataframe['Date_Plantation'] <= str(end+1))]
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    dataframe = dataframe.groupby(["Arrond_Nom", dataframe['Date_Plantation'].dt.year]).size()
    dataframe = pd.DataFrame(dataframe)
    dataframe.columns = ["Counts"]
    dataframe.reset_index(inplace=True)
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'], format='%Y') + pd.offsets.YearEnd(1)
    return dataframe


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    df = yearly_df.pivot(
        index='Arrond_Nom',
        columns='Date_Plantation',
        values='Counts')
    df = df.fillna(0)

    return df


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    # On regroupe le dataframe par arrondissement et par jours chronologiques
    dataframe = dataframe.groupby(["Arrond_Nom", dataframe['Date_Plantation']]).size()

    # On extrait l'arrondissement souhaité de notre dataframe
    dataframe = pd.DataFrame(dataframe.loc[arrond])
    dataframe.columns = ["Counts"]
    
    # On retransforme notre dataframe correctement avec le bon nom de colonnes
    dataframe.reset_index(inplace=True)
    
    # On extrait l'année souhaitée de notre dataframe
    dataframe = dataframe.loc[(dataframe['Date_Plantation'].dt.year == year)]
    
    dataframe = pd.DataFrame(dataframe)
    
    # On ajoute les dates manquantes et on set la valeur correspondante à 0
    start = dataframe['Date_Plantation'].iloc[0].strftime("%Y-%m-%d")
    end = dataframe['Date_Plantation'].iloc[-1].strftime("%Y-%m-%d")
    idx = pd.date_range(start,end)
    dataframe = dataframe.set_index('Date_Plantation').reindex(idx).fillna(0).reset_index()
    
    # On retransforme les valeurs de la colonne "Counts" en entier
    dataframe[['Counts']] = dataframe[['Counts']].astype(int)
    return dataframe
