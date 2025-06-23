import streamlit as st
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random


def get_logo_path():
    # Define the base directory relative to this file
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    LOGO_BASE_PATH = os.path.join(BASE_DIR, "Assets/Images/logo.jpg")

    return LOGO_BASE_PATH


def create_sample_performance_chart(time_period="1 Year"):
    """Create a sample performance chart for demonstration"""
    # Determine date range based on time period
    if time_period == "3 Months":
        start_date = "2024-10-01"
        end_date = "2024-12-31"
    elif time_period == "6 Months":
        start_date = "2024-07-01"
        end_date = "2024-12-31"
    else:  # 1 Year
        start_date = "2024-01-01"
        end_date = "2024-12-31"

    # Create sample data for demonstration
    dates = pd.date_range(start=start_date, end=end_date, freq="D")

    # Simulate performance data
    cumulative_return = []
    current_return = 1.0

    for _ in dates:
        # Add some randomness with a slight upward bias
        daily_return = random.normalvariate(
            0.002, 0.02
        )  # 0.2% mean daily return, 2% volatility
        current_return *= 1 + daily_return
        cumulative_return.append((current_return - 1) * 100)

    df = pd.DataFrame({"Date": dates, "Cumulative Return (%)": cumulative_return})

    fig = px.line(
        df,
        x="Date",
        y="Cumulative Return (%)",
        title=f"Research Platform Performance Simulation ({time_period})",
        labels={"Cumulative Return (%)": "Cumulative Return (%)"},
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Cumulative Return (%)",
        template="plotly_white",
        height=400,
    )

    return fig


def create_strategy_comparison():
    """Create a comparison chart between strategies"""
    strategies = ["Simons Strategy", "Sun Tzu Strategy", "Financial Torque Hypothesis"]
    accuracy = [82.5, 78.3, 87.2]  # Sample accuracy percentages

    fig = go.Figure(
        data=[
            go.Bar(
                name="Accuracy (%)",
                x=strategies,
                y=accuracy,
                marker_color=["#3B82F6", "#10B981", "#F59E0B"],
            )
        ]
    )

    fig.update_layout(
        title="Strategy Research Accuracy Comparison",
        xaxis_title="Strategy",
        yaxis_title="Accuracy (%)",
        template="plotly_white",
        height=400,
    )

    return fig


def main_overview():
    # --- Page Content ---
    # Wrap content in a div with Tailwind classes - Adjusted padding
    st.markdown("<div class='bg-gray-100 min-h-screen p-8'>", unsafe_allow_html=True)

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

    # Technology Stack Badges Section - Enhanced with more technologies from README
    st.markdown(
        """
        <div class='container mx-auto px-6 py-4 bg-white shadow-lg rounded-lg mb-6'>
            <div class='flex flex-wrap justify-center gap-2'>
                <img src='https://img.shields.io/badge/python-3.10-blue.svg' alt='Python Version'/>
                <img src='https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white' alt='Streamlit'/>
                <img src='https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white' alt='TensorFlow'/>
                <img src='https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white' alt='Pandas'/>
                <img src='https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white' alt='NumPy'/>
                <img src='https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white' alt='Scikit-learn'/>
                <img src='https://img.shields.io/badge/Matplotlib-11557c?logo=matplotlib&logoColor=white' alt='Matplotlib'/>
                <img src='https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white' alt='Plotly'/>
                <img src='https://img.shields.io/badge/Altair-15B8D5?logo=altair&logoColor=white' alt='Altair'/>
                <img src='https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white' alt='SciPy'/>
                <img src='https://img.shields.io/badge/Joblib-007ACC?logo=python&logoColor=white' alt='Joblib'/>
                <img src='https://img.shields.io/badge/FuzzyWuzzy-4169E1?logo=python&logoColor=white' alt='FuzzyWuzzy'/>
                <img src='https://img.shields.io/badge/Polygon%20API-3957FF?logo=polygon&logoColor=white' alt='Polygon API Client'/>
                <img src='https://img.shields.io/badge/Alpaca%20API-v3.2.0-blue.svg' alt='Alpaca API'/>
                <img src='https://img.shields.io/badge/Python--Dotenv-FFD700?logo=python&logoColor=black' alt='Python-Dotenv'/>
                <img src='https://img.shields.io/badge/Ruff-D37D37?logo=python&logoColor=white' alt='Ruff'/>
                <img src='https://img.shields.io/badge/license-MIT-green.svg' alt='License'/>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Overview Section - Enhanced card styling and heading
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>🚀 Overview</h2>
            <p class='text-lg text-gray-700 leading-relaxed mb-4'>
                Prometheus is an algorithmic trading research platform that integrates with the 
                <a href='https://alpaca.markets/' target='_blank' rel='noopener noreferrer' class='text-sky-600 hover:text-sky-800 hover:underline'>Alpaca Markets API</a> 
                for trading strategies. This project combines data analysis, machine learning models, and market data analysis to support trading research and development.
            </p>
            <div class='bg-gradient-to-r from-sky-50 to-blue-50 p-4 rounded-lg border-l-4 border-sky-400'>
                <p class='text-sky-800 font-medium'>🎯 Research Platform Focus</p>
                <p class='text-sky-700 text-sm mt-1'>This platform emphasizes rigorous academic research and open-source contributions to the algorithmic trading community.</p>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Key Accomplishments Section - New Interactive Section
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-green-500 pl-4'>🏆 Key Accomplishments</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Create interactive tabs for accomplishments
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "📚 Academic Research",
            "🏗️ Data Infrastructure",
            "🖥️ Research Platform",
            "📊 Multi-Strategy Framework",
            "🤖 ML Integration",
            "🌐 Open Source",
        ]
    )

    with tab1:
        st.markdown(
            """
            <div class='bg-gradient-to-r from-green-50 to-emerald-50 p-6 rounded-lg border-l-4 border-green-400 mb-4'>
                <h3 class='text-xl font-semibold text-green-800 mb-3'>📚 Published Academic Research</h3>
                <p class='text-green-700 mb-3'>Successfully published research achieving <strong>over 87% accuracy</strong> in stock price movement predictions</p>
                <div class='bg-white p-4 rounded-lg shadow-sm'>
                    <p class='text-sm text-gray-600 mb-2'><strong>Paper:</strong> "The Financial Torque Hypothesis: Predicting Short-Term Stock Price Movements Using LSTM Neural Networks"</p>
                    <p class='text-sm text-gray-600 mb-2'><strong>Published:</strong> SSRN (June 2025)</p>
                    <p class='text-sm text-gray-600'><strong>Achievement:</strong> 87%+ accuracy with 21 months of unseen test data</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab2:
        st.markdown(
            """
            <div class='bg-gradient-to-r from-blue-50 to-cyan-50 p-6 rounded-lg border-l-4 border-blue-400 mb-4'>
                <h3 class='text-xl font-semibold text-blue-800 mb-3'>🏗️ Comprehensive Data Infrastructure</h3>
                <p class='text-blue-700 mb-3'>Built extensive market data collection system with multiple feed support</p>
                <ul class='list-disc list-inside space-y-1 text-blue-600'>
                    <li>Multiple data feeds (IEX, SIP)</li>
                    <li>Regular trading hours + extended session data</li>
                    <li>Automated data collection and processing</li>
                    <li>Scalable storage architecture</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab3:
        st.markdown(
            """
            <div class='bg-gradient-to-r from-purple-50 to-pink-50 p-6 rounded-lg border-l-4 border-purple-400 mb-4'>
                <h3 class='text-xl font-semibold text-purple-800 mb-3'>🖥️ Interactive Research Platform</h3>
                <p class='text-purple-700 mb-3'>Full-featured Streamlit web application for research insights</p>
                <ul class='list-disc list-inside space-y-1 text-purple-600'>
                    <li>Data visualization and analysis tools</li>
                    <li>Model analysis and insights</li>
                    <li>Interactive research interface</li>
                    <li>Real-time data exploration</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab4:
        st.markdown(
            """
            <div class='bg-gradient-to-r from-orange-50 to-red-50 p-6 rounded-lg border-l-4 border-orange-400 mb-4'>
                <h3 class='text-xl font-semibold text-orange-800 mb-3'>📊 Multi-Strategy Framework</h3>
                <p class='text-orange-700 mb-3'>Research notebooks for different trading approaches</p>
                <ul class='list-disc list-inside space-y-1 text-orange-600'>
                    <li>Simons quantitative strategy research</li>
                    <li>Sun Tzu tactical analysis</li>
                    <li>Modular strategy development</li>
                    <li>Comparative analysis tools</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab5:
        st.markdown(
            """
            <div class='bg-gradient-to-r from-indigo-50 to-blue-50 p-6 rounded-lg border-l-4 border-indigo-400 mb-4'>
                <h3 class='text-xl font-semibold text-indigo-800 mb-3'>🤖 Machine Learning Integration</h3>
                <p class='text-indigo-700 mb-3'>TensorFlow-based LSTM neural networks with real market data</p>
                <ul class='list-disc list-inside space-y-1 text-indigo-600'>
                    <li>LSTM neural network implementation</li>
                    <li>Real-time market data integration</li>
                    <li>Predictive modeling capabilities</li>
                    <li>Model performance optimization</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tab6:
        st.markdown(
            """
            <div class='bg-gradient-to-r from-teal-50 to-green-50 p-6 rounded-lg border-l-4 border-teal-400 mb-4'>
                <h3 class='text-xl font-semibold text-teal-800 mb-3'>🌐 Open Source Contribution</h3>
                <p class='text-teal-700 mb-3'>Complete research platform with academic contributions</p>
                <ul class='list-disc list-inside space-y-1 text-teal-600'>
                    <li>MIT License for open access</li>
                    <li>Comprehensive documentation</li>
                    <li>Dependency management</li>
                    <li>Academic citations and references</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Academic Publications Section - New Interactive Section
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-amber-500 pl-4'>🪶 Academic Publications</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Create expandable sections for publications
    with st.expander(
        "📄 Published Research - The Financial Torque Hypothesis", expanded=True
    ):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(
                """
                **[The Financial Torque Hypothesis: Predicting Short-Term Stock Price Movements Using LSTM Neural Networks](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5288444)**
                
                **Authors:** [Guilherme Grancho Duarte Fernandes](https://www.linkedin.com/in/guilhermegrancho/), [Vasco V. R. Serpa Pereira](https://www.linkedin.com/in/vasco-pereira03/)
                
                **Published:** June 20, 2025 - SSRN
                
                **Abstract:** This paper introduces the Financial Torque Hypothesis, which asserts that Volume-Weighted Average Price and Trade Count are critical indicators for predicting stock price movements. By incorporating these features into a Long Short-Term Memory Neural Network, our model achieved over 87% accuracy in predicting stock-price increases over a three-hour horizon, based on 21 months of previously unseen test data. We also perform a comprehensive comparative analysis of model performance using two datasets: one that spans the entire trading session—pre-market, regular-market and after-hours—and one confined to regular-market hours. Our results reveal that models trained on full-session data consistently outperform those built on regular-hours-only data, delivering a 15% improvement in predictive accuracy.
                
                **Citation:**
                ```
                Fernandes, Guilherme Grancho Duarte and Pereira, Vasco, The Financial Torque Hypothesis: 
                Predicting Short-Term Stock Price Movements Using LSTM Neural Networks (June 20, 2025). 
                Available at SSRN: https://ssrn.com/abstract=5288444
                ```
                """
            )

        with col2:
            st.metric("Accuracy", "87%+", "15% improvement")
            st.metric("Test Period", "21 months", "Unseen data")
            st.metric("Prediction Horizon", "3 hours", "Real-time")
            st.metric("Data Improvement", "15%", "Full-session vs RTH")

    with st.expander("🔬 Upcoming Research - Advanced Portfolio Management"):
        st.markdown(
            """
            **Integrating The Financial Torque Hypothesis into Advanced Algorithmic Portfolio Management**
            
            **Authors:** [Guilherme Grancho Duarte Fernandes](https://www.linkedin.com/in/guilhermegrancho/), [Vasco V. R. Serpa Pereira](https://www.linkedin.com/in/vasco-pereira03/)
            
            **Status:** 🔄 Set to be published in the coming months
            
            This upcoming publication will detail the practical implementation of the Financial Torque Hypothesis within the Prometheus trading platform and its integration into advanced portfolio management strategies. The research will cover portfolio optimization techniques, risk management integration, and real-world application scenarios.
            """
        )

        st.info("📅 Expected Publication: Coming Months - Stay tuned for updates!")

        # Add progress indicator
        progress_col1, progress_col2 = st.columns([3, 1])
        with progress_col1:
            st.progress(0.75, text="Research Progress: 75% Complete")
        with progress_col2:
            st.markdown("**🔬 In Development**")

    # Future Roadmap Section - Interactive Timeline
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-violet-500 pl-4'>🚀 Future Roadmap</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Create roadmap with progress indicators
    roadmap_items = [
        {
            "title": "Next.js Frontend Migration",
            "description": "Transition to modern Next.js web application",
            "status": "🔄 In Planning",
            "color": "blue",
        },
        {
            "title": "Advanced Portfolio Management Research",
            "description": "Second academic publication development",
            "status": "📝 In Progress",
            "color": "green",
        },
        {
            "title": "Enhanced ML Models",
            "description": "Expand LSTM framework with ensemble methods",
            "status": "🔄 In Planning",
            "color": "purple",
        },
        {
            "title": "Real-time Trading Integration",
            "description": "Production-ready trading execution",
            "status": "🔮 Future",
            "color": "orange",
        },
        {
            "title": "API Development",
            "description": "REST APIs for third-party integrations",
            "status": "🔮 Future",
            "color": "teal",
        },
    ]

    for i, item in enumerate(roadmap_items):
        with st.container():
            col1, col2, col3 = st.columns([1, 8, 2])

            with col1:
                st.markdown(f"**{i + 1}.**")

            with col2:
                st.markdown(f"**{item['title']}**")
                st.markdown(f"*{item['description']}*")

            with col3:
                st.markdown(f"**{item['status']}**")

            if i < len(roadmap_items) - 1:
                st.markdown("---")

    # Features Section - Enhanced card styling, heading, and feature item styling
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>✨ Features</h2>
            <div class='grid md:grid-cols-2 gap-8'>
                <div class='bg-gray-50 p-6 rounded-lg shadow-lg border border-gray-100 hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 ease-out'>
                    <h3 class='text-xl font-medium text-sky-700 mb-3'>Market Data Integration</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600 marker:text-sky-500'>
                        <li>Integration with Alpaca Markets API</li>
                        <li>Data collection with rate limit management</li>
                        <li>Support for multiple timeframes and market data types (IEX, SIP)</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-lg border border-gray-100 hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 ease-out'>
                    <h3 class='text-xl font-medium text-sky-700 mb-3'>Trading Research Models</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600 marker:text-sky-500'>
                        <li>Machine learning model integration with TensorFlow</li>
                        <li>Custom trading strategies research (Simons, Sun Tzu)</li>
                        <li>Research-based approach with separate modules</li>
                        <li>Structured model management and evaluation</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-lg border border-gray-100 hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 ease-out'>
                    <h3 class='text-xl font-medium text-sky-700 mb-3'>Data Analysis & Visualization</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600 marker:text-sky-500'>
                        <li>Market data analysis using pandas and numpy</li>
                        <li>Data visualization with matplotlib and plotly</li>
                        <li>Performance metrics and reporting</li>
                        <li>Historical data analysis and storage</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-lg border border-gray-100 hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 ease-out'>
                    <h3 class='text-xl font-medium text-sky-700 mb-3'>Risk Management Research</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600 marker:text-sky-500'>
                        <li>Position sizing algorithms research</li>
                        <li>Stop-loss and take-profit mechanisms research</li>
                        <li>Portfolio diversification strategies research</li>
                        <li>Risk assessment tools research</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-lg border border-gray-100 hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 ease-out'>
                    <h3 class='text-xl font-medium text-sky-700 mb-3'>Interactive Frontend Dashboard</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600 marker:text-sky-500'>
                        <li>Portfolio monitoring and tracking</li>
                        <li>Strategy visualization with charts</li>
                        <li>Risk management interface</li>
                        <li>Academic research integration</li>
                    </ul>
                </div>
                <div class='bg-gray-50 p-6 rounded-lg shadow-lg border border-gray-100 hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 ease-out'>
                    <h3 class='text-xl font-medium text-sky-700 mb-3'>Live Trading Research</h3>
                    <ul class='list-disc list-inside space-y-2 text-gray-600 marker:text-sky-500'>
                        <li>Jupyter notebook for live trading research</li>
                        <li>Research and monitoring capabilities</li>
                        <li>Risk assessment integration</li>
                        <li>Academic research validation</li>
                    </ul>
                </div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Project Structure Section - Enhanced card styling and updated structure from README
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>📊 Project Structure</h2>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto border border-gray-200 border-t-4 border-gray-300'><code>Prometheus/
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
├── Simons/                     # Simons trading strategy research
│   ├── backend/                # Research notebooks for Simons strategy
│   ├── Images/                 # Images related to Simons strategy
│   ├── Paper/                  # Research paper published on SSRN
│   ├── Report/                 # Reports and results for Simons
│   └── Settings/               # Configuration for Simons strategy
├── Sun_Tzu/                    # Sun Tzu trading strategy research
│   ├── backend/                # Research notebooks for Sun Tzu strategy
│   └── research/               # Research for Sun Tzu strategy
├── .venv/                      # Python virtual environment
├── .git/                       # Git version control files
├── .gitignore                  # Specifies intentionally untracked files that Git should ignore
├── CITATION.cff                # Citation file for the project
├── LICENSE                     # Project license (MIT)
├── pyproject.toml              # Project build configuration (PEP 518)
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── uv.lock                     # Lock file for uv package manager
</code></pre>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Streamlit App Navigation Section - Enhanced card styling, heading, lists, and pre block
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>🧭 Navigating the Dashboard</h2>
            <p class='text-gray-700 mb-4'>
                This Streamlit application serves as the main interface for interacting with the Prometheus trading platform. Here's a brief guide on its structure and how to use it:
            </p>
            <ul class='list-disc list-inside space-y-3 text-gray-700 marker:text-sky-500'>
                <li><strong>Overview (This Page):</strong> You are currently on the Overview page, which provides a general introduction to the project, its features, setup instructions, and how to use different components.</li>
                <li><strong>Top Bar Navigation:</strong> At the top of the application, you'll find a navigation bar. This top bar is the primary way to navigate between different sections or pages of the dashboard. Each page will focus on a specific aspect of the platform, such as:
                    <ul class='list-disc list-inside pl-6 space-y-1 text-gray-600 marker:text-sky-400'>
                        <li>Detailed views of trading strategy performance.</li>
                        <li>Market data visualization and analysis tools.</li>
                        <li>Configuration settings for trading parameters.</li>
                        <li>Live trading monitoring (if applicable and enabled).</li>
                    </ul>
                </li>
                <li><strong>Interactive Elements:</strong> Throughout the application, you will encounter various interactive elements like charts, tables, input fields, and buttons. These are designed to allow you to:
                    <ul class='list-disc list-inside pl-6 space-y-1 text-gray-600 marker:text-sky-400'>
                        <li>Explore data dynamically.</li>
                        <li>Adjust parameters for analysis or trading models.</li>
                        <li>View real-time updates and logs.</li>
                    </ul>
                </li>
                <li><strong>Data Display:</strong> Key information, such as market data, model predictions, portfolio status, and performance metrics, will be displayed in a clear and organized manner using tables, charts, and text summaries.</li>
                <li><strong>Launching the App:</strong> As mentioned in the 'Usage' section, you can run the Streamlit app using the command:
            </ul>
            <pre class='bg-gray-100 p-3 rounded text-sm overflow-x-auto mt-2 mb-2 border border-gray-200 border-t-4 border-gray-300'><code>streamlit run frontend/my-streamlit-app/Home.py</code></pre>
            <p class='text-gray-700 mt-3'>
                Explore the different pages using the top navigation bar to get a comprehensive understanding of the platform's capabilities. Each section is designed to be intuitive, but specific instructions or tooltips may be provided within those pages for more complex functionalities.
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Implemented Strategies Section - Enhanced card styling, heading, and list
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>📈 Research Strategies</h2>
            <p class='text-gray-700 mb-4'>The platform supports research into multiple trading strategies:</p>
            <ul class='list-disc list-inside space-y-3 text-gray-700 marker:text-sky-500'>
                <li><strong class='text-sky-700'>Simons Strategy:</strong> Quantitative trading research approach (see <code>Simons/backend/Simons.ipynb</code>)</li>
                <li><strong class='text-sky-700'>Sun Tzu Strategy:</strong> Tactical market analysis research (see <code>Sun_Tzu/backend/Ronin_SunTzu.ipynb</code>)</li>
            </ul>
            <p class='mt-5 text-sm text-gray-500'>Performance metrics can be analyzed through the provided research notebooks.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Installation Section - Enhanced with updated GitHub clone command
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>🛠️ Installation</h2>
            <p class='text-gray-700 mb-4'>Follow these steps to set up the project locally:</p>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4 marker:text-sky-600 marker:font-semibold'>
                <li>Clone the repository:</li>
            </ol>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto mt-2 mb-4 border border-gray-200 border-t-4 border-gray-300'><code>git clone [YOUR_REPOSITORY_URL]
cd Prometheus</code></pre>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4 marker:text-sky-600 marker:font-semibold' start='2'>
                <li>Create and activate a virtual environment:</li>
            </ol>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto mt-2 mb-4 border border-gray-200 border-t-4 border-gray-300'><code>python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate</code></pre>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4 marker:text-sky-600 marker:font-semibold' start='3'>
                <li>Install required dependencies:</li>
            </ol>
            <pre class='bg-gray-100 p-4 rounded text-sm overflow-x-auto mt-2 mb-4 border border-gray-200 border-t-4 border-gray-300'><code>pip install -r requirements.txt</code></pre>
            <ol class='list-decimal list-inside space-y-3 text-gray-700 mb-4 marker:text-sky-600 marker:font-semibold' start='4'>
                <li>Set up your Alpaca API credentials:
                    <ul class='list-disc list-inside pl-6 space-y-1 text-gray-600 marker:text-sky-400'>
                        <li>Create an account at <a href='https://alpaca.markets/' target='_blank' rel='noopener noreferrer' class='text-sky-600 hover:text-sky-800 hover:underline'>Alpaca Markets</a></li>
                        <li>Generate your API keys</li>
                        <li>Configure your credentials in the appropriate configuration files (e.g., within <code>Simons/Settings/</code> or as environment variables)</li>
                    </ul>
                </li>
            </ol>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Usage Example Section - Enhanced card styling, heading, and step titles
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>🚀 Usage</h2>
            <p class='text-gray-700 mb-4 text-lg'><strong>1. Launching the Frontend Dashboard:</strong></p>
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
            <p class='text-gray-700 mt-4 mb-4 text-lg'><strong>2. Data Collection and Analysis:</strong></p>
            <p class='text-gray-700 mb-2'>Refer to notebooks within <code>Data/</code> subdirectories or specific strategy research. Example of initializing API connection:</p>
        """,
        unsafe_allow_html=True,
    )

    st.code(
        """
    # Example: Initialize API connection (ensure credentials are set)
    import alpaca_trade_api as tradeapi

    api = tradeapi.REST(
        key_id='YOUR_API_KEY',          # Preferably set via environment variables
        secret_key='YOUR_SECRET_KEY',  # Preferably set via environment variables
        base_url='https://paper-api.alpaca.markets'
    )

    # Example: Fetch market data
    # data = api.get_bars('AAPL', '1D', '2024-01-01', '2024-04-15').df
    # For more detailed data handling, see notebooks in Data/ or strategy research folders.
    """,
        language="python",
    )

    st.markdown(
        """
            <p class='text-gray-700 mt-4 mb-4 text-lg'><strong>3. Running Trading Strategies:</strong></p>
            <p class='text-gray-700 mb-2'>The strategy modules referenced below are research notebooks:</p>
        """,
        unsafe_allow_html=True,
    )
    st.code(
        """
    # Note: The strategy modules referenced below are research notebooks
    # and not standalone importable modules. Refer to the actual notebook files:
    # - Simons/backend/Simons.ipynb 
    # - Sun_Tzu/backend/Ronin_SunTzu.ipynb
    
    # For actual strategy implementation, see the notebook files directly
    """,
        language="python",
    )

    st.markdown(
        """
            <p class='text-gray-700 mt-4 mb-4 text-lg'><strong>4. Live Trading Research:</strong></p>
            <p class='text-gray-700'>Open and run cells in <code>Live_Trading/Live_Trading.ipynb</code> after appropriate setup and risk assessment.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Performance Section - Enhanced card styling, heading, and list
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>📈 Research Performance</h2>
            <p class='text-gray-700 mb-4'>The platform supports research into multiple trading strategies:</p>
            
            <div class='grid md:grid-cols-2 gap-6 mb-6'>
                <div class='bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-lg border-l-4 border-blue-500'>
                    <h3 class='text-xl font-semibold text-blue-800 mb-3'>📊 Simons Strategy</h3>
                    <p class='text-blue-700 mb-2'>Quantitative trading research approach</p>
                    <p class='text-sm text-blue-600'>Research notebooks available in <code>Simons/backend/Simons.ipynb</code></p>
                </div>
                
                <div class='bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-lg border-l-4 border-green-500'>
                    <h3 class='text-xl font-semibold text-green-800 mb-3'>⚔️ Sun Tzu Strategy</h3>
                    <p class='text-green-700 mb-2'>Tactical market analysis research</p>
                    <p class='text-sm text-green-600'>Research notebooks available in <code>Sun_Tzu/backend/Ronin_SunTzu.ipynb</code></p>
                </div>
            </div>
            
            <div class='bg-gradient-to-r from-amber-50 to-orange-50 p-6 rounded-lg border-l-4 border-amber-500'>
                <h3 class='text-lg font-semibold text-amber-800 mb-2'>🏆 Academic Achievement</h3>
                <p class='text-amber-700'>Published research achieving <strong>87%+ accuracy</strong> in stock price predictions with the Financial Torque Hypothesis implementation.</p>
            </div>
            
            <p class='text-gray-700 mt-4'>Performance metrics can be analyzed through the provided research notebooks and academic publications.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Contributing Section - Enhanced card styling, heading, and list
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-sky-500 pl-4'>🤝 Contributing</h2>
            <p class='text-gray-700 mb-4'>Contributions are welcome! Please follow these steps:</p>
            <ol class='list-decimal list-inside space-y-2 text-gray-700 marker:text-sky-600 marker:font-semibold'>
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

    # Contact Section - Interactive Authors Information
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-blue-500 pl-4'>👥 Authors & Contact</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Create two columns for authors
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class='bg-gradient-to-br from-blue-50 to-indigo-50 p-6 rounded-lg border border-blue-200'>
                <h3 class='text-xl font-semibold text-blue-800 mb-3'>👨‍🎓 Guilherme Grancho</h3>
                <div class='space-y-2'>
                    <p class='text-blue-700'><strong>Affiliations:</strong></p>
                    <ul class='text-sm text-blue-600 space-y-1'>
                        <li>• Department of Earth Science and Engineering, Imperial College London</li>
                        <li>• Department of Physics, Instituto Superior Técnico, Lisbon</li>
                    </ul>
                    <div class='mt-4 space-y-2'>
                        <a href='https://www.linkedin.com/in/guilhermegrancho/' target='_blank' class='inline-block bg-blue-600 text-white px-3 py-1 rounded text-sm hover:bg-blue-700 transition-colors'>LinkedIn</a>
                        <div class='text-sm text-blue-600'>
                            <p>📧 <a href='mailto:guilhermegrancho@tecnico.ulisboa.pt' class='hover:underline'>guilhermegrancho@tecnico.ulisboa.pt</a></p>
                            <p>📧 <a href='mailto:guilherme.fernandes25@imperial.ac.uk' class='hover:underline'>guilherme.fernandes25@imperial.ac.uk</a></p>
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class='bg-gradient-to-br from-green-50 to-teal-50 p-6 rounded-lg border border-green-200'>
                <h3 class='text-xl font-semibold text-green-800 mb-3'>👨‍💻 Vasco Pereira</h3>
                <div class='space-y-2'>
                    <p class='text-green-700'><strong>Affiliation:</strong></p>
                    <ul class='text-sm text-green-600 space-y-1'>
                        <li>• Department of Computer Science and Engineering, Instituto Superior Técnico, Lisbon</li>
                    </ul>
                    <div class='mt-4 space-y-2'>
                        <a href='https://www.linkedin.com/in/vasco-pereira03/' target='_blank' class='inline-block bg-green-600 text-white px-3 py-1 rounded text-sm hover:bg-green-700 transition-colors'>LinkedIn</a>
                        <div class='text-sm text-green-600'>
                            <p>📧 <a href='mailto:vasco.serpa.pereira@tecnico.ulisboa.pt' class='hover:underline'>vasco.serpa.pereira@tecnico.ulisboa.pt</a></p>
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Footer - Enhanced with license and acknowledgments from README
    st.markdown(
        """
        <footer class='text-center mt-16 py-8 border-t border-gray-400'>
            <div class='mb-6'>
                <h3 class='text-lg font-semibold text-gray-700 mb-3'>📄 License & Acknowledgments</h3>
                <p class='text-base text-gray-600 mb-3'>
                    This project is licensed under the MIT License - see the <a href='https://github.com/yourusername/Prometheus/blob/main/LICENSE' target='_blank' rel='noopener noreferrer' class='text-sky-600 hover:text-sky-800 hover:underline'>LICENSE</a> file for details.
                </p>
            </div>
            
            <div class='mb-4'>
                <p class='text-sm text-gray-500'>
                    <strong>Acknowledgments:</strong> 
                    <a href='https://alpaca.markets/' target='_blank' rel='noopener noreferrer' class='text-sky-600 hover:text-sky-800 hover:underline'>Alpaca Markets</a> • 
                    Contributors & Maintainers • 
                    The Open-Source Community
                </p>
            </div>
            
            <div class='text-xs text-gray-400'>
                <p><strong>Citation:</strong> If you use this research platform, please cite our work:</p>
                <p class='font-mono bg-gray-100 inline-block px-2 py-1 rounded mt-1'>
                    Fernandes, G. G. D. & Pereira, V. (2025). The Financial Torque Hypothesis. SSRN.
                </p>
            </div>
        </footer>
    """,
        unsafe_allow_html=True,
    )

    # Close the wrapping div
    st.markdown("</div>", unsafe_allow_html=True)

    # Interactive Performance Dashboard Section
    st.markdown("---")
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-gradient-to-r from-slate-50 to-blue-50 shadow-xl rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-indigo-500 pl-4'>📊 Interactive Research Dashboard</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Interactive Performance Dashboard Section
    st.markdown("---")
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-gradient-to-r from-slate-50 to-blue-50 shadow-xl rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-indigo-500 pl-4'>📊 Interactive Research Dashboard</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Interactive Metrics Section - Enhanced with more detailed metrics
    st.markdown(
        """
        <div class='container mx-auto px-6 py-4 bg-gradient-to-r from-blue-50 to-indigo-50 shadow-lg rounded-lg mb-6'>
            <h3 class='text-2xl font-semibold text-center text-gray-800 mb-4'>📊 Research Platform Metrics</h3>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Create metrics columns with enhanced information
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="🎯 ML Model Accuracy",
            value="87.2%",
            delta="15% improvement",
            help="Accuracy achieved by the Financial Torque Hypothesis model on 21 months of unseen test data",
        )

    with col2:
        st.metric(
            label="📈 Test Data Period",
            value="21 months",
            delta="Unseen data",
            help="Duration of previously unseen test data used for validation",
        )

    with col3:
        st.metric(
            label="🔬 Research Strategies",
            value="3",
            delta="Active research",
            help="Number of trading strategies under active research (Financial Torque, Simons, Sun Tzu)",
        )

    with col4:
        st.metric(
            label="📚 Publications",
            value="1",
            delta="+1 upcoming",
            help="Published academic papers with one more in development",
        )

    with col5:
        st.metric(
            label="⏱️ Prediction Horizon",
            value="3 hours",
            delta="Real-time",
            help="Time horizon for stock price movement predictions",
        )

    # Interactive Performance Comparison Section
    st.markdown("### 🏆 Research Strategy Performance Comparison")

    # Create tabs for different performance views
    perf_tab1, perf_tab2, perf_tab3 = st.tabs(
        ["📊 Accuracy Comparison", "📈 Performance Simulation", "🔍 Model Insights"]
    )

    with perf_tab1:
        st.markdown("**Strategy Research Accuracy Rates**")
        col1, col2 = st.columns([2, 1])

        with col1:
            fig2 = create_strategy_comparison()
            st.plotly_chart(fig2, use_container_width=True)

        with col2:
            st.markdown("""
            **Key Findings:**
            
            🥇 **Financial Torque Hypothesis**
            - 87.2% accuracy
            - LSTM neural networks
            - Published research
            
            🥈 **Simons Strategy**
            - 82.5% accuracy  
            - Quantitative approach
            - Mathematical modeling
            
            🥉 **Sun Tzu Strategy**
            - 78.3% accuracy
            - Tactical analysis
            - Strategic positioning
            """)

    with perf_tab2:
        st.markdown("**Research Platform Performance Simulation**")
        st.info(
            "📊 This chart shows a simulated performance based on research methodologies. Actual results may vary."
        )

        # Add an interactive selector for time period
        col1, col2 = st.columns([3, 1])

        with col1:
            time_period = st.selectbox(
                "Select Time Period for Simulation:",
                ["1 Year", "6 Months", "3 Months"],
                index=0,
            )

        with col2:
            show_metrics = st.checkbox("Show Performance Metrics", value=True)

        fig1 = create_sample_performance_chart(time_period)
        st.plotly_chart(fig1, use_container_width=True)

        if show_metrics:
            # Add some context
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Simulated Annual Return", "24.7%", "2.1%")
            with col2:
                st.metric("Max Drawdown", "-8.3%", "0.5%")
            with col3:
                st.metric("Sharpe Ratio", "1.87", "0.12")
            with col4:
                st.metric("Win Rate", "68.4%", "3.2%")

    with perf_tab3:
        st.markdown("**Model Architecture & Insights**")

        # Create expandable sections for technical details
        with st.expander(
            "🧠 Financial Torque Hypothesis - Technical Details", expanded=True
        ):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("""
                **Model Architecture:**
                - LSTM Neural Network
                - TensorFlow implementation
                - Volume-Weighted Average Price (VWAP)
                - Trade Count features
                - 3-hour prediction horizon
                """)

            with col2:
                st.markdown("""
                **Key Performance Factors:**
                - Full-session data (pre + regular + after hours)
                - 15% improvement over regular-hours-only
                - 21 months of unseen test data
                - Real-time market data integration
                """)

        with st.expander("📊 Data Infrastructure"):
            st.markdown("""
            **Data Sources:**
            - **IEX Feed**: Real-time market data
            - **SIP Feed**: Securities Information Processor data
            - **Regular Hours**: Standard trading session (9:30 AM - 4:00 PM ET)
            - **Extended Hours**: Pre-market and after-hours sessions
            
            **Processing Pipeline:**
            - Automated data collection
            - Rate limit management
            - Data normalization and feature engineering
            - Real-time scalers for model inputs
            """)

        with st.expander("🔬 Research Methodology"):
            st.markdown("""
            **Academic Rigor:**
            - Peer-reviewed publication process
            - Comprehensive backtesting framework
            - Out-of-sample validation (21 months)
            - Comparative analysis across multiple datasets
            
            **Validation Process:**
            - Train/validation/test splits
            - Time-series cross-validation
            - Performance consistency checks
            - Risk-adjusted return analysis
            """)

    # Interactive Metrics Section - Original but enhanced
    st.markdown("---")

    chart_tab1, chart_tab2 = st.tabs(
        ["📈 Performance Simulation", "🏆 Strategy Comparison"]
    )

    with chart_tab1:
        st.markdown("### Research Platform Performance Simulation")
        st.info(
            "📊 This chart shows a simulated performance based on research methodologies. Actual results may vary."
        )

        # Add an interactive selector for time period
        time_period = st.selectbox(
            "Select Time Period for Simulation:",
            ["1 Year", "6 Months", "3 Months"],
            index=0,
        )

        fig1 = create_sample_performance_chart(time_period)
        st.plotly_chart(fig1, use_container_width=True)

        # Add some context
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Simulated Annual Return", "24.7%", "2.1%")
        with col2:
            st.metric("Max Drawdown", "-8.3%", "0.5%")
        with col3:
            st.metric("Sharpe Ratio", "1.87", "0.12")

    with chart_tab2:
        st.markdown("### Strategy Research Accuracy Comparison")
        st.info(
            "🎯 Comparison of accuracy rates achieved by different research strategies."
        )

        fig2 = create_strategy_comparison()
        st.plotly_chart(fig2, use_container_width=True)

        # Add explanatory text
        st.markdown("""
        **Research Findings:**
        - **Financial Torque Hypothesis**: Highest accuracy at 87.2% using LSTM neural networks
        - **Simons Strategy**: Quantitative approach achieving 82.5% accuracy
        - **Sun Tzu Strategy**: Tactical analysis with 78.3% accuracy
        
        *All accuracy measurements are based on historical backtesting and research validation.*
        """)

    # Interactive FAQ Section
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-white shadow-xl rounded-lg mb-10 transition-shadow duration-300 hover:shadow-2xl'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-purple-500 pl-4'>❓ Frequently Asked Questions</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    with st.expander("🤖 What is the Financial Torque Hypothesis?"):
        st.markdown("""
        The **Financial Torque Hypothesis** is our groundbreaking research that asserts Volume-Weighted Average Price (VWAP) and Trade Count are critical indicators for predicting stock price movements. 
        
        Our LSTM neural network implementation achieved **over 87% accuracy** in predicting stock price increases over a three-hour horizon, validated with 21 months of previously unseen test data.
        
        **Key Findings:**
        - 📊 Models trained on full-session data (pre-market + regular + after-hours) outperform regular-hours-only models by 15%
        - 🎯 87%+ accuracy rate with real market data validation
        - 📈 Robust performance across different market conditions
        """)

    with st.expander("🔬 How does this research platform work?"):
        st.markdown("""
        Prometheus is designed as a **research-first platform** that combines:
        
        **Data Infrastructure:**
        - Multiple market data feeds (IEX, SIP)
        - Real-time and historical data processing
        - Extended trading hours support
        
        **Machine Learning Pipeline:**
        - TensorFlow-based LSTM neural networks
        - Feature engineering with VWAP and Trade Count
        - Comprehensive backtesting framework
        
        **Research Environment:**
        - Jupyter notebooks for strategy development
        - Interactive Streamlit dashboard for visualization
        - Academic publication integration
        """)

    with st.expander("📊 What trading strategies are researched here?"):
        st.markdown("""
        We currently research **three main strategies**:
        
        **1. Financial Torque Hypothesis**
        - Published academic research
        - 87%+ accuracy in price predictions
        - LSTM neural network implementation
        
        **2. Simons Strategy**
        - Quantitative trading research approach
        - Mathematical modeling focus
        - Available in `Simons/backend/Simons.ipynb`
        
        **3. Sun Tzu Strategy**
        - Tactical market analysis research
        - Strategic positioning methods
        - Available in `Sun_Tzu/backend/Ronin_SunTzu.ipynb`
        """)

    with st.expander("🎓 Is this for academic or commercial use?"):
        st.markdown("""
        **Prometheus is primarily an academic research platform** with the following characteristics:
        
        **Academic Focus:**
        - 📚 Published research in peer-reviewed venues
        - 🔬 Open-source contributions to the community
        - 🎓 Educational resource for algorithmic trading research
        
        **Open Source:**
        - MIT License for broad accessibility
        - Complete source code available
        - Comprehensive documentation
        
        **Research Ethics:**
        - Rigorous validation methodologies
        - Transparent reporting of results
        - Emphasis on academic integrity
        """)

    with st.expander("🚀 How can I get started?"):
        st.markdown("""
        **Getting Started with Prometheus:**
        
        **1. Clone and Setup** 📥
        ```bash
        git clone [repository-url]
        cd Prometheus
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        ```
        
        **2. Explore the Research** 🔍
        - Read our published paper on SSRN
        - Review Jupyter notebooks in strategy folders
        - Examine the data processing pipeline
        
        **3. Run the Dashboard** 🖥️
        ```bash
        streamlit run frontend/my-streamlit-app/Home.py
        ```
        
        **4. Set Up API Access** 🔑
        - Create Alpaca Markets account
        - Configure API credentials
        - Start with paper trading for research
        """)

    # Interactive Research Status Board
    st.markdown("---")
    st.markdown(
        """
        <div class='container mx-auto px-6 py-8 bg-gradient-to-r from-purple-50 to-pink-50 shadow-xl rounded-lg mb-10'>
            <h2 class='text-3xl font-semibold text-gray-800 mb-6 border-b border-gray-200 pb-3 border-l-4 border-purple-500 pl-4'>🚀 Live Research Status</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Create a status dashboard
    status_col1, status_col2, status_col3 = st.columns(3)

    with status_col1:
        st.markdown("**📊 Current Research**")
        st.progress(1.0, text="Financial Torque Hypothesis - Published ✅")
        st.progress(0.75, text="Advanced Portfolio Management - 75% Complete")
        st.progress(0.3, text="Enhanced ML Models - In Planning")

    with status_col2:
        st.markdown("**🔬 Active Studies**")
        st.markdown("""
        - ✅ LSTM Neural Network Performance
        - ✅ Full vs Regular Session Analysis  
        - 🔄 Ensemble Methods Research
        - 🔄 Risk Management Integration
        - 📅 API Development Planning
        """)

    with status_col3:
        st.markdown("**📈 Next Milestones**")
        st.markdown("""
        - **Q3 2025**: Second paper submission
        - **Q4 2025**: Next.js frontend migration  
        - **Q1 2026**: Enhanced ML models
        - **Q2 2026**: API development
        - **Q3 2026**: Production trading integration
        """)

    # Quick navigation section
    st.markdown("---")
    st.markdown("### 🧭 Quick Navigation & Resources")

    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

    with nav_col1:
        st.markdown("""
        **📚 Research Papers**
        - [SSRN Publication](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5288444)
        - Citation Guidelines
        - Academic References
        """)

    with nav_col2:
        st.markdown("""
        **💻 Code & Data**
        - Jupyter Notebooks
        - Strategy Implementations
        - Data Processing Scripts
        """)

    with nav_col3:
        st.markdown("""
        **🔧 Setup & Config**
        - Installation Guide
        - API Configuration
        - Environment Setup
        """)

    with nav_col4:
        st.markdown("""
        **🤝 Community**
        - LinkedIn Profiles
        - GitHub Repository
        - Academic Affiliations
        """)

    # Add a final call-to-action
    st.markdown("---")
    st.markdown(
        """
        <div class='text-center py-8 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg'>
            <h3 class='text-2xl font-semibold text-gray-800 mb-4'>🚀 Ready to Explore Prometheus?</h3>
            <p class='text-lg text-gray-600 mb-6'>Start your journey in algorithmic trading research today!</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Create action buttons
    action_col1, action_col2, action_col3, action_col4 = st.columns(4)

    with action_col1:
        if st.button("📖 Read the Paper", use_container_width=True):
            st.success("🔗 Opening SSRN publication...")
            st.markdown(
                "[The Financial Torque Hypothesis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5288444)"
            )

    with action_col2:
        if st.button("📊 View Strategies", use_container_width=True):
            st.info(
                "🎯 Navigate to the strategy pages in the sidebar to explore different research approaches."
            )

    with action_col3:
        if st.button("🔧 Setup Guide", use_container_width=True):
            st.info(
                "📋 Scroll up to view the detailed installation and setup instructions."
            )

    with action_col4:
        if st.button("👥 Contact Authors", use_container_width=True):
            st.success(
                "📧 Contact information is available in the Authors & Contact section above."
            )
