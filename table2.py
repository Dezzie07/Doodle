import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Score": [85, 90, 95, 100]
}
df = pd.DataFrame(data)

st.title("Interactive Table with Streamlit")

# Step 1: Display editable table
st.write("### Edit the table directly:")
edited_df = st.data_editor(
    df,
    num_rows="dynamic",  # Allow adding or removing rows
    use_container_width=True
)

# Step 2: Choose elements for a filtered table
st.write("### Select Specific Rows:")
selected_rows = st.multiselect(
    "Select rows by index:",
    options=edited_df.index,
    default=edited_df.index.tolist()
)

filtered_df = edited_df.loc[selected_rows]

# Step 3: Display filtered table
st.write("### Filtered Table (Based on Your Selection):")
st.write(filtered_df)