PROJECT MEMBERS:
- Brad Johnson
- Chau Nguyen

GOALS:
Provide Microsoft with actionable insights on how to start a movie studio.
1. Provide analysis on most financially successful genres (profitable, high ROI)
2. Provide insights on movie-goers most highly rated genres

FILE SUMMARY:

Deliverables
1. index.ipynb
2. mod1_movie_deck.pdf
3. data/movie_data.csv.gz
4. data/movie_data_genre_breakout.csv.gz

Python Module
1. movie_data.py
1. movie_data/chart.py
1. movie_data/clean.py
1. movie_data/split_fields.py

Data cleaning and EDA Notebooks
1. notebooks/generate_clean_dataframe.ipynb
1. notebooks/load_data_tables.ipynb
1. notebooks/split_data_tables.ipynb
1. notebooks/movie_eda.ipynb
1. notebooks/more_movie_eda.ipynb


# To load the datafis-mod1-project
FIS project one repo

```
import movie_data as md

rootdir = 'mydata/' # default is 'data/'
df = md.generate_movie_analysis_df(rootdir)
