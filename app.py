import streamlit as st
from ui.styling import apply_base_styles

apply_base_styles()

st.set_page_config(
    page_title="Dynasty Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("🏈 Dynasty Analytics")
st.markdown("Welcome to your Dynasty Analytics platform.")

st.markdown("Use the sidebar to navigate to:")
st.markdown("- Home Dashboard")
st.markdown("- Power Rankings")
st.markdown("- Season Simulation")
