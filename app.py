# app.py
import streamlit as st
import pandas as pd
from scraper import scrape_website

# Set up page configuration
st.set_page_config(page_title="Web Scraper", layout="wide")

# Company logo on the top-left
logo_url = "https://metascifor.com/static/images/Meta%20Scifor%20Icon.png"
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="{logo_url}" alt="Meta Scifor Logo" style="width: 50px; height: 50px; margin-right: 10px;">
        <h1 style="margin: 0;">🔍 Universal Web Scraper & Report Generator</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Description
st.markdown("Enter a website URL to crawl its content and generate a downloadable report.")

# URL input
url = st.text_input("Enter Website URL (e.g., https://example.com)", placeholder="https://")

# Numeric input for max pages
max_pages = st.number_input("Number of pages to crawl", min_value=1, max_value=100, value=5, step=1)

# Scraping button
if st.button("Start Scraping"):
    if url:
        with st.spinner("Scraping in progress..."):
            df = scrape_website(url, max_pages=max_pages)
            if not df.empty:
                df.to_csv("report.csv", index=False)
                st.success(f"✅ Scraping completed! {len(df)} pages scraped.")
                # Blue-colored CSV download button
                st.markdown(
                    f"""
                    <style>
                    .stDownloadButton > button {{
                        background-color: #007bff;
                        color: white;
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                st.download_button(
                    label="📄 Download CSV Report",
                    data=df.to_csv(index=False),
                    file_name="report.csv",
                    mime="text/csv",
                    key="download_csv",
                )
            else:
                st.warning("⚠️ No data was scraped. Make sure the URL is reachable and contains content.")
    else:
        st.error("❌ Please enter a valid URL to proceed.")
