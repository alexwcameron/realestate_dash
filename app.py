import streamlit as st

import pandas as pd
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

from bokeh.palettes import Spectral5, Spectral3
from bokeh.transform import factor_cmap

import pandas as pd
import math

st.write("Australian Property Prices")

from vizs import total_loans_value, owner_vs_investor, first_time_owner_vs_investor, first_time_investor

page_names = ['All Buyers', 'Established Investors', 'Only First Home Buyers', "First Time Investors"]

page = st.radio("Navigation", page_names)

if page == "All Buyers":
    st.write(total_loans_value())
elif page == "Established Investors":
    st.write(owner_vs_investor())
elif page == "Only First Home Buyers":
    just_investors = False
    first_time_owner_vs_investor(just_investors)
elif page == "First Time Investors":
    just_investors = True
    first_time_investor()

    



 


