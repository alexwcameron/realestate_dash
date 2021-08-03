import pandas as pd
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

from bokeh.palettes import Spectral5, Spectral3
from bokeh.transform import factor_cmap

import streamlit as st

import math

def total_loans_value():
    DF = pd.read_csv("loans.csv")

    DF['Old'] = DF.Total_New_Loans - DF.Total_First_Loans
    new_old = DF[['date','Old', 'Total_First_Loans']]
    new_old = new_old.set_index('date')
    source = ColumnDataSource(new_old)
    dates = DF['date'].tolist()

    TOOLTIPS = [
        ("First Time Home Buyers", "$@Total_First_Loans{int} million"),
        ("Established Buyers", "$@Old{int} million"),]

    p = figure(x_range=dates, tooltips=TOOLTIPS)

    p.toolbar.logo = None
    p.toolbar_location = None

    p.vbar_stack(stackers=['Total_First_Loans', 'Old'],
                x='date', source=source,
                width=0.5, color=['#EC7063', '#A569BD'],
                legend_label = ['First Home Buyers', 'Other'])

    p.legend.location = 'top_left'

    p.xaxis.axis_label = 'Month'
    p.xgrid.grid_line_color = None	#remove the x grid lines
    p.ygrid.grid_line_color = None	#remove the x grid lines

    p.background_fill_color = "#0E1113"
    p.border_fill_color = "#0E1113"
    p.outline_line_color = "#0E1113"


    p.xaxis.major_label_text_color = "white"
    p.yaxis.major_label_text_color = "white"
    p.xaxis.axis_label_text_color = "white"
    p.yaxis.axis_label_text_color = "white"


    p.yaxis.axis_label = 'Loans in $ Millions'

    p.xaxis.major_label_orientation = math.pi/2

    st.write(p)


def owner_vs_investor():
    DF = pd.read_csv("loans.csv")
    invester_owner = DF[['date','Owner_Occupier', 'Investor']]
    source = ColumnDataSource(invester_owner)
    dates = DF['date'].tolist()

    TOOLTIPS = [
    ("Owner Occupier", "$@Owner_Occupier{int} million"),
    ("Investor", "$@Investor{int} million"),]

    p = figure(x_range=dates, tooltips=TOOLTIPS)

    p.toolbar.logo = None
    p.toolbar_location = None

    p.vbar_stack(stackers=['Owner_Occupier', 'Investor'],
                x='date', source=source,
                width=0.5, color=['#EC7063', '#A569BD'],
            legend_label = ['Owner Occupier', 'Investor'])

    p.legend.location = 'top_left'

    p.xaxis.axis_label = 'Month'
    p.xgrid.grid_line_color = None	#remove the x grid lines
    p.ygrid.grid_line_color = None	#remove the x grid lines

    p.background_fill_color = "#0E1113"
    p.border_fill_color = "#0E1113"
    p.outline_line_color = "#0E1113"


    p.xaxis.major_label_text_color = "white"
    p.yaxis.major_label_text_color = "white"
    p.xaxis.axis_label_text_color = "white"
    p.yaxis.axis_label_text_color = "white"

    p.yaxis.axis_label = 'Loans in $ Millions'

    p.xaxis.major_label_orientation = math.pi/2

    st.write(p)

def first_time_owner_vs_investor(just_investors):
    DF = pd.read_csv("loans.csv")
    invester_owner = DF[['date','First_Owner','First_Investor']]

    source = ColumnDataSource(invester_owner)
    dates = DF['date'].tolist()

    TOOLTIPS = [
    ("Owner Occupier", "$@First_Owner{int} million"),
    ("Investor", "$@First_Investor{int} million"),]

    p = figure(x_range=dates, tooltips=TOOLTIPS)

    p.toolbar.logo = None
    p.toolbar_location = None

    p.vbar_stack(stackers=['First_Owner', 'First_Investor'],
                x='date', source=source,
                width=0.5, color=['#EC7063', '#A569BD'],
            legend_label = ['Owner Occupier', 'Investor'])

    p.legend.location = 'top_left'

    p.xaxis.axis_label = 'Month'
    p.xgrid.grid_line_color = None	#remove the x grid lines
    p.ygrid.grid_line_color = None	#remove the x grid lines

    p.background_fill_color = "#0E1113"
    p.border_fill_color = "#0E1113"
    p.outline_line_color = "#0E1113"


    p.xaxis.major_label_text_color = "white"
    p.yaxis.major_label_text_color = "white"
    p.xaxis.axis_label_text_color = "white"
    p.yaxis.axis_label_text_color = "white"

    p.yaxis.axis_label = 'Loans in $ Millions'

    p.xaxis.major_label_orientation = math.pi/2

    st.write(p)

def first_time_investor():
    DF = pd.read_csv("loans.csv")
    invester_owner = DF[['date','First_Investor']]

    source = ColumnDataSource(invester_owner)
    dates = DF['date'].tolist()

    TOOLTIPS = [
    ("First Time Investor", "$@First_Investor{int} million"),]

    p = figure(x_range=dates, tooltips=TOOLTIPS)

    p.toolbar.logo = None
    p.toolbar_location = None

    p.vbar_stack(stackers=['First_Investor'],
                x='date', source=source,
                width=0.5, color=['#EC7063'],
            legend_label = ['Investor'])

    p.legend.location = 'top_left'

    p.xaxis.axis_label = 'Month'
    p.xgrid.grid_line_color = None	#remove the x grid lines
    p.ygrid.grid_line_color = None	#remove the x grid lines

    p.background_fill_color = "#0E1113"
    p.border_fill_color = "#0E1113"
    p.outline_line_color = "#0E1113"


    p.xaxis.major_label_text_color = "white"
    p.yaxis.major_label_text_color = "white"
    p.xaxis.axis_label_text_color = "white"
    p.yaxis.axis_label_text_color = "white"

    p.yaxis.axis_label = 'Loans in $ Millions'

    p.xaxis.major_label_orientation = math.pi/2

    st.write(p)