import streamlit as st
from ui.styling import apply_base_styles
from views import home, power_rankings, season_sim

# Base styles
apply_base_styles()

# Page config
st.set_page_config(
    page_title="Dynasty Analytics",
    page_icon="📊",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Dynasty Analytics")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Power Rankings", "Season Simulation"]
)

# Routing
if page == "Home":
    home.render()
elif page == "Power Rankings":
    power_rankings.render()
elif page == "Season Simulation":
    season_sim.render()
