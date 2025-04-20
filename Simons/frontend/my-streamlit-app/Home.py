import streamlit as st

st.set_page_config(layout="wide")

# Function to load CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_name}. Make sure the file exists.")

# Load the Tailwind CSS file
# Assuming the CSS file is generated and placed correctly in the static folder
local_css("static/css/tailwind.css")

# --- Page Content ---

# Display Logo (Adjust path if necessary)
# Note: Streamlit might require the image to be in a 'static' folder or accessible via URL.
# This relative path might not work depending on how Streamlit serves files.
# Consider copying the logo to the 'static' directory within 'my-streamlit-app'.
try:
    st.image("../../../Assets/Images/logo.jpg", width=700)
except Exception as e:
    st.warning(f"Could not load logo. Place it in an accessible location. Error: {e}")


st.title("Prometheus: Algorithmic Trading Platform")

st.markdown("""
    <div class="text-lg">
    Prometheus is a sophisticated algorithmic trading platform that leverages the
    <a href="https://alpaca.markets/" target="_blank" class="text-blue-600 hover:underline">Alpaca Markets API</a>
    to execute automated trading strategies. This project combines advanced data analysis,
    machine learning models, and real-time market data to make informed trading decisions.
    </div>
""", unsafe_allow_html=True)

st.divider()

st.header("✨ Features")

st.markdown("""
<ul class="list-disc list-inside space-y-2 text-base">
    <li><b>Real-time Market Data Integration:</b>
        <ul class="list-disc list-inside ml-6">
            <li>Seamless integration with Alpaca Markets API</li>
            <li>High-frequency data collection with rate limit management</li>
            <li>Support for multiple timeframes and market data types</li>
        </ul>
    </li>
    <li><b>Advanced Trading Models:</b>
        <ul class="list-disc list-inside ml-6">
            <li>Machine learning model integration with TensorFlow</li>
            <li>Custom trading strategies implementation (Simons, Sun Tzu)</li>
            <li>Research-based approach with separate modules</li>
        </ul>
    </li>
    <li><b>Data Analysis & Visualization:</b>
        <ul class="list-disc list-inside ml-6">
            <li>Comprehensive market data analysis using pandas and numpy</li>
            <li>Interactive data visualization with matplotlib</li>
            <li>Performance metrics and reporting</li>
            <li>Historical data analysis</li>
        </ul>
    </li>
    <li><b>Risk Management:</b>
        <ul class="list-disc list-inside ml-6">
            <li>Position sizing algorithms</li>
            <li>Stop-loss and take-profit mechanisms</li>
            <li>Portfolio diversification strategies</li>
            <li>Risk assessment tools</li>
        </ul>
    </li>
</ul>
""", unsafe_allow_html=True)

st.divider()

st.header("📈 Implemented Strategies")
st.markdown("""
<ul class="list-disc list-inside space-y-1 text-base">
    <li><b>Simons Strategy:</b> An advanced quantitative trading approach.</li>
    <li><b>Sun Tzu Strategy:</b> Focuses on tactical market analysis and execution.</li>
</ul>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
    <p class="text-sm text-gray-600">
        Project licensed under the MIT License.
        Contact: Guilherme Grancho (guilhermegrancho@tecnico.ulisboa.pt), Vasco Pereira (vasco.serpa.pereira@tecnico.ulisboa.pt)
    </p>
""", unsafe_allow_html=True)

# Example of using a Tailwind class (optional, kept for reference)
# st.markdown('<h2 class="text-2xl font-semibold text-green-600 mt-4">Tailwind CSS is integrated!</h2>', unsafe_allow_html=True)
