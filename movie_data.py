#!/usr/bin/env python
""" Generate clean dataframe for movie project. Uses data_cleaning functions.

USAGE:
import movie_data as md

rootdir = 'mydata/' # default is 'data/'
df = md.generate_movie_analysis_df(rootdir)
"""
import pandas as pd
from data_cleaning import *

def generate_movie_analysis_df(rootdir='data/'):
    """Do the full set of commands to generate our clean dataframe."""

    # import tables into dataframes
    print('Importing tables into dataframes...')
    import_tables = ['imdb.title.basics', 'imdb.title.ratings', 'bom.movie_gross', 'tn.movie_budgets']
    dfs = {}
    for table_name in import_tables:
        dfs[table_name] = df_from_movie_csv(table_name, rootdir)

    # clean dataframes
    print('Cleaning data...')
    for table_name in import_tables:
        dfs[table_name] = clean_movie_df(dfs[table_name], table_name)

    # merge imdb dataframes
    print('Merging IMDB data...')
    imdb_title_ratings_df = dfs['imdb.title.basics'].join(dfs['imdb.title.ratings'])

    # drop duplicates
    print('Deduping IMDB data...')
    imdb_title_ratings_df = select_max_rows_on_key_column(imdb_title_ratings_df,
                                                         key_column='title',
                                                         max_column='numvotes')

    # merge BoxOfficeMojo data
    print('Merging BoxOfficeMojo data...')
    bom_df = dfs['bom.movie_gross']
    bom_df = select_max_rows_on_key_column(bom_df,key_column='title',max_column='domestic_gross')
    imdb_bom_df = join_dfs_on_key_col(imdb_title_ratings_df,bom_df, on='title')

    # merge TheNumbers data
    print('Merging TheNumbers data...')
    tn_df = dfs['tn.movie_budgets']
    dframe = join_dfs_on_key_col(imdb_bom_df.drop(columns=['domestic_gross', 'foreign_gross']),
                                 tn_df,
                                 on=['title', 'year'])

    # create profit and roi columns
    print('Calculating profit and ROI')
    dframe['profit'] = dframe.worldwide_gross - dframe.production_budget
    dframe['roi'] = dframe.profit / dframe.production_budget

    return dframe
