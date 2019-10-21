#!/usr/bin/env python
"""Process fields of form 'a,b,c' or 'a|b|c' or '[a,b,c]' into pd.Series / expand into rows"""

import re
import pandas as pd
from data_cleaning import TABLE_FORMATS

# code that does all the steps of splitting a field (genres) and merging it back
# into the original table in multiple rows


def split_line(line, sep):
    """Splits string line of form "[a,b,c]" or "['a','b','c']" or "a,b,c" into a list"""
    if pd.isnull(line): return
    return [st.strip("[']") for st in line.split(sep)]

def multifield_to_list(dframe,split_field, split_on=','):
    """Interpret string-form list in dframe's split_field as a list object"""
    return_df = dframe.copy()
    return_df[split_field] = return_df[split_field].apply(lambda field: split_line(field, split_on))
    return return_df

def multifield_to_col(dframe, index_col, split_field, split_on=','):
    """Given dataframe df, expands split_field of format "val1,val2,val3" to multiple rows"""
    new_field_name = re.sub('s$', '', split_field)
    return dframe[split_field].apply(lambda field: split_line(field, split_on)) \
               .apply(pd.Series) \
               .merge(dframe, left_index=True, right_index=True) \
               .reset_index() \
               .drop([split_field], axis=1) \
               .melt(id_vars=dframe.reset_index().columns.drop(split_field), \
                     value_name=new_field_name) \
               .drop("variable", axis=1) \
               .dropna() \
               .set_index(index_col) \
               .sort_values(by=[index_col, new_field_name])

def df_split_fields_to_lists(dframe, table_name):
    """Use TABLE_FORMATS to interpret split_fields found in df defined for table_name as lists"""
    f_table = TABLE_FORMATS[table_name]
    return_df = dframe.copy()
    if 'split_fields' in f_table:
        split_on = f_table.get('split_on', ',')
        for split_field in f_table['split_fields']:
            return_df = multifield_to_list(return_df, split_field, split_on)

    return return_df

def expand_df_split_fields(dframe, table_name):
    """Use TABLE_FORMATS to expand all split_fields found in df defined for table_name"""
    f_table = TABLE_FORMATS[table_name]
    return_df = dframe.copy()

    if 'split_fields' in f_table:
        index_col = f_table['index_col']
        split_on = f_table.get('split_on', ',')
        for split_field in f_table['split_fields']:
            return_df = multifield_to_col(return_df, index_col, split_field, split_on)

    return return_df
