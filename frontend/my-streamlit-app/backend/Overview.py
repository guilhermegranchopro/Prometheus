import streamlit as st

def main_overview():
    # --- Page Content ---
    # Wrap content in a div with Tailwind classes
    st.markdown("<div class='bg-gray-100 min-h-screen p-8'>", unsafe_allow_html=True)

    # Centered Logo
    # Adjusted column proportions to give the image more space
    col1, col2, col3 = st.columns(
        [0.5, 2, 0.5]
    )  # Give middle column more relative width
    with col2:
        try:
            # Corrected path relative to Home.py and used use_container_width
            st.image("../../Assets/Images/logo.jpg", use_container_width=True)
        except Exception as e:
            st.warning(
                f"Could not load logo. Place it in an accessible location relative to Home.py. Error: {e}"
            )

    st.markdown(
        """
        <div class='container mx-auto px-4 py-6 bg-white shadow-md rounded-lg mb-8'>
            <h2 class='text-2xl font-semibold text-gray-700 mb-4 border-b pb-2'>🚀 Overview</h2>
            <p class='text-lg text-gray-600 leading-relaxed'>
                Prometheus is a sophisticated algorithmic trading platform that leverages the
                <a href='https://alpaca.markets/' target='_blank' class='text-blue-600 hover:text-blue-800 hover:underline'>Alpaca Markets API</a>
                to execute automated trading strategies. This project combines advanced data analysis,
                machine learning models, and real-time market data to make informed trading decisions.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='container mx-auto px-4 py-6 bg-white shadow-md rounded-lg mb-8'>
            <h2 class='text-2xl font-semibold text-gray-700 mb-4 border-b pb-2'>✨ Features</h2>
            <div class='grid md:grid-cols-2 gap-6'>
                <div class='bg-gray-50 p-4 rounded-lg shadow-sm'>
                    <h3 class='text-xl font-medium text-gray-800 mb-2'>Real-time Market Data Integration</h3>
                    <ul class='list-disc list-inside space-y-1 text-gray-600'>
                        <li>Seamless integration with Alpaca Markets API</li>
                        <li>High-frequency data collection with rate limit management</li>
                        <li>Support for multiple timeframes and market data types</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-4 rounded-lg shadow-sm'>
                    <h3 class='text-xl font-medium text-gray-800 mb-2'>Advanced Trading Models</h3>
                    <ul class='list-disc list-inside space-y-1 text-gray-600'>
                        <li>Machine learning model integration with TensorFlow</li>
                        <li>Custom trading strategies implementation (Simons, Sun Tzu)</li>
                        <li>Research-based approach with separate modules</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-4 rounded-lg shadow-sm'>
                    <h3 class='text-xl font-medium text-gray-800 mb-2'>Data Analysis & Visualization</h3>
                    <ul class='list-disc list-inside space-y-1 text-gray-600'>
                        <li>Comprehensive market data analysis using pandas and numpy</li>
                        <li>Interactive data visualization with matplotlib</li>
                        <li>Performance metrics and reporting</li>
                        <li>Historical data analysis</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-4 rounded-lg shadow-sm'>
                    <h3 class='text-xl font-medium text-gray-800 mb-2'>Risk Management</h3>
                    <ul class='list-disc list-inside space-y-1 text-gray-600'>
                        <li>Position sizing algorithms</li>
                        <li>Stop-loss and take-profit mechanisms</li>
                        <li>Portfolio diversification strategies</li>
                        <li>Risk assessment tools</li>
                    </ul>
                </div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='container mx-auto px-4 py-6 bg-white shadow-md rounded-lg mb-8'>
            <h2 class='text-2xl font-semibold text-gray-700 mb-4 border-b pb-2'>📈 Implemented Strategies</h2>
            <ul class='list-disc list-inside space-y-2 text-gray-600'>
                <li><strong class='text-gray-800'>Simons Strategy:</strong> An advanced quantitative trading approach.</li>
                <li><strong class='text-gray-800'>Sun Tzu Strategy:</strong> Focuses on tactical market analysis and execution.</li>
            </ul>
            <p class='mt-4 text-sm text-gray-500'>Performance metrics are continuously monitored and updated based on live trading results.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='container mx-auto px-4 py-6 bg-white shadow-md rounded-lg mb-8'>
            <h2 class='text-2xl font-semibold text-gray-700 mb-4 border-b pb-2'>🛠️ Installation</h2>
            <p class='text-gray-600 mb-4'>Follow these steps to set up the project locally:</p>
            <ol class='list-decimal list-inside space-y-2 text-gray-600 mb-4'>
                <li>Clone the repository:</li>
            </ol>
            <pre class='bg-gray-100 p-3 rounded text-sm overflow-x-auto mt-2 mb-4'><code>git clone https://github.com/yourusername/Prometheus.git
    cd Prometheus</code></pre>
            <ol class='list-decimal list-inside space-y-2 text-gray-600 mb-4' start='2'>
                <li>Create and activate a virtual environment:</li>
            </ol>
            <pre class='bg-gray-100 p-3 rounded text-sm overflow-x-auto mt-2 mb-4'><code>python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate</code></pre>
            <ol class='list-decimal list-inside space-y-2 text-gray-600 mb-4' start='3'>
                <li>Install required dependencies:</li>
            </ol>
            <pre class='bg-gray-100 p-3 rounded text-sm overflow-x-auto mt-2 mb-4'><code>pip install -r requirements.txt</code></pre>
            <ol class='list-decimal list-inside space-y-2 text-gray-600 mb-4' start='4'>
                <li>Set up your Alpaca API credentials (refer to project configuration).</li>
            </ol>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='container mx-auto px-4 py-6 bg-white shadow-md rounded-lg mb-8'>
            <h2 class='text-2xl font-semibold text-gray-700 mb-4 border-b pb-2'>🚀 Usage Example</h2>
            <p class='text-gray-600 mb-4'>Basic example of fetching market data using the Alpaca API:</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Use st.code for better code display
    st.code(
        """
    import alpaca_trade_api as tradeapi

    # Initialize API connection (replace with your actual keys)
    api = tradeapi.REST(
        key_id='YOUR_API_KEY',
        secret_key='YOUR_SECRET_KEY',
        base_url='https://paper-api.alpaca.markets' # Use paper trading endpoint for testing
    )

    # Fetch market data for Apple (AAPL)
    try:
        data = api.get_bars('AAPL', '1D', '2024-01-01', '2024-04-15').df
        # Example: Print the first few rows
        # print(data.head())
    except Exception as e:
        print(f"Error fetching data: {e}") # Use print or logging in actual script
    """,
        language="python",
    )

    st.markdown(
        """
        <div class='container mx-auto px-4 py-6 bg-white shadow-md rounded-lg mb-8'>
            <p class='text-gray-600 mt-4'>To run specific trading strategies, import and execute the respective modules from the `Simons/backend` or `Sun_Tzu/backend` directories.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='container mx-auto px-4 py-6 bg-white shadow-md rounded-lg mb-8'>
            <h2 class='text-2xl font-semibold text-gray-700 mb-4 border-b pb-2'>🤝 Contributing</h2>
            <p class='text-gray-600 mb-4'>Contributions are welcome! Please follow these steps:</p>
            <ol class='list-decimal list-inside space-y-1 text-gray-600'>
                <li>Fork the repository.</li>
                <li>Create your feature branch (`git checkout -b feature/AmazingFeature`).</li>
                <li>Commit your changes (`git commit -m 'Add some AmazingFeature'`).</li>
                <li>Push to the branch (`git push origin feature/AmazingFeature`).</li>
                <li>Open a Pull Request.</li>
            </ol>
            <p class='text-gray-600 mt-4'>For major changes, please open an issue first to discuss what you would like to change.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <footer class='text-center mt-10 py-6 border-t border-gray-200'>
            <p class='text-sm text-gray-500 mb-2'>
                Project licensed under the MIT License. See LICENSE file for details.
            </p>
            <p class='text-sm text-gray-500'>
                Contact: Guilherme Grancho (guilhermegrancho@tecnico.ulisboa.pt) | Vasco Pereira (vasco.serpa.pereira@tecnico.ulisboa.pt)
            </p>
            <p class='text-xs text-gray-400 mt-4'>
                Acknowledgments: Alpaca Markets, Contributors, Open-Source Community
            </p>
        </footer>
    """,
        unsafe_allow_html=True,
    )

    # Close the wrapping div
    st.markdown("</div>", unsafe_allow_html=True)
