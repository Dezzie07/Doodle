from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import streamlit as st

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Score": [85, 90, 95, 100]
}
df = pd.DataFrame(data)

st.title("Interactive Table with Selection")

# Configure AgGrid
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection("multiple", use_checkbox=True)  # Enable row selection
grid_options = gb.build()

# Display AgGrid table
grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    update_mode="MODEL_CHANGED",
    enable_enterprise_modules=False,
)

# Get selected rows
selected = grid_response["selected_rows"]

# Display selected rows
st.write("### Selected Rows:")
st.write(pd.DataFrame(selected))