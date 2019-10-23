PROJECT MEMBERS:
- Brad Johnson
- Chau Nguyen

GOALS:
Provide Microsoft with actionable insights on how to start a movie studio.
1. Provide analysis on most financially successful genres (profitable, high ROI)
2. Provide insights on movie-goers most highly rated genres

FILE SUMMARY:

Data Cleaning
1. data_cleaning.py
2. generate_clean_dataframe.ipynb
3. load_data_tables.ipynb
4. split_data_fields.py
5. split_data_tables.ipynb

EDA
1. movie_charts.py
2. movie_data.py
3. eda_cn.ipynb
4. movie_eda.ipynb

Final Files
1. data_charting.ipynb
2. mod1_movie_deck.pdf
3. data/movie_data.csv.gz
4. data/movie_data_genre_breakout.csv.gz

# To load the datafis-mod1-project
FIS project one repo

```
import movie_data as md

rootdir = 'mydata/' # default is 'data/'
df = md.generate_movie_analysis_df(rootdir)
