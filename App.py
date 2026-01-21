import streamlit as st
import requests
from datetime import datetime


# Page Configuration

st.set_page_config(
    page_title="Joke Generator App",
    page_icon="😂",
    layout="centered"
)



st.title("😂 Joke Generator App")
st.caption("Interactive joke app using public REST API (JokeAPI)")



CATEGORIES = [
    "Any",
    "Programming",
    "Misc",
    "Dark",
    "Pun",
    "Spooky",
    "Christmas"
]

# UI Category Selection

selected_category = st.selectbox(
    "Select Joke Category",
    CATEGORIES
)

# API Fetch Function

def fetch_joke(category):
    url = f"https://v2.jokeapi.dev/joke/{category}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()



if st.button("🎲Press for Joke"):
    joke_data = fetch_joke(selected_category)

    if joke_data is None:
        st.error("⚠️ Failed to fetch joke. Please try again.")
    else:
        if joke_data["type"] == "single":
            st.success(joke_data["joke"])
        else:
            st.success(joke_data["setup"])
            st.info(joke_data["delivery"])

        # Metadata
        st.caption(
            f" Category: {joke_data.get('category')} | "
            f" Type: {joke_data.get('type')} | "
            f" Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )



with st.expander(" How this app works"):
    st.markdown("""
- User selects joke category from the UI  
- Fetches jokes from **JokeAPI** dynamically  
- Handles **single & two-part** joke formats  
- Demonstrates API integration with Streamlit  
    """)

# Footer

st.markdown("---")
st.caption("Built with ❤️ using Python, Streamlit & REST APIs")



