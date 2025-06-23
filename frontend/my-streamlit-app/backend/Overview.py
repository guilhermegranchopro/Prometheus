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
    st.markdown("# 🚀 Prometheus Trading Research Platform")
    
    st.markdown("""
    An advanced algorithmic trading research platform achieving **87%+ accuracy** in stock price predictions through our published **Financial Torque Hypothesis**. 
    This open-source platform combines rigorous academic research with practical trading applications.
    """)
    
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Research Accuracy", "87%+", "Published SSRN")
    with col2:
        st.metric("Test Data", "21 months", "Unseen validation")
    with col3:
        st.metric("Data Sources", "IEX + SIP", "Multiple feeds")
    with col4:
        st.metric("License", "MIT", "Open source")
    
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
            
            Our research demonstrates that Volume-Weighted Average Price (VWAP) and Trade Count are critical indicators for predicting stock price movements. Using LSTM neural networks, we achieved **over 87% accuracy** in predicting stock price increases over a three-hour horizon with 21 months of previously unseen test data.
            
            **Key Finding:** Models trained on full-session data (pre-market + regular + after-hours) outperform regular-hours-only models by 15%.
            """)
        
        with col2:
            st.metric("Accuracy", "87%+", "Published research")
            st.metric("Validation", "21 months", "Unseen data")
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
        - 🔌 Alpaca Markets API integration with rate limiting
        - 📡 Multiple data feeds (IEX, SIP) with extended hours support
        - 💾 Automated data collection and scalable storage
        - 📊 Comprehensive market data analysis tools
        - ⏰ Real-time and historical data processing
        """)
    
    with tab3:
        st.markdown("""
        **User Interface & Research Tools**
        - 🖥️ Interactive Streamlit web dashboard
        - 📈 Advanced data visualization with Plotly
        - 📓 Jupyter notebooks for strategy research
        - � Portfolio monitoring and performance tracking
        - 🛡️ Risk management interface and tools
        """)
    
    with tab4:
        st.markdown("""
        **Trading Strategy Research**
        - 🎲 **Simons Strategy**: Quantitative mathematical modeling (`Simons/backend/`)
        - ⚔️ **Sun Tzu Strategy**: Tactical market analysis (`Sun_Tzu/backend/`)
        - � **Financial Torque**: Published LSTM-based predictions
        - 📊 Multi-strategy comparative analysis framework
        - 🧪 Live trading research environment
        """)
    
    st.markdown("---")

    # Project Structure - Simplified
    st.markdown("## 📁 Project Structure")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.code("""
Prometheus/
├── 📊 Data/                    # Market data (IEX, SIP, Regular Hours)
├── 🖥️ frontend/               # Streamlit web application
├── 🤖 Models/                 # ML models and analysis notebooks
├── 🧪 Live_Trading/           # Live trading research environment
├── 🎲 Simons/                 # Quantitative strategy research
├── ⚔️ Sun_Tzu/               # Tactical strategy research
├── 🖼️ Assets/                # Project assets and images
├── 📄 requirements.txt        # Python dependencies
└── 📋 CITATION.cff           # Academic citation information
        """, language="text")
    
    with col2:
        st.markdown("**📊 Data Sources**")
        st.markdown("- IEX Cloud feed")
        st.markdown("- SIP (Securities Information Processor)")
        st.markdown("- Extended & regular trading hours")
        
        st.markdown("**🔬 Research Areas**")
        st.markdown("- Financial Torque Hypothesis")
        st.markdown("- Quantitative modeling")
        st.markdown("- Tactical analysis")
        st.markdown("- Portfolio management")
    
    st.markdown("---")

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
        st.markdown("**� Active Development**")
        st.markdown("""
        - ✅ LSTM Neural Networks (87%+ accuracy)
        - ✅ Multi-feed data infrastructure 
        - 🔄 Advanced portfolio management
        - 🔄 Next.js frontend migration
        - 📅 API development planning
        """)
    
    with roadmap_col3:
        st.markdown("**� Timeline Milestones**")
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
        - � guilhermegrancho@tecnico.ulisboa.pt
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
Fernandes, G.G.D. and Pereira, V., 
The Financial Torque Hypothesis: Predicting 
Short-Term Stock Price Movements Using LSTM 
Neural Networks (June 20, 2025). 
Available at SSRN: https://ssrn.com/abstract=5288444
            """, language="text")
        
        with cite_col2:
            st.markdown("**Software Citation:**")
            st.code("""
@software{prometheus_2025,
  author = {Grancho, Guilherme and Pereira, Vasco},
  title = {Prometheus Trading Research Platform},
  year = {2025},
  url = {https://github.com/your-repo/Prometheus}
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
            Our LSTM model achieved **87%+ accuracy** over 3-hour horizons with 21 months of validation data.
            """)
        
        with st.expander("📊 What strategies are researched?"):
            st.markdown("""
            - **Financial Torque**: Published LSTM research (87%+ accuracy)
            - **Simons**: Quantitative mathematical modeling
            - **Sun Tzu**: Tactical market analysis
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
