import streamlit as st
from Overview import main_overview
from Model_Stats import main_model_stats
from Academic_References import main_academic_references
from Predictions import main_predictions
from Portfolio_Management import main_portfolio_management


def main():
    # Set the page configuration
    st.set_page_config(
        layout="wide", page_title="Prometheus - Quant Research", page_icon="🔥"
    )

    # Page Title
    st.title("Prometheus")

    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Overview",
            "Predictions",
            "Portfolio Management",
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
        main_portfolio_management()
        # Add more content specific to the Portfolio Management tab

    with tab4:
        main_model_stats()
        # Stock Selection - Moved inside the Model Stats tab

    with tab5:
        main_academic_references()
        # Add references or links here


if __name__ == "__main__":
    main()
