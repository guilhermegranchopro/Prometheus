import streamlit as st

st.set_page_config(layout="wide")

# Function to load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the Tailwind CSS file
local_css("static/css/tailwind.css")

st.title("Hello Streamlit!")
st.write("If you see this, Streamlit is working.")

# Example of using a Tailwind class
st.markdown('<h1 class="text-3xl font-bold underline text-blue-600">Tailwind CSS is also working!</h1>', unsafe_allow_html=True)
