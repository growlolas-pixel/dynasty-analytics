import streamlit as st

st.set_page_config(page_title="Home Dashboard", layout="wide")

st.title("🏈 Home Dashboard")

st.write("This is your main dashboard page. More features will be added here as we build the app.")

import streamlit as st

def render_home():
    st.title("🏠 Home Dashboard")
    st.markdown("Welcome to your Dynasty Analytics platform.")

    st.markdown("### What you can do next:")
    st.markdown("- View Power Rankings")
    st.markdown("- Run Season Simulations")
    st.markdown("- Analyze Trades (coming soon)")
    st.markdown("- Explore Manager Profiles (coming soon)")

render_home()
