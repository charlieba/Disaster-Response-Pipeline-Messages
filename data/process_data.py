import sys
import pandas as pd 
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):  
    '''
    Function for load 2 dataset and merge in one by id
    Args:   messages_filepath: messages.csv file path
            categories_filepath: categories.csv file path
    Returns: A data frame that include both datasets merged
    '''
    
    # load messages dataset
    messages = pd.read_csv(messages_filepath) 
    
    # load categories dataset
    categories = pd.read_csv(categories_filepath) 
    
    # merge datasets
    df = pd.merge(messages,categories,on='id')
    
    return df


def clean_data(df):
    '''
    Function for clean data, splitting the categories, renaming a head for each column and dropping duplicates.
    Args:    df: dataframe to clean. This dataframe must be the messages.csv and categories.csv merged by id. 
    Returns: A data frame cleaned
    '''
    # create a dataframe of the 36 individual category columns
    categories = df["categories"].str.split(";", expand=True)
    
    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = [x.split('-')[0] for x in row.values]
    
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])
       
    # drop the original categories column from `df`
    df = df.drop(columns = ["categories"])
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
   
    # drop duplicates
    df = df.drop_duplicates(keep='last')

    return df


def save_data(df, database_filename):
    '''
    Function that take a dataframe and save the dataframe into a sql lite database. 
    Args:    database_filename: file name and path for the database.  
    Returns: The function does not return nothing, just save the dataframe 
    '''
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('Messages_transformed', engine, if_exists='replace', index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()