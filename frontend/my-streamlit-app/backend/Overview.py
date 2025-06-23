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


def main_overview():
    # Centered Logo
    col1, col2, col3 = st.columns([0.5, 2, 0.5])
    with col2:
        try:
            st.image(get_logo_path(), use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Could not load logo. Error: {e}")

    # Hero Section
    st.markdown("# 🚀 Welcome to Prometheus")
    
    st.markdown("""
    An advanced algorithmic trading research platform achieving **87%+ accuracy** in stock price predictions through our published **Financial Torque Hypothesis**. 
    This open-source platform combines rigorous academic research with practical trading applications.
    """)
    
    st.markdown("---")

    # Academic Publications - Move to prominent position
    st.markdown("## 🪶 Published Research")
    
    with st.expander("📄 The Financial Torque Hypothesis - Published on SSRN", expanded=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("""
            **[The Financial Torque Hypothesis: Predicting Short-Term Stock Price Movements Using LSTM Neural Networks](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5288444)**
            
            **Authors:** [Guilherme Grancho](https://www.linkedin.com/in/guilhermegrancho/) & [Vasco Pereira](https://www.linkedin.com/in/vasco-pereira03/)  
            **Published:** June 20, 2025 - SSRN
            
            **Abstract:** This paper introduces the Financial Torque Hypothesis, which asserts that Volume-Weighted Average Price and Trade Count are critical indicators for predicting stock price movements. By incorporating these features into a Long Short-Term Memory Neural Network, our model achieved **over 87% accuracy** in predicting stock-price increases over a three-hour horizon, based on 21 months of previously unseen test data. 
            
            We also perform a comprehensive comparative analysis of model performance using two datasets: one that spans the entire trading session—pre-market, regular-market and after-hours—and one confined to regular-market hours. Our results reveal that models trained on full-session data consistently outperform those built on regular-hours-only data, delivering a **15% improvement** in predictive accuracy.
            """)
        
        with col2:
            st.metric("Accuracy", "87%+", "Published research")
            st.metric("Test", "21 months", "Unseen data")
            st.metric("Horizon", "3 hours", "Real-time")
            st.metric("Improvement", "15%", "Full vs RTH")
    
    with st.expander("🔬 Upcoming Research - Advanced Portfolio Management"):
        st.markdown("""
        **Integrating The Financial Torque Hypothesis into Advanced Algorithmic Portfolio Management**
        
        **Status:** 🔄 75% Complete - Expected publication in coming months
        
        This upcoming research will detail the practical implementation of our Financial Torque Hypothesis within advanced portfolio management strategies, covering optimization techniques and risk management integration.
        """)
        st.progress(0.75, text="Research Progress: 75% Complete")
    
    st.markdown("---")

    # Platform Capabilities - Consolidated section
    st.markdown("## ⚡ Platform Capabilities")
    
    # Core capabilities in tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🤖 ML & Research", 
        "📊 Data & Infrastructure", 
        "🖥️ Interface & Tools",
        "📈 Trading Strategies"
    ])
    
    with tab1:
        st.markdown("""
        **Machine Learning & Research**
        - 🧠 TensorFlow LSTM neural networks achieving 87%+ accuracy
        - 📊 Financial Torque Hypothesis implementation
        - 🔬 Academic research integration and validation
        - 📈 Real-time predictive modeling capabilities
        - 🎯 Three-hour prediction horizon with 21-month validation
        """)
    
    with tab2:
        st.markdown("""
        **Data Infrastructure & Analysis**
        - 🔌 Alpaca Markets API integration (v3.2.0) with rate limiting
        - 📡 Multiple data feeds (IEX, SIP) with extended hours support
        - 💾 Automated data collection and scalable storage
        - 📊 Comprehensive analysis using pandas, numpy, and scipy
        - ⏰ Real-time and historical data processing
        - 📈 Advanced visualization with matplotlib, plotly, and altair
        """)
    
    with tab3:
        st.markdown("""
        **User Interface & Research Tools**
        - 🖥️ Interactive Streamlit web dashboard
        - 📈 Advanced data visualization with Plotly
        - 📓 Jupyter notebooks for strategy research
        - 🔍 Portfolio monitoring and performance tracking
        - 🛡️ Risk management interface and tools
        - 🔧 Additional tools: scikit-learn, joblib, fuzzywuzzy
        """)
    
    with tab4:
        st.markdown("""
        **Trading Strategy Research**
        - 🎲 **Simons Strategy**: Quantitative mathematical modeling (`Simons/backend/`)
        - ⚔️ **Sun Tzu Strategy**: Tactical market analysis (`Sun_Tzu/backend/`)
        - 🔬 **Financial Torque**: Published LSTM-based predictions
        - 📊 Multi-strategy comparative analysis framework
        - 🧪 Live trading research environment (`Live_Trading/`)
        """)
    
    st.markdown("---")
    
    # Technology Stack - New section
    st.markdown("## 🛠️ Technology Stack")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("**🐍 Core Python (3.10+)**")
        st.markdown("""
        - **TensorFlow** - Deep learning framework
        - **Pandas & NumPy** - Data manipulation
        - **Scikit-learn** - Machine learning tools
        - **SciPy** - Scientific computing
        """)
    
    with tech_col2:
        st.markdown("**📊 Visualization & Analysis**")
        st.markdown("""
        - **Streamlit** - Web application framework
        - **Plotly** - Interactive visualizations
        - **Matplotlib** - Static plotting
        - **Altair** - Statistical visualization
        """)
    
    with tech_col3:
        st.markdown("**🔌 APIs & Integration**")
        st.markdown("""
        - **Alpaca API v3.2.0** - Trading data
        - **Polygon API** - Market data
        - **Python-Dotenv** - Configuration
        - **Joblib** - Model persistence
        """)

    # Getting Started - Simplified
    st.markdown("## 🚀 Getting Started")
    
    start_tab1, start_tab2, start_tab3 = st.tabs(["⚙️ Installation", "🖥️ Running the App", "🔬 Research Setup"])
    
    with start_tab1:
        st.markdown("**Quick Setup:**")
        st.code("""
# Clone and setup
git clone [repository-url]
cd Prometheus
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
        """, language="bash")
        
    with start_tab2:
        st.markdown("**Launch the Dashboard:**")
        st.code("streamlit run frontend/my-streamlit-app/Home.py", language="bash")
        st.markdown("📍 Navigate between sections using the top navigation bar")
        
    with start_tab3:
        st.markdown("**For Trading Research:**")
        st.markdown("""
        1. 🔑 **Set up Alpaca API**: Create account at [Alpaca Markets](https://alpaca.markets/)
        2. 📓 **Explore Notebooks**: Check `Simons/backend/` and `Sun_Tzu/backend/` 
        3. 🧪 **Live Research**: Open `Live_Trading/Live_Trading.ipynb` for live analysis
        4. 📊 **Data Analysis**: Review processed data in `Data/` directories
        5. ⚙️ **Configure credentials**: Set up in `Simons/Settings/` or environment variables
        """)
    
    st.markdown("---")

    # Development Roadmap
    st.markdown("## 🛣️ Development Roadmap")
    
    roadmap_col1, roadmap_col2, roadmap_col3 = st.columns(3)
    
    with roadmap_col1:
        st.markdown("**📊 Current Research**")
        st.progress(1.0, text="Financial Torque Hypothesis - Published ✅")
        st.progress(0.75, text="Portfolio Management Research - 75%")
        st.progress(0.3, text="Enhanced ML Models - Planning")
    
    with roadmap_col2:
        st.markdown("**📈 Active Development**")
        st.markdown("""
        - ✅ LSTM Neural Networks (87%+ accuracy)
        - ✅ Multi-feed data infrastructure 
        - 🔄 Advanced portfolio management
        - 🔄 Next.js frontend migration
        - 📅 API development planning
        """)
    
    with roadmap_col3:
        st.markdown("**📆 Timeline Milestones**")
        st.markdown("""
        - **Q3 2025**: Second paper publication
        - **Q4 2025**: Frontend modernization
        - **Q1 2026**: Enhanced ML models
        - **Q2 2026**: REST API development
        - **Q3 2026**: Production integration
        """)
    
    st.markdown("---")
    
    # Authors & Contact
    st.markdown("## 👥 Authors & Contact")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**👨‍🎓 Guilherme Grancho**")
        st.markdown("""
        - 🏫 Imperial College London (Earth Science & Engineering)
        - 🏫 Instituto Superior Técnico (Physics)
        - 🔗 [LinkedIn](https://www.linkedin.com/in/guilhermegrancho/)
        - 📧 guilhermegrancho@tecnico.ulisboa.pt
        - 📧 guilherme.fernandes25@imperial.ac.uk
        """)
    
    with col2:
        st.markdown("**👨‍💻 Vasco Pereira**")
        st.markdown("""
        - 🏫 Instituto Superior Técnico (Computer Science)
        - 🔗 [LinkedIn](https://www.linkedin.com/in/vasco-pereira03/)
        - 📧 vasco.serpa.pereira@tecnico.ulisboa.pt
        """)
    
    st.markdown("---")
    
    # Contributing & License
    st.markdown("## 🤝 Contributing & License")
    
    contrib_col1, contrib_col2 = st.columns(2)
    
    with contrib_col1:
        st.markdown("**🔧 Contributing**")
        st.markdown("""
        1. Fork the repository
        2. Create feature branch (`git checkout -b feature/AmazingFeature`)
        3. Commit changes (`git commit -m 'Add feature'`)
        4. Push branch (`git push origin feature/AmazingFeature`)
        5. Open Pull Request
        """)
    
    with contrib_col2:
        st.markdown("**📄 License & Acknowledgments**")
        st.markdown("""
        - 📋 **MIT License** - Open source and free to use
        - 🙏 **Thanks to:** [Alpaca Markets](https://alpaca.markets/) API
        - 🌟 **Open Source Community** contributions
        """)
    
    st.markdown("---")
    
    # Citation Information
    st.markdown("## 📚 Citation Information")
    
    with st.expander("📖 How to Cite This Work", expanded=False):
        cite_col1, cite_col2 = st.columns(2)
        
        with cite_col1:
            st.markdown("**Academic Paper:**")
            st.code("""
Fernandes, Guilherme Grancho Duarte and Pereira, Vasco, 
The Financial Torque Hypothesis: Predicting Short-Term 
Stock Price Movements Using LSTM Neural Networks 
(June 20, 2025). 
Available at SSRN: https://ssrn.com/abstract=5288444
            """, language="text")
            
            st.markdown("**Simple Software Citation:**")
            st.code("""
Grancho, G., & Pereira, V. (2025). 
Prometheus (Version 1.0.0) [Computer software]. 
https://github.com/guilhermegranchopro/Prometheus
            """, language="text")
        
        with cite_col2:
            st.markdown("**BibTeX Software Citation:**")
            st.code("""
@software{prometheus_2025,
  author = {Grancho, Guilherme and Pereira, Vasco},
  title = {Prometheus},
  version = {1.0.0},
  date = {2025-04-20},
  url = {https://github.com/guilhermegranchopro/Prometheus},
  license = {MIT},
  abstract = {Prometheus is a sophisticated algorithmic trading platform that leverages the Alpaca Markets API to execute automated trading strategies. This project combines advanced data analysis, machine learning models, and real-time market data to make informed trading decisions.}
}
            """, language="bibtex")
    
    st.markdown("---")
    
    # Frequently Asked Questions
    st.markdown("## ❓ Frequently Asked Questions")
    
    faq_col1, faq_col2 = st.columns(2)
    
    with faq_col1:
        with st.expander("🤖 What is the Financial Torque Hypothesis?"):
            st.markdown("""
            Our research hypothesis that **VWAP and Trade Count** are critical for predicting stock movements. 
            Our LSTM model achieved **87%+ accuracy** over 3-hour horizons with 21 months of test data.
            """)
        
        with st.expander("📊 What strategies are researched?"):
            st.markdown("""
            - **Financial Torque**: Published LSTM research (87%+ accuracy)
            - **Simons**: Quantitative mathematical modeling
            - **Sun Tzu**: Tactical market analysis
            
            Performance metrics can be analyzed through the provided research notebooks with structured model management and evaluation.
            """)
    
    with faq_col2:
        with st.expander("🔬 Is this academic or commercial?"):
            st.markdown("""
            **Primarily academic** - MIT licensed research platform with published papers, 
            open-source contributions, and rigorous validation methodologies.
            """)
        
        with st.expander("🚀 How to get started?"):
            st.markdown("""
            1. Clone repo and install requirements
            2. Run `streamlit run frontend/my-streamlit-app/Home.py`
            3. Set up Alpaca API for research
            4. Explore Jupyter notebooks
            """)
    
    # Success banner
    st.success("""
    🏆 **Research Achievement**: 87%+ accuracy in stock price predictions • Published on SSRN June 2025 • Open source MIT license
    """)
