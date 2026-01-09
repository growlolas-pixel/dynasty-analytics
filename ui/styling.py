import streamlit as st

def apply_base_styles():
    st.markdown(
        """
        <style>
        /* Make the app cleaner and more modern */
        .main {
            padding: 2rem;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #111827;
            color: white;
        }

        /* Sidebar text */
        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Headings */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
