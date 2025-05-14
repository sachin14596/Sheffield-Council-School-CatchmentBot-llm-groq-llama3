import streamlit as st
import geopandas as gpd
from catchment_agent import run_catchment_agent

# Set up Streamlit page
st.set_page_config(page_title="CatchmentBot AI", layout="centered")
st.title("🏫 CatchmentBot AI - Sheffield School Planning")

st.markdown("Ask me anything about school catchments, fairness, overlap, transport burden, or planning scenarios.")

# -------------------- Step 1: Load and Show GeoJSON Data --------------------
# Load GeoJSON data
gdf = gpd.read_file('cleaned_catchments.geojson')

# Show sample data (first 5 rows of the dataframe)
st.markdown("### 🗺️ Sample Catchment Data")
st.write(gdf.head())  # Display first 5 rows of data
# ---------------------------------------------------------------------------

# Initialize session state history if it doesn't exist
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("🔍 Your question:")

# Run the agent
if user_input:
    # Append user input to history
    st.session_state.history.append(user_input)
    st.markdown("---")
    with st.spinner("🤖 Agent is thinking..."):
        try:
            answer = run_catchment_agent(user_input)
            st.success("✅ Answer: ")
            st.markdown(f"**{answer}**")
        except Exception as e:
            st.error("❌ Agent could not return a valid answer.")
            st.code(str(e))

    st.markdown("---")
    with st.expander("🧾 Chat History"):
        for q in st.session_state.history:
            st.markdown(f"- {q}")

    with st.expander("🛠️ Raw Agent Response"):
        st.json(answer)
