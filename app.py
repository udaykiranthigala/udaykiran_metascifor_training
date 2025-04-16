# app.py
import streamlit as st
import pandas as pd
from scraper import scrape_website

st.set_page_config(page_title="Web Scraper", layout="wide")
st.title("🔍 Universal Web Scraper & Report Generator")

st.markdown("Enter a website URL to crawl its content and generate a downloadable report.")

url = st.text_input("Enter Website URL (e.g., https://example.com)", placeholder="https://")

max_pages = st.slider("Max number of subpages to crawl", 1, 100, 30)

if st.button("Start Scraping"):
    if url:
        with st.spinner("Scraping in progress..."):
            df = scrape_website(url, max_pages=max_pages)
            if not df.empty:
                df.to_csv("report.csv", index=False)
                st.success(f"✅ Scraping completed! {len(df)} pages scraped.")
                st.dataframe(df)
                st.download_button("📄 Download CSV Report", df.to_csv(index=False), "report.csv", "text/csv")
            else:
                st.warning("⚠️ No data was scraped. Make sure the URL is reachable and contains content.")
    else:
        st.error("❌ Please enter a valid URL to proceed.")
