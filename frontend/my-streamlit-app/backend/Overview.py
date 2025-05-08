import streamlit as st
import os


def get_logo_path():
    # Define the base directory relative to this file
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    LOGO_BASE_PATH = os.path.join(BASE_DIR, "Assets/Images/logo.jpg")

    return LOGO_BASE_PATH


def main_overview():
    # --- Page Content ---
    # Wrap content in a div with Tailwind classes - Increased padding
    st.markdown("<div class='bg-gray-100 min-h-screen p-10'>", unsafe_allow_html=True)

    # Centered Logo
    # Adjusted column proportions to give the image more space
    col1, col2, col3 = st.columns(
        [0.5, 2, 0.5]
    )  # Give middle column more relative width
    with col2:
        try:
            # Corrected path relative to Home.py and used use_container_width
            st.image(get_logo_path(), use_container_width=True)
            # Add some space below the logo
            st.markdown("<div class='h-8'></div>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(
                f"Could not load logo. Place it in an accessible location relative to Home.py. Error: {e}"
            )

    # Overview Section - Increased padding, margin, shadow, refined heading border
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>🚀 Overview</h2>
            <p class='text-lg text-gray-700 leading-relaxed'>
                Prometheus is a sophisticated algorithmic trading platform that leverages the
                <a href='https://alpaca.markets/' target='_blank' class='text-blue-600 hover:text-blue-800 hover:underline'>Alpaca Markets API</a>
                to execute automated trading strategies. This project combines advanced data analysis,
                machine learning models, and real-time market data to make informed trading decisions.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Features Section - Updated content
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>✨ Features</h2>
            <div class='grid md:grid-cols-2 gap-8'>
                <div class='bg-gray-50 p-6 rounded-lg shadow-md border border-gray-100'>
                    <h3 class='text-xl font-medium text-gray-800 mb-3'>Real-time Market Data Integration</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600'>
                        <li>Seamless integration with Alpaca Markets API</li>
                        <li>High-frequency data collection with rate limit management</li>
                        <li>Support for multiple timeframes and market data types (IEX, SIP)</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-md border border-gray-100'>
                    <h3 class='text-xl font-medium text-gray-800 mb-3'>Advanced Trading Models</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600'>
                        <li>Machine learning model integration with TensorFlow</li>
                        <li>Custom trading strategies implementation (Simons, Sun Tzu)</li>
                        <li>Research-based approach with separate modules for different strategies</li>
                        <li>Structured model management and evaluation (see <code>Models/</code> directory)</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-md border border-gray-100'>
                    <h3 class='text-xl font-medium text-gray-800 mb-3'>Data Analysis & Visualization</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600'>
                        <li>Comprehensive market data analysis using pandas and numpy</li>
                        <li>Interactive data visualization with matplotlib and Plotly</li>
                        <li>Performance metrics and reporting</li>
                        <li>Historical data analysis and storage for various sources (see <code>Data/</code> directory)</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-md border border-gray-100'>
                    <h3 class='text-xl font-medium text-gray-800 mb-3'>Risk Management</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600'>
                        <li>Position sizing algorithms</li>
                        <li>Stop-loss and take-profit mechanisms</li>
                        <li>Portfolio diversification strategies</li>
                        <li>Risk assessment tools</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-md border border-gray-100'>
                    <h3 class='text-xl font-medium text-gray-800 mb-3'>Interactive Frontend Dashboard</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600'>
                        <li>Streamlit application for monitoring and interaction (see <code>frontend/</code> directory)</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-md border border-gray-100'>
                    <h3 class='text-xl font-medium text-gray-800 mb-3'>Live Trading Capabilities</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600'>
                        <li>Jupyter notebook for live trading execution and monitoring (see <code>Live_Trading/</code> directory)</li>
                    </ul>
                </div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Project Structure Section
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>📊 Project Structure</h2>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto border border-gray-200'><code>Prometheus/
├── Assets/                     # Project assets (e.g., logo)
│   └── Images/
├── Data/                       # Processed and raw market data
│   ├── IEX/                    # Data from IEX feed
│   ├── Regular Hours/          # Data filtered for regular trading hours
│   └── SIP/                    # Data from SIP feed
├── frontend/                   # Streamlit frontend application
│   └── my-streamlit-app/
│       └── Home.py             # Main Streamlit app file
├── Live_Trading/               # Notebooks and scripts for live trading
│   └── Live_Trading.ipynb
├── Models/                     # Trained models, evaluation, and related notebooks
│   ├── IEX/
│   ├── Regular Hours/
│   ├── SIP/
│   └── Table.ipynb
├── Simons/                     # Simons trading strategy
│   ├── backend/                # Backend logic for Simons strategy
│   ├── Images/                 # Images related to Simons strategy
│   ├── Paper/                  # Research paper published on Arxiv
│   ├── Report/                 # Reports and results for Simons
│   └── Settings/               # Configuration for Simons strategy
├── Sun_Tzu/                    # Sun Tzu trading strategy
│   ├── backend/                # Backend logic for Sun Tzu strategy
│   └── research/               # Research for Sun Tzu strategy
├── .venv/                      # Python virtual environment
├── .git/                       # Git version control files
├── .gitignore                  # Specifies intentionally untracked files
├── CITATION.cff                # Citation file for the project
├── LICENSE                     # Project license (MIT)
├── pyproject.toml              # Project build configuration
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── uv.lock                     # Lock file for uv package manager
</code></pre>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Streamlit App Navigation Section
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>🧭 Navigating the Dashboard</h2>
            <p class='text-gray-700 mb-4'>
                This Streamlit application serves as the main interface for interacting with the Prometheus trading platform. Here's a brief guide on its structure and how to use it:
            </p>
            <ul class='list-disc list-inside space-y-3 text-gray-700'>
                <li><strong>Overview (This Page):</strong> You are currently on the Overview page, which provides a general introduction to the project, its features, setup instructions, and how to use different components.</li>
                <li><strong>Top Bar Navigation:</strong> At the top of the application, you'll find a navigation bar. This top bar is the primary way to navigate between different sections or pages of the dashboard. Each page will focus on a specific aspect of the platform, such as:
                    <ul class='list-disc list-inside pl-6 space-y-1 text-gray-600'>
                        <li>Detailed views of trading strategy performance.</li>
                        <li>Market data visualization and analysis tools.</li>
                        <li>Configuration settings for trading parameters.</li>
                        <li>Live trading monitoring (if applicable and enabled).</li>
                    </ul>
                </li>
                <li><strong>Interactive Elements:</strong> Throughout the application, you will encounter various interactive elements like charts, tables, input fields, and buttons. These are designed to allow you to:
                    <ul class='list-disc list-inside pl-6 space-y-1 text-gray-600'>
                        <li>Explore data dynamically.</li>
                        <li>Adjust parameters for analysis or trading models.</li>
                        <li>View real-time updates and logs.</li>
                    </ul>
                </li>
                <li><strong>Data Display:</strong> Key information, such as market data, model predictions, portfolio status, and performance metrics, will be displayed in a clear and organized manner using tables, charts, and text summaries.</li>
                <li><strong>Launching the App:</strong> As mentioned in the 'Usage' section, you can run the Streamlit app using the command:
            </ul>
            <pre class='bg-gray-100 p-3 rounded text-sm overflow-x-auto mt-2 mb-2 border border-gray-200'><code>streamlit run frontend/my-streamlit-app/Home.py</code></pre>
            <p class='text-gray-700 mt-3'>
                Explore the different pages using the top navigation bar to get a comprehensive understanding of the platform's capabilities. Each section is designed to be intuitive, but specific instructions or tooltips may be provided within those pages for more complex functionalities.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Implemented Strategies Section - Increased padding, margin, shadow, refined heading border
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>📈 Implemented Strategies</h2>
            <ul class='list-disc list-inside space-y-3 text-gray-700'>
                <li><strong class='text-gray-800'>Simons Strategy:</strong> An advanced quantitative trading approach.</li>
                <li><strong class='text-gray-800'>Sun Tzu Strategy:</strong> Focuses on tactical market analysis and execution.</li>
            </ul>
            <p class='mt-5 text-sm text-gray-500'>Performance metrics are continuously monitored and updated based on live trading results.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Installation Section - Updated content
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>🛠️ Installation</h2>
            <p class='text-gray-700 mb-4'>Follow these steps to set up the project locally:</p>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4'>
                <li>Clone the repository:</li>
            </ol>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto mt-2 mb-4 border border-gray-200'><code>git clone https://github.com/yourusername/Prometheus.git
    cd Prometheus</code></pre>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4' start='2'>
                <li>Create and activate a virtual environment:</li>
            </ol>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto mt-2 mb-4 border border-gray-200'><code>python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate</code></pre>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4' start='3'>
                <li>Install required dependencies:</li>
            </ol>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto mt-2 mb-4 border border-gray-200'><code>pip install -r requirements.txt</code></pre>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4' start='4'>
                <li>Set up your Alpaca API credentials:
                    <ul class='list-disc list-inside pl-6 space-y-1 text-gray-600'>
                        <li>Create an account at <a href='https://alpaca.markets/' target='_blank' class='text-blue-600 hover:text-blue-800 hover:underline'>Alpaca Markets</a></li>
                        <li>Generate your API keys</li>
                        <li>Configure your credentials in the appropriate configuration files (e.g., within <code>Simons/Settings/</code> or as environment variables)</li>
                    </ul>
                </li>
            </ol>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Usage Example Section - Updated content
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>🚀 Usage</h2>
            <p class='text-gray-700 mb-4'><strong>1. Data Collection and Analysis:</strong></p>
            <p class='text-gray-700 mb-2'>Refer to notebooks within <code>Data/</code> subdirectories or specific strategy research. Example of initializing API connection:</p>
        """,
        unsafe_allow_html=True,
    )

    st.code(
        """
    import alpaca_trade_api as tradeapi

    # Initialize API connection (ensure credentials are set)
    api = tradeapi.REST(
        key_id='YOUR_API_KEY',          # Preferably set via environment variables
        secret_key='YOUR_SECRET_KEY',  # Preferably set via environment variables
        base_url='https://paper-api.alpaca.markets'
    )

    # Example: Fetch market data (for more detailed data handling, see scripts/notebooks in Data/ or strategy research folders)
    # data = api.get_bars('AAPL', '1D', '2024-01-01', '2024-04-15').df
    """,
        language="python",
    )
    st.markdown(
        """
            <p class='text-gray-700 mt-4 mb-4'><strong>2. Running Trading Strategies:</strong></p>
        """,
        unsafe_allow_html=True,
    )
    st.code(
        """
    # Import your preferred strategy module
    from Simons.backend import strategy as simons_strategy
    # or
    from Sun_Tzu.backend import strategy as sun_tzu_strategy

    # Execute the strategy (ensure strategy-specific configurations are set)
    # results = strategy.execute() # Placeholder, actual execution might vary
    """,
        language="python",
    )
    st.markdown(
        """
            <p class='text-gray-700 mt-4 mb-4'><strong>3. Launching the Frontend Dashboard:</strong></p>
            <p class='text-gray-700 mb-2'>Ensure Streamlit is installed (<code>pip install streamlit</code>).</p>
        """,
        unsafe_allow_html=True,
    )
    st.code(
        """
    streamlit run frontend/my-streamlit-app/Home.py
    """,
        language="bash",
    )
    st.markdown(
        """
            <p class='text-gray-700 mt-4 mb-4'><strong>4. Live Trading:</strong></p>
            <p class='text-gray-700'>Open and run cells in <code>Live_Trading/Live_Trading.ipynb</code> after appropriate setup and risk assessment.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Performance Section
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>📈 Performance</h2>
            <p class='text-gray-700 mb-4'>The platform implements multiple trading strategies:</p>
            <ul class='list-disc list-inside space-y-2 text-gray-700'>
                <li><strong>Simons Strategy:</strong> Advanced quantitative trading approach.</li>
                <li><strong>Sun Tzu Strategy:</strong> Tactical market analysis and execution.</li>
            </ul>
            <p class='text-gray-700 mt-4'>Performance metrics are continuously monitored and updated based on live trading results.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Contributing Section - Increased padding, margin, shadow, refined heading border
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-lg rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3'>🤝 Contributing</h2>
            <p class='text-gray-700 mb-4'>Contributions are welcome! Please follow these steps:</p>
            <ol class='list-decimal list-inside space-y-2 text-gray-700'>
                <li>Fork the repository.</li>
                <li>Create your feature branch (`git checkout -b feature/AmazingFeature`).</li>
                <li>Commit your changes (`git commit -m 'Add some AmazingFeature'`).</li>
                <li>Push to the branch (`git push origin feature/AmazingFeature`).</li>
                <li>Open a Pull Request.</li>
            </ol>
            <p class='text-gray-700 mt-5'>For major changes, please open an issue first to discuss what you would like to change.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Footer - Updated content
    st.markdown(
        """
        <footer class='text-center mt-16 py-8 border-t border-gray-300'>
            <p class='text-base text-gray-600 mb-3'>
                This project is licensed under the MIT License - see the <a href='https://github.com/yourusername/Prometheus/blob/main/LICENSE' target='_blank' class='text-blue-600 hover:text-blue-800 hover:underline'>LICENSE</a> file for details.
            </p>
            <p class='text-base text-gray-600 mb-4'>
                Contact: Guilherme Grancho (<a href='mailto:guilhermegrancho@tecnico.ulisboa.pt' class='text-blue-600 hover:text-blue-800 hover:underline'>guilhermegrancho@tecnico.ulisboa.pt</a> / <a href='mailto:guilherme.fernandes25@imperial.ac.uk' class='text-blue-600 hover:text-blue-800 hover:underline'>guilherme.fernandes25@imperial.ac.uk</a>)
                <br>
                Vasco Pereira (<a href='mailto:vasco.serpa.pereira@tecnico.ulisboa.pt' class='text-blue-600 hover:text-blue-800 hover:underline'>vasco.serpa.pereira@tecnico.ulisboa.pt</a>)
            </p>
            <p class='text-sm text-gray-500 mt-4'>
                Acknowledgments: <a href='https://alpaca.markets/' target='_blank' class='text-blue-600 hover:text-blue-800 hover:underline'>Alpaca Markets</a>, Contributors, The open-source community.
            </p>
        </footer>
    """,
        unsafe_allow_html=True,
    )

    # Close the wrapping div
    st.markdown("</div>", unsafe_allow_html=True)
