import streamlit as st


def load_css():
    """Loads custom CSS inspired by Tailwind for styling."""
    css = r"""
    <style>
        /* General Page Style */
        .stApp > header {
            background-color: transparent; /* Keep header background transparent */
        }
        .stApp {
            background-color: var(--background-color); /* Use theme background */
        }

        /* Main Title */
        h1 {
            font-size: 2rem; /* Slightly larger title */
            font-weight: 700;
            color: var(--text-color);
            padding-bottom: 0.75rem; /* Increased padding */
            border-bottom: 1px solid var(--secondary-background-color); /* Use secondary background for border */
            margin-bottom: 2rem; /* Increased margin */
        }

        /* Introductory text */
        /* Target the specific paragraph more reliably if possible, otherwise use the existing selector */
        .stApp > div:nth-of-type(1) > div:nth-of-type(1) > div > div > div:nth-of-type(2) > p {
            color: var(--text-color);
             font-size: 1.1rem; /* Slightly larger intro text */
             margin-bottom: 2.5rem; /* Increased margin */
            line-height: 1.6;
        }

        /* Paper Container Card Style */
        .paper-container {
            border: 1px solid var(--secondary-background-color); /* Softer border */
            border-radius: 0.75rem; /* Slightly more rounded corners */
            padding: 2rem; /* Increased padding */
            margin-bottom: 2rem; /* Increased margin */
            background-color: var(--secondary-background-color); /* Use theme secondary background */
            box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.05); /* Softer shadow */
            transition: box-shadow 0.3s ease-in-out, transform 0.2s ease-in-out; /* Added transform transition */
        }
        .paper-container:hover {
             box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Enhanced hover shadow */
             transform: translateY(-3px); /* Subtle lift effect on hover */
        }

        /* Paper Subheader (Title) */
        .paper-container h3 {
            font-size: 1.35rem; /* Slightly larger paper title */
            font-weight: 600;
            color: var(--text-color);
            margin-bottom: 1rem; /* Increased margin */
        }

        /* Paper Content Text */
        .paper-container p {
            color: var(--text-color);
            line-height: 1.7; /* Increased line height for readability */
            margin-bottom: 0.75rem; /* Adjusted margin */
            font-size: 1rem; /* Standard text size */
            text-align: justify; /* Added text justification */
        }
        .paper-container p strong {
            color: var(--text-color); /* Ensure strong text uses theme color */
            font-weight: 600;
        }
        .paper-container p em {
             color: var(--text-color); /* Ensure emphasis text uses theme color */
             opacity: 0.9; /* Slightly less prominent */
        }

        /* Authors Layout */
        .authors-container {
            display: flex;
            justify-content: space-between; /* Distribute space between author blocks */
            margin-bottom: 1rem; /* Add some margin below the authors section */
        }
        .author-block {
            flex: 1; /* Allow blocks to grow and shrink as needed */
            padding-right: 1rem; /* Add some padding to the right of each block, except the last */
        }
        .author-block:last-child {
            padding-right: 0; /* No padding for the last block */
        }
        .author-block p {
            margin-bottom: 0.25rem; /* Smaller margin for paragraphs within author block */
            text-align: left; /* Align text to the left for author details */
        }


        /* Links */
        .paper-container a {
            color: var(--primary-color); /* Use theme primary color */
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s ease; /* Smooth color transition */
        }
        .paper-container a:hover {
            text-decoration: underline;
            color: var(--primary-color); /* Keep color, maybe slightly darken/lighten if needed */
            opacity: 0.8; /* Slight fade on hover */
        }

        /* Remove default Streamlit dividers if using containers */
        hr {
            display: none;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def main_academic_references():
    load_css()  # Load the custom CSS

    st.header(
        "Academic References"
    )  # Changed from h1 to header for semantic correctness if needed, but h1 CSS targets it
    st.write(
        "Explore the foundational research papers authored by our team that underpin the methodologies used in this application."
    )

    # Paper 1
    st.markdown(
        """
    <div class="paper-container">
        <h3>1. The Financial Torque Hypothesis: Predicting Short-Term Stock Price Movements Using LSTM Neural Networks</h3>
        <p><strong>Link:</strong> <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5288444" target="_blank">Read the full paper on SSRN</a></p>
        <p><strong>Authors:</strong></p>
        <div class="authors-container">
            <div class="author-block">
                <p><em><a href="https://www.linkedin.com/in/guilhermegrancho/" target="_blank">Guilherme Grancho D. Fernandes</a></em><br>
                Department of Earth Science and Engineering, Imperial College London, London, United Kingdom<br>
                <a href="mailto:guilherme.fernandes25@imperial.ac.uk">guilherme.fernandes25@imperial.ac.uk</a><br>
                Department of Physics, Instituto Superior Técnico, Lisbon, Portugal<br>
                <a href="mailto:guilhermegrancho@tecnico.ulisboa.pt">guilhermegrancho@tecnico.ulisboa.pt</a></p>
            </div>
            <div class="author-block">
                <p><em><a href="https://www.linkedin.com/in/vasco-pereira03/" target="_blank">Vasco V. R. Serpa Pereira</a></em><br>
                Department of Computer Science and Engineering, Instituto Superior Técnico, Lisbon, Portugal<br>
                <a href="mailto:vasco.serpa.pereira@tecnico.ulisboa.pt">vasco.serpa.pereira@tecnico.ulisboa.pt</a></p>
            </div>
        </div>
        <p><strong>Abstract:</strong></p>
        <p><em>This paper introduces the Financial Torque Hypothesis, which asserts that Volume-Weighted Average Price
        and Trade Count are critical indicators for predicting stock price movements. By incorporating these features into a Long
        Short-Term Memory Neural Network, our model achieved over 87% accuracy in predicting stock-price increases over a
        three-hour horizon, based on 21 months of previously unseen test data. We also perform a comprehensive comparative
        analysis of model performance using two datasets: one that spans the entire trading session—pre-market, regular-market
        and after-hours—and one confined to regular-market hours. Our results reveal that models trained on full-session data
        consistently outperform those built on regular-hours-only data, delivering a 15% improvement in predictive accuracy.
        Furthermore, we evaluate and compare three feature normalization techniques—Standard, MinMax, and Robust—against
        non-normalized data. The paper highlights the value of incorporating raw extended-hours data into intraday forecasting
        models and market microstructure indicators to inform more robust, data-driven trading strategies. The results also help
        corroborate the Financial Torque Hypothesis, advancing our understanding of how the distribution of market activity
        across price levels influences subsequent price trends.</em></p>
        <p><strong>How to cite:</strong></p>
        <p><em>Fernandes, Guilherme Grancho Duarte and Pereira, Vasco, The Financial Torque Hypothesis: Predicting Short-Term Stock Price Movements Using LSTM Neural Networks (June 20, 2025). Available at SSRN: https://ssrn.com/abstract=5288444</em></p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Paper 2
    st.markdown(
        """
    <div class="paper-container">
        <h3>2. Integrating The Financial Torque Hypothesis into Advanced Algorithmic Portefolio Management</h3>
        <p><strong>Set to be published in just a few months...</strong></p>
        <p><strong>Authors:</strong></p>
        <div class="authors-container">
            <div class="author-block">
                <p><em><a href="https://www.linkedin.com/in/guilhermegrancho/" target="_blank">Guilherme Grancho D. Fernandes</a></em><br>
                Department of Earth Science and Engineering, Imperial College London, London, United Kingdom<br>
                <a href="mailto:guilherme.fernandes25@imperial.ac.uk">guilherme.fernandes25@imperial.ac.uk</a><br>
                Department of Physics, Instituto Superior Técnico, Lisbon, Portugal<br>
                <a href="mailto:guilhermegrancho@tecnico.ulisboa.pt">guilhermegrancho@tecnico.ulisboa.pt</a></p>
            </div>
            <div class="author-block">
                <p><em><a href="https://www.linkedin.com/in/vasco-pereira03/" target="_blank">Vasco V. R. Serpa Pereira</a></em><br>
                Department of Computer Science and Engineering, Instituto Superior Técnico, Lisbon, Portugal<br>
                <a href="mailto:vasco.serpa.pereira@tecnico.ulisboa.pt">vasco.serpa.pereira@tecnico.ulisboa.pt</a></p>
            </div>
        </div>
        <!--<p><strong>Link:</strong> <a href="#" target="_blank">Link to the paper - *Please provide the actual URL*</a></p>-->
        <!--<p><strong>Abstract:</strong></p>-->
        <!--<p><em>*Please add the abstract here.* This section provides a concise summary of the paper's key findings, methodologies, and conclusions. Understanding the abstract gives a quick overview of the research's scope and significance.</em></p>
        <!--<p><strong>How to cite:</strong></p>-->
        <!--<p><em>*Please add the citation information here (e.g., Authors, Year, Journal/Conference, DOI).* Proper citation allows others to locate the work and give credit to the authors. Example: Smith, J., & Doe, A. (2023). The Financial Torque Hypotheses. Journal of Financial Studies, 15(2), 123-145. doi:10.xxxx/jfs.xxxx</em></p>-->
    </div>
    """,
        unsafe_allow_html=True,
    )


# If running this script directly (optional, for testing)
# if __name__ == "__main__":
#     main_academic_references()
