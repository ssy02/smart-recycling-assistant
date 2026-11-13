import json
from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).parent
DATA_FILE = APP_DIR / "data" / "waste_items.json"

st.set_page_config(page_title="Smart Recycling Assistant", page_icon="♻️", layout="wide")

@st.cache_data
def load_items():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

items = load_items()
categories = ["All"] + sorted({item["category"] for item in items})

if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "history" not in st.session_state:
    st.session_state.history = []

st.title("♻️ Smart Recycling Assistant")
st.write("Find an item and learn how to prepare and dispose of it responsibly.")
st.info("Recycling rules can differ by city. This app provides general guidance; always check your local waste collection rules.")

with st.sidebar:
    st.header("Browse")
    page = st.radio("Choose a section", ["Search Waste", "Waste Categories", "Favorites", "Search History", "About"])
    st.divider()
    st.caption(f"{len(items)} sample items in the database")

def show_item(item):
    st.subheader(item["name"])
    st.caption(f'Category: {item["category"]}')
    if item["recyclable"]:
        st.success("Recycling / special collection may be available")
    else:
        st.warning("Usually not accepted in standard recycling")
    st.markdown("**How to prepare**")
    st.write(item["preparation"])
    st.markdown("**How to dispose**")
    st.write(item["disposal"])
    st.markdown("**Tip**")
    st.write(item["tip"])
    if item["name"] in st.session_state.favorites:
        if st.button("★ Remove from favorites", key=f'remove_{item["name"]}'):
            st.session_state.favorites.remove(item["name"])
            st.rerun()
    else:
        if st.button("☆ Add to favorites", key=f'add_{item["name"]}'):
            st.session_state.favorites.append(item["name"])
            st.rerun()

if page == "Search Waste":
    st.header("Search for a waste item")
    query = st.text_input("Enter an item name or keyword", placeholder="Example: plastic bottle")
    if query.strip():
        q = query.strip().lower()
        matches = [
            item for item in items
            if q in item["name"].lower()
            or q in item["category"].lower()
            or any(q in word.lower() for word in item["keywords"])
        ]
        if query.strip() not in st.session_state.history:
            st.session_state.history.insert(0, query.strip())
            st.session_state.history = st.session_state.history[:20]
        if matches:
            st.success(f"{len(matches)} result(s) found.")
            for item in matches:
                with st.expander(f'{item["name"]} — {item["category"]}', expanded=len(matches) == 1):
                    show_item(item)
        else:
            st.warning("No matching item was found. Try a shorter keyword or browse the categories.")
    else:
        st.write("Popular examples")
        cols = st.columns(3)
        for col, name in zip(cols, ["Plastic bottle", "Cardboard box", "Aluminum can"]):
            col.markdown(f"**{name}**")

elif page == "Waste Categories":
    st.header("Browse by category")
    selected = st.selectbox("Select a category", categories)
    shown = items if selected == "All" else [item for item in items if item["category"] == selected]
    st.write(f"{len(shown)} item(s)")
    for item in shown:
        with st.expander(f'{item["name"]} — {"Recyclable / special collection" if item["recyclable"] else "General waste"}'):
            show_item(item)

elif page == "Favorites":
    st.header("Your favorite items")
    if not st.session_state.favorites:
        st.write("You have not saved any favorites yet. Search for an item and select “Add to favorites”.")
    else:
        for name in list(st.session_state.favorites):
            item = next((x for x in items if x["name"] == name), None)
            if item:
                with st.expander(item["name"]):
                    show_item(item)

elif page == "Search History":
    st.header("Recent searches")
    if not st.session_state.history:
        st.write("Your search history is empty.")
    else:
        for term in st.session_state.history:
            st.write(f"• {term}")
        if st.button("Clear search history"):
            st.session_state.history = []
            st.rerun()

else:
    st.header("About this project")
    st.write(
        "Smart Recycling Assistant is a student term project designed to help users "
        "find general recycling information in one place. It includes item search, "
        "recycling instructions, category browsing, favorites, and recent search history."
    )
    st.markdown("**Technology**")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- JSON data file")
    st.markdown("**Future improvement**")
    st.write("An AI image-recognition feature may be added in a future version after the basic functions are completed.")
    st.markdown("**Important note**")
    st.write("This application is an educational guide, not an official waste-disposal authority. Local rules may be different.")
