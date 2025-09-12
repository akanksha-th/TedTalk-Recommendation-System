import streamlit as st
from recommender import Recommender

st.set_page_config(page_title="Ted Talk Recommender", layout="wide")
st.title("Ted Talk Recommender")

@st.cache_resource
def load_recommender():
    return Recommender()

recommender = load_recommender()

query = st.text_input("What Kind of Ted Talk Are You Looking For?", "")
if query:
    st.write(f"Searhing for **{query}**")
    results = recommender.recommend(query, top_k=5)

    row1, row2 = results[:3], results[3:]

    # --- First row (3 items, centered) ---
    cols = st.columns([1, 3, 3, 3, 1])  # outer 1s are spacers
    for i, r in enumerate(row1):
        with cols[i + 1]:
            st.image(r["thumbnail_url"], width='stretch')
            st.subheader(r["title"])
            st.caption(f"Score: {r['score']:.3f}")
            url = f"https://www.youtube.com/watch?v={r['video_id']}"
            st.markdown(f"[Watch on YouTube]({url})")

    # --- Second row (2 items, centered) ---
    cols = st.columns([1, 3, 3, 1])  # only 2 main columns
    for i, r in enumerate(row2):
        with cols[i + 1]:
            st.image(r["thumbnail_url"], width='stretch')
            st.subheader(r["title"])
            st.caption(f"Score: {r['score']:.3f}")
            url = f"https://www.youtube.com/watch?v={r['video_id']}"
            st.markdown(f"[Watch on YouTube]({url})")