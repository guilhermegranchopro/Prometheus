# 🔥 Prometheus

<div align="center">
  <img src="Assets/Images/logo.jpg" alt="Prometheus Logo" width="700"/>
  
  [![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
  [![Alpaca API](https://img.shields.io/badge/Alpaca%20API-v3.2.0-blue.svg)](https://alpaca.markets/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
  [![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
  [![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
  [![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org/)
  [![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
  [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?logo=matplotlib&logoColor=white)](https://matplotlib.org/)
  [![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
  [![Altair](https://img.shields.io/badge/Altair-15B8D5?logo=altair&logoColor=white)](https://altair-viz.github.io/)
  [![Joblib](https://img.shields.io/badge/Joblib-007ACC?logo=python&logoColor=white)](https://joblib.readthedocs.io/)
  [![FuzzyWuzzy](https://img.shields.io/badge/FuzzyWuzzy-4169E1?logo=python&logoColor=white)](https://github.com/seatgeek/fuzzywuzzy)
  [![Ruff](https://img.shields.io/badge/Ruff-D37D37?logo=python&logoColor=white)](https://github.com/astral-sh/ruff)
  [![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)](https://scipy.org/)
  [![npm](https://img.shields.io/badge/npm-CB3837?logo=npm&logoColor=white)](https://www.npmjs.com/)
  [![Python-Dotenv](https://img.shields.io/badge/Python--Dotenv-FFD700?logo=python&logoColor=black)](https://github.com/theskumar/python-dotenv)
  [![Polygon API Client](https://img.shields.io/badge/Polygon%20API-3957FF?logo=polygon&logoColor=white)](https://polygon.io/)
  [![Python-Levenshtein](https://img.shields.io/badge/Python--Levenshtein-4B8BBE?logo=python&logoColor=white)](https://github.com/maxbachmann/python-Levenshtein)
</div>

## 🚀 Overview

Prometheus is a sophisticated algorithmic trading platform that leverages the Alpaca Markets API to execute automated trading strategies. This project combines advanced data analysis, machine learning models, and real-time market data to make informed trading decisions.

## ✨ Features

- **Real-time Market Data Integration**
  - Seamless integration with Alpaca Markets API
  - High-frequency data collection with rate limit management
  - Support for multiple timeframes and market data types (IEX, SIP)

- **Advanced Trading Models**
  - Machine learning model integration with TensorFlow
  - Custom trading strategies implementation (Simons, Sun Tzu)
  - Research-based approach with separate modules for different strategies
  - Structured model management and evaluation (see `Models/` directory)

- **Data Analysis & Visualization**
  - Comprehensive market data analysis using pandas and numpy
  - Interactive data visualization with matplotlib
  - Performance metrics and reporting
  - Historical data analysis and storage for various sources (see `Data/` directory)

- **Risk Management**
  - Position sizing algorithms
  - Stop-loss and take-profit mechanisms
  - Portfolio diversification strategies
  - Risk assessment tools

- **Interactive Frontend Dashboard**
  - Streamlit application for monitoring and interaction (see `frontend/` directory)

- **Live Trading Capabilities**
  - Jupyter notebook for live trading execution and monitoring (see `Live_Trading/` directory)

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Prometheus.git
    cd Prometheus
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Alpaca API credentials:
    - Create an account at [Alpaca Markets](https://alpaca.markets/)
    - Generate your API keys
    - Configure your credentials in the appropriate configuration files (e.g., within `Simons/Settings/` or as environment variables)

## 📊 Project Structure

```text
Prometheus/
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
│   ├── Paper/                  # Research paper published on Arxiv based on the quantitative software develop for Simons
│   ├── Report/                 # Reports and results for Simons
│   └── Settings/               # Configuration for Simons strategy
├── Sun_Tzu/                    # Sun Tzu trading strategy
│   ├── backend/                # Backend logic for Sun Tzu strategy
│   └── research/               # Research for Sun Tzu strategy
├── .venv/                      # Python virtual environment
├── .git/                       # Git version control files
├── .gitignore                  # Specifies intentionally untracked files that Git should ignore
├── CITATION.cff                # Citation file for the project
├── LICENSE                     # Project license (MIT)
├── pyproject.toml              # Project build configuration (PEP 518)
├── README.md                   # This file
├── requirements.txt            # Project dependencies
└── uv.lock                     # Lock file for uv package manager
```

## 🚀 Usage

1. **Data Collection and Analysis**

    (Refer to notebooks within `Data/` subdirectories or specific strategy research)

    ```python
    # Example: Initialize API connection (ensure credentials are set)
    import alpaca_trade_api as tradeapi

    api = tradeapi.REST(
        key_id='YOUR_API_KEY',          # Preferably set via environment variables
        secret_key='YOUR_SECRET_KEY',  # Preferably set via environment variables
        base_url='https://paper-api.alpaca.markets'
    )

    # Example: Fetch market data
    # data = api.get_bars('AAPL', '1D', '2024-01-01', '2024-04-15').df # Original example
    # For more detailed data handling, see scripts/notebooks in Data/ or strategy research folders.
    ```

2. **Running Trading Strategies**

    ```python
    # Import your preferred strategy module
    from Simons.backend import strategy as simons_strategy
    # or
    from Sun_Tzu.backend import strategy as sun_tzu_strategy

    # Execute the strategy (ensure strategy-specific configurations are set)
    # results = strategy.execute() # Placeholder, actual execution might vary
    ```

3. **Launching the Frontend Dashboard**

    Ensure Streamlit is installed (`pip install streamlit`).

    ```bash
    streamlit run frontend/my-streamlit-app/Home.py
    ```

4. **Live Trading**

    Open and run cells in `Live_Trading/Live_Trading.ipynb` after appropriate setup and risk assessment.

## 📈 Performance

The platform implements multiple trading strategies:

- **Simons Strategy**: Advanced quantitative trading approach
- **Sun Tzu Strategy**: Tactical market analysis and execution

Performance metrics are continuously monitored and updated based on live trading results.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Alpaca Markets](https://alpaca.markets/) for providing the trading API
- Contributors and maintainers
- The open-source community

## � Academic Publications

This project is supported by rigorous academic research published in peer-reviewed venues:

### Published Research

**[The Financial Torque Hypothesis: Predicting Short-Term Stock Price Movements Using LSTM Neural Networks](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5288444)**

*Authors:* [Guilherme Grancho Duarte Fernandes](https://www.linkedin.com/in/guilhermegrancho/), [Vasco V. R. Serpa Pereira](https://www.linkedin.com/in/vasco-pereira03/)

*Abstract:* This paper introduces the Financial Torque Hypothesis, which asserts that Volume-Weighted Average Price and Trade Count are critical indicators for predicting stock price movements. By incorporating these features into a Long Short-Term Memory Neural Network, our model achieved over 87% accuracy in predicting stock-price increases over a three-hour horizon, based on 21 months of previously unseen test data. We also perform a comprehensive comparative analysis of model performance using two datasets: one that spans the entire trading session—pre-market, regular-market and after-hours—and one confined to regular-market hours. Our results reveal that models trained on full-session data consistently outperform those built on regular-hours-only data, delivering a 15% improvement in predictive accuracy.

**Citation:**

```bibtex
Fernandes, Guilherme Grancho Duarte and Pereira, Vasco, The Financial Torque Hypothesis: 
Predicting Short-Term Stock Price Movements Using LSTM Neural Networks (June 20, 2025). 
Available at SSRN: https://ssrn.com/abstract=5288444
```

### Upcoming Research

#### Integrating The Financial Torque Hypothesis into Advanced Algorithmic Portfolio Management

*Authors:* [Guilherme Grancho Duarte Fernandes](https://www.linkedin.com/in/guilhermegrancho/), [Vasco V. R. Serpa Pereira](https://www.linkedin.com/in/vasco-pereira03/)

*Status:* Set to be published in the coming months

This upcoming publication will detail the practical implementation of the Financial Torque Hypothesis within the Prometheus trading platform and its integration into advanced portfolio management strategies.

## �📧 Contact

**[Guilherme Grancho](https://www.linkedin.com/in/guilhermegrancho/)** - [guilhermegrancho@tecnico.ulisboa.pt](mailto:guilhermegrancho@tecnico.ulisboa.pt) / [guilherme.fernandes25@imperial.ac.uk](mailto:guilherme.fernandes25@imperial.ac.uk)

- Department of Earth Science and Engineering, Imperial College London
- Department of Physics, Instituto Superior Técnico, Lisbon

**[Vasco Pereira](https://www.linkedin.com/in/vasco-pereira03/)** - [vasco.serpa.pereira@tecnico.ulisboa.pt](mailto:vasco.serpa.pereira@tecnico.ulisboa.pt)

- Department of Computer Science and Engineering, Instituto Superior Técnico, Lisbon
