# fis-mod1-project
FIS project one repo

```
from data_cleaning import df_from_movie_csv, TABLE_FORMATS
from split_data_fields import expand_df_split_fields

dfs = {}
for table_name in TABLE_FORMATS.keys():
    dfs[table_name] = df_from_movie_csv(table_name)
    
dfs_expanded = {}
for table_name in TABLE_FORMATS.keys():
    dfs_expanded[table_name] = expand_df_split_fields(dfs[table_name],table_name)
