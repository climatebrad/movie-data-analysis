#!/usr/bin/env python
""" Generate clean dataframe for movie project. Uses data_cleaning functions.

USAGE:
import movie_data as md

rootdir = 'mydata/' # default is 'data/'
dframe = md.generate_movie_analysis_df(rootdir)
"""
import pandas as pd
from data_cleaning import *

def generate_movie_analysis_df(rootdir='data/',sources=['tn']):
    """Do the full set of commands to generate our clean dataframe.
Arguments:
    rootdir : where the csv.gz files live (default = 'data/')
    sources : list of sources in addition to IMDB data to use,
              can be 'tn', 'bom' (default = ['tn']"""

    # import tables into dataframes
    print('Importing tables into dataframes...')
    import_tables = ['imdb.title.basics', 'imdb.title.ratings']
    for source in sources:
        if source == 'bom':
            import_tables.append('bom.movie_gross')
        elif source == 'tn':
            import_tables.append('tn.movie_budgets')

    dfs = {}
    for table_name in import_tables:
        dfs[table_name] = df_from_movie_csv(table_name, rootdir)

    # clean dataframes
    print('Cleaning data...')
    for table_name in import_tables:
        dfs[table_name] = clean_movie_df(dfs[table_name], table_name)

    # merge imdb dataframes
    print('Merging IMDB data...')
    dframe = dfs['imdb.title.basics'].join(dfs['imdb.title.ratings'])

    # drop duplicates
    print('Deduping IMDB data...')
    dframe = select_max_rows_on_key_column( dframe,
                                       key_column='title',
                                       max_column='numvotes')

    if 'bom.movie_gross' in dfs:
        # merge BoxOfficeMojo data
        print('Merging BoxOfficeMojo data...')
        bom_df = dfs['bom.movie_gross']
        bom_df = select_max_rows_on_key_column(bom_df,
                                               key_column='title',
                                               max_column='domestic_gross')
        dframe = join_dfs_on_key_col(dframe, bom_df, on='title')

    if 'tn.movie_budgets' in dfs:
        # merge TheNumbers data
        print('Merging TheNumbers data...')
        tn_df = dfs['tn.movie_budgets']
        dframe = join_dfs_on_key_col(dframe.drop(columns=['domestic_gross', 'foreign_gross'],
                                                 errors='ignore'),
                                 tn_df,
                                 on='title')

        # create profit and roi columns
        print('Calculating profit and ROI')
        dframe['profit'] = dframe.worldwide_gross - dframe.production_budget
        dframe['roi'] = dframe.profit / dframe.production_budget

    return dframe
