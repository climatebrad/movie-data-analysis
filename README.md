PROJECT MEMBERS:
- Brad Johnson
- Chau Nguyen

GOALS:
Provide Microsoft with actionable insights on how to start a movie studio.
1. Provide an overview of the competitive landscape
2. Provide information on average movie budgets genre
3. Provide insights on movie-goers most highly rated genres and titles
4. 

RESPONSIBILITIES:
Brad:    
Chau:

FILE SUMMARY:
1. data_cleaning.py
2. split_data_fields.py

# To load the datafis-mod1-project
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
