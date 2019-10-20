#!/usr/bin/env python
""" Data cleaning utility for movie project.

USAGE:
from data_cleaning import *
dfs = {}
for table_name in TABLE_FORMATS.keys():
    dfs[table_name] = df_from_movie_csv(table_name)
"""
import pandas as pd

FORMAT_DEFAULTS = {
    'suffix':'csv',
    'sep':',',
    'encoding':'utf8'
}

TABLE_FORMATS = {
    'bom.movie_gross':{},
    'imdb.name.basics':{
        'index_col':'nconst',
        'split_fields':['primary_profession', 'known_for_titles']
    },
    'imdb.title.basics':{
        'index_col':'tconst',
        'split_fields':['genres']
    },
    'imdb.title.crew':{
        'index_col':'tconst',
        'split_fields':['directors', 'writers']
    },
    'imdb.title.principals':{
        'index_col':'tconst'
    },
    'imdb.title.ratings':{
        'index_col':'tconst'
    },
    'imdb.title.akas':{
        'index_col':'title_id'
    },
    'rt.movie_info':{
        'suffix':'tsv',
        'sep':'\t',
        'encoding':'ISO-8859-1',
        'index_col':'id',
        'split_fields':['genre', 'director', 'writer'],
        'split_on':'|',
        'date_fields':['theater_date', 'dvd_date']
    },
    'rt.reviews':{
        'index_col':'id',
        'suffix':'tsv',
        'sep':'\t',
        'encoding':'ISO-8859-1',
        'date_fields':['date']
    },
    'tmdb.movies':{
        'index_col':'id',
        'split_fields':['genre_ids'],
        'date_fields':['release_date'],
        'skip_cols':['Unnamed: 0']
    },
    'tn.movie_budgets':{
        'index_col':'id',
        'date_fields':['release_date'],
        'dollar_fields':['production_budget', 'domestic_gross', 'worldwide_gross']
    }
}

def include_col(formats, col):
    """Returns True unless col listed in formats['skip_cols']"""
    if 'skip_cols' not in formats:
        return True
    return col not in set(formats['skip_cols'])

def convert_dollars_to_no(dollars):
    """Converts string in $12, 345.67 format to 12345.67 float"""
    return float(dollars.replace('$', '').replace(',', ''))

def set_read_args(fname):
    """Sets arguments for pd.read_csv() based on FORMAT_DEFAULTS and TABLE_FORMATS"""
    if fname in TABLE_FORMATS:
        f_table = TABLE_FORMATS[fname]
    else:
        return {}

    read_args = {}
    converters = {}

    # set file format
    for arg in ['sep', 'encoding']:
        read_args[arg] = f_table.get(arg, FORMAT_DEFAULTS[arg])

    # set index_col
    if 'index_col' in f_table:
        read_args['index_col'] = f_table['index_col']

    # skip columns listed in 'skip_cols'
    if 'skip_cols' in f_table:
        read_args['usecols'] = lambda x: include_col(f_table, x)

    # parse 'date_fields' to datetime, 'dollar_fields' to float
    if 'date_fields' in f_table:
        read_args['parse_dates'] = f_table['date_fields']
    if 'dollar_fields' in f_table:
        for dollar_field in f_table['dollar_fields']:
            converters[dollar_field] = convert_dollars_to_no
    read_args['converters'] = converters

    return read_args

def set_gz_fpath(fname, rootdir):
    """Sets full filename from fname, rootdir, and suffix"""
    suffix = FORMAT_DEFAULTS['suffix']
    if fname in TABLE_FORMATS:
        suffix = TABLE_FORMATS[fname].get('suffix', suffix)
    return rootdir + fname + '.' + suffix + '.gz'

def df_from_movie_csv(fname, rootdir='data/'):
    """Given fname and rootdir of csv, returns cleaned DataFrame"""
    read_args = set_read_args(fname)
    fpath = set_gz_fpath(fname, rootdir)
    movie_df = pd.read_csv(fpath, **read_args)
    return movie_df
