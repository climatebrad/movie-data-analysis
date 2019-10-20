#!/usr/bin/env python
"""Process fields of form 'a,b,c' or 'a|b|c' or '[a,b,c]' into pd.Series / expand into rows"""

# code that does all the steps of splitting a field (genres) and merging it back
# into the original table in multiple rows

test.genres.apply(lambda x: [str.strip("[']") for str in x.split(",")]) \
           .apply(pd.Series) \
           .merge(test, left_index = True, right_index = True) \
           .reset_index() \
           .drop(["genres"], axis = 1) \
           .melt(id_vars = test.reset_index().columns.drop('genres'), value_name = "genre") \
           .drop("variable", axis = 1) \
           .dropna() \
           .set_index('tconst') \
           .sort_values(by=['tconst','genre'])
