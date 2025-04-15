# Prometheus

<div align="center">
  <img src="Assets/logo.jpg" alt="Prometheus Logo" width="700"/>
  
  [![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
  [![ API](https://img.shields.io/badge/%20API-v2-blue.svg)](https://.markets/)
</div>

## 🚀 Overview

Prometheus is a sophisticated algorithmic trading platform that leverages the  Markets API to execute automated trading strategies. This project combines advanced data analysis, machine learning models, and real-time market data to make informed trading decisions.

## ✨ Features

- **Real-time Market Data Integration**
  - Seamless integration with  Markets API
  - High-frequency data collection with rate limit management
  - Support for multiple timeframes (1Min, 5Min, 15Min, etc.)

- **Advanced Trading Models**
  - SIP (Securities Information Processor) based analysis
  - IEX (Investors Exchange) data integration
  - Custom trading strategies implementation
  - Machine learning model integration

- **Data Analysis & Visualization**
  - Comprehensive market data analysis
  - Interactive data visualization
  - Performance metrics and reporting
  - Historical data analysis

- **Risk Management**
  - Position sizing algorithms
  - Stop-loss and take-profit mechanisms
  - Portfolio diversification strategies
  - Risk assessment tools

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Prometheus.git
cd Prometheus
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your  API credentials:
   - Create an account at [ Markets](https://.markets/)
   - Generate your API keys
   - Create a `Settings/API_Keys.txt` file with your credentials:
     ```
     YOUR_API_KEY
     YOUR_SECRET_KEY
     https://api..markets
     ```

## 📊 Project Structure

```
Prometheus/
├── /              #  API integration and trading logic
├── Data/               # Market data storage and processing
├── Images/             # Project images and logos
├── Models/             # Trading models and strategies
│   ├── IEX/           # IEX-specific models
│   └── SIP/           # SIP-based models
├── Report/             # Analysis reports and visualizations
│   ├── IEX/           # IEX analysis reports
│   └── SIP/           # SIP analysis reports
└── Settings/           # Configuration files and API keys
```

## 🚀 Usage

1. **Data Collection**
```python
from .Legacy import _autentification

# Initialize API connection
api = _autentification('Settings/API_Keys.txt')

# Fetch historical data
data = get_all_data(symbol='AAPL', timeframe='1Min')
```

2. **Running Trading Strategies**
```python
# Import your preferred strategy
from Models.SIP import your_strategy

# Execute the strategy
strategy = your_strategy(data)
results = strategy.execute()
```

## 📈 Performance

The platform has been tested with various trading strategies and timeframes. Key performance metrics include:

- Sharpe Ratio: [On Progress]
- Maximum Drawdown: [On Progress]
- Annual Return: [On Progress]
- Win Rate: [On Progress]

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

- [ Markets](https://.markets/) for providing the trading API
- Contributors and maintainers
- The open-source community

## 📧 Contact

Guilherme Grancho - guilhermegrancho@tecnico.ulisboa.pt

Vasco Pereira - vasco.serpa.pereira@tecnico.ulisboa.pt