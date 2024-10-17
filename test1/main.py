import streamlit as st
from scrape import scrape_website



st.title("AI Scraper")

url = st.text_input("Enter URL: ")

if st.button("Scrape Site"):
    st.write("Scraping website...")
    result = scrape_website(url)
    print(result)

