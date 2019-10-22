PROJECT MEMBERS:
- Brad Johnson
- Chau Nguyen

GOALS:
Provide Microsoft with actionable insights on how to start a movie studio.
1. Provide an overview of the competitive landscape
1. Provide information on average movie budgets genre
1. Provide insights on movie-goers most highly rated genres and titles


RESPONSIBILITIES:
Brad: Data load and cleaning
Chau:

FILE SUMMARY:
1. data_cleaning.py
1. split_data_fields.py
1. movie_data.py

# To load the datafis-mod1-project
FIS project one repo

```
import movie_data as md

rootdir = 'mydata/' # default is 'data/'
df = md.generate_movie_analysis_df(rootdir)
