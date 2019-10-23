#!/usr/bin/env python
""" Generate charts for movie project.

USAGE:
import movie_charts as mc
mc.make_genre_boxplot(expand_df,'roi',value_num=13,
                      highlight_list=['Horror'],
                   	  xlabel='Return on Investment',
                      ylabel='Genre',
                      formatx_as_percent=True)
"""
import pandas as pd
import seaborn as sns
from data_cleaning import *

def top_genre_list(dframe,field):
    return dframe[['genre',field]].groupby('genre').median().sort_values(ascending=False,
                                                   by=field).reset_index()

def make_genre_boxplot(data,x,value_num=5,highlight_list=[],**kwargs):
    display = top_genre_list(data, x)
    genre_list = display[:value_num].genre.to_list()
    palette = ['gray']*value_num
    for i in display[display.genre.isin(highlight_list)].index:
        palette[i]='red'
    splot = sns.boxplot(data=data[data['genre'].isin(genre_list)],
                           x=x,
                           y='genre',
                           palette=palette,
                           order=genre_list,
                           showfliers=False)
    if 'xlabel' in kwargs:
        splot.set_xlabel(kwargs['xlabel'], fontsize=20)
    if 'ylabel' in kwargs:
        splot.set_ylabel(kwargs['ylabel'], fontsize=20)
    if 'formatx_as_percent' in kwargs:
        if kwargs['formatx_as_percent']:
            splot.set_xticklabels(['{0:.0%}'.format(x) for x in splot.get_xticks()])
    splot.tick_params(labelsize=20)
    return splot
