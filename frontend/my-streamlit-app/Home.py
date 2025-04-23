import os
import sys
import streamlit as st
from backend.Overview import main_overview
from backend.Model_Stats import main_model_stats
from backend.Academic_References import main_academic_references
from backend.Predictions import main_predictions

# Redirect all stderr messages to null
devnull = os.open(os.devnull, os.O_WRONLY)
os.dup2(devnull, sys.stderr.fileno())
os.close(devnull)
# Disable GPU and suppress TF/Absl logs
os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_CPP_MIN_VLOG_LEVEL'] = '3'
os.environ['ABSL_CPP_MIN_LOG_LEVEL'] = '3'

def main():
    # Set the page configuration before any UI elements
    st.set_page_config(layout="wide", page_title="Prometheus - Quant Research", page_icon="🔥")

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
