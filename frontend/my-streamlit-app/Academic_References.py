import streamlit as st

def load_css():
    """Loads custom CSS inspired by Tailwind for styling."""
    css = r"""
    <style>
        /* General Page Style */
        .stApp > header {
            background-color: transparent;
        }
        .stApp {
            background-color: #f9fafb; /* Tailwind gray-50 */
        }

        /* Main Title */
        h1 {
            font-size: 1.875rem; /* text-3xl */
            font-weight: 700; /* font-bold */
            color: #111827; /* gray-900 */
            padding-bottom: 0.5rem; /* pb-2 */
            border-bottom: 1px solid #d1d5db; /* border-b border-gray-300 */
            margin-bottom: 1.5rem; /* mb-6 */
        }

        /* Introductory text */
        .stApp > div:nth-of-type(1) > div:nth-of-type(1) > div > div > div:nth-of-type(2) > p {
             color: #4b5563; /* gray-600 */
             font-size: 1rem; /* text-base */
             margin-bottom: 2rem; /* mb-8 */
        }

        /* Paper Container Card Style */
        .paper-container {
            border: 1px solid #e5e7eb; /* gray-200 */
            border-radius: 0.5rem; /* rounded-lg */
            padding: 1.5rem; /* p-6 */
            margin-bottom: 1.5rem; /* mb-6 */
            background-color: #ffffff; /* bg-white */
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1); /* shadow-lg */
            transition: box-shadow 0.3s ease-in-out;
        }
        .paper-container:hover {
             box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1); /* shadow-xl */
        }

        /* Paper Subheader (Title) */
        .paper-container h3 {
            font-size: 1.25rem; /* text-xl */
            font-weight: 600; /* font-semibold */
            color: #1f2937; /* gray-800 */
            margin-bottom: 0.75rem; /* mb-3 */
        }

        /* Paper Content Text */
        .paper-container p {
            color: #374151; /* gray-700 */
            line-height: 1.625; /* leading-relaxed */
            margin-bottom: 0.5rem; /* mb-2 */
        }
        .paper-container p strong {
            color: #111827; /* gray-900 */
            font-weight: 600;
        }

        /* Links */
        .paper-container a {
            color: #2563eb; /* blue-600 */
            text-decoration: none;
            font-weight: 500;
        }
        .paper-container a:hover {
            text-decoration: underline;
            color: #1d4ed8; /* blue-700 */
        }

        /* Remove default Streamlit dividers if using containers */
        hr {
            display: none;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def main_academic_references():
    load_css() # Load the custom CSS

    st.header("Academic References")
    st.write(
        "Explore the foundational research papers authored by our team that underpin the methodologies used in this application."
    )

    # Paper 1
    st.markdown("""
    <div class="paper-container">
        <h3>1. The Financial Torque Hypotheses</h3>
        <p><strong>Link:</strong> <a href="#" target="_blank">Link to the paper - *Please provide the actual URL*</a></p>
        <p><strong>Abstract:</strong></p>
        <p><em>*Please add the abstract here.* This section provides a concise summary of the paper's key findings, methodologies, and conclusions. Understanding the abstract gives a quick overview of the research's scope and significance.</em></p>
        <p><strong>How to cite:</strong></p>
        <p><em>*Please add the citation information here (e.g., Authors, Year, Journal/Conference, DOI).* Proper citation allows others to locate the work and give credit to the authors. Example: Smith, J., & Doe, A. (2023). The Financial Torque Hypotheses. Journal of Financial Studies, 15(2), 123-145. doi:10.xxxx/jfs.xxxx</em></p>
    </div>
    """, unsafe_allow_html=True)

    # Paper 2
    st.markdown("""
    <div class="paper-container">
        <h3>2. High-Frequency Portfolio Algorithmic Portfolio Management</h3>
        <p><strong>Link:</strong> <a href="#" target="_blank">Link to the paper - *Please provide the actual URL*</a></p>
        <p><strong>Abstract:</strong></p>
        <p><em>*Please add the abstract here.* This abstract details the approaches and results related to managing portfolios algorithmically using high-frequency data, highlighting the techniques and performance metrics discussed in the paper.</em></p>
        <p><strong>How to cite:</strong></p>
        <p><em>*Please add the citation information here (e.g., Authors, Year, Journal/Conference, DOI).* Example: Johnson, R., & Williams, L. (2024). High-Frequency Algorithmic Portfolio Management. Proceedings of the International Conference on Quantitative Finance, 78-92.</em></p>
    </div>
    """, unsafe_allow_html=True)

# If running this script directly (optional, for testing)
# if __name__ == "__main__":
#     main_academic_references()
