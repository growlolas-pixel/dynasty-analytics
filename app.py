import streamlit as st

st.set_page_config(page_title="Dynasty Analytics", layout="wide")

st.title("🏈 Dynasty Analytics Platform")

st.write("Welcome to your Dynasty Analytics App. Use the sidebar to navigate.")

import streamlit as st
from multi_league_manager import MultiLeagueManager
from ui.styling import apply_base_styles

# Apply base styles
apply_base_styles()

# Page config
st.set_page_config(
    page_title="Dynasty Analytics",
    page_icon="📊",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Dynasty Analytics")
st.sidebar.markdown("---")

# League selector
league_manager = MultiLeagueManager()
selected_league = league_manager.select_league()

st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigate",
    ["Home Dashboard", "Power Rankings", "Season Simulation"]
)

# Page routing
if page == "Home Dashboard":
    st.switch_page("pages/home_dashboard.py")
elif page == "Power Rankings":
    st.switch_page("pages/power_rankings.py")
elif page == "Season Simulation":
    st.switch_page("pages/season_simulation.py")
