import streamlit as st

class MultiLeagueManager:
    def __init__(self):
        if "selected_league" not in st.session_state:
            st.session_state["selected_league"] = None

    def select_league(self):
        leagues = ["League A", "League B", "League C"]  # placeholder
        selected = st.selectbox("Select a league:", leagues)
        st.session_state["selected_league"] = selected
        return selected

    def get_current_league(self):
        return st.session_state.get("selected_league", None)
