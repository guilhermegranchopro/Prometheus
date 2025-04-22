import streamlit as st
import os
from backend.Overview import main_overview
from backend.Model_Stats import main_model_stats
from backend.Academic_References import main_academic_references
from backend.Predictions import main_predictions


def load_css():
    css_file = os.path.join(os.path.dirname(__file__), "static/css/tailwind.css")
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    # Set the page configuration (must come before any other Streamlit commands)
    st.set_page_config(
        layout="wide", page_title="Prometheus - Quant Research", page_icon="🔥"
    )
    # Load Tailwind CSS
    load_css()

    # Page Title
    st.title("Prometheus")

    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Overview",
            "Predictions",
            "Model Stats",
            "Academic References",
        ]
    )

    with tab1:
        main_overview()
        # Add more content specific to the Overview tab

    with tab2:
        main_predictions()
        # Add more content specific to the Predictions tab

    with tab3:
        main_model_stats()
        # Stock Selection - Moved inside the Model Stats tab

    with tab4:
        main_academic_references()
        # Add references or links here


if __name__ == "__main__":
    main()
