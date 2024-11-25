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

st.title("Interactive Table in Streamlit")

# Step 1: Multiselect for columns
selected_columns = st.multiselect(
    "Select columns to display:",
    options=df.columns,
    default=df.columns.tolist()  # Default to all columns
)

# Step 2: Multiselect for rows
row_labels = df.index.astype(str)  # Use index as labels for simplicity
selected_rows = st.multiselect(
    "Select rows to display:",
    options=row_labels,
    default=row_labels.tolist()  # Default to all rows
)

# Step 3: Filter DataFrame based on selections
filtered_df = df.loc[df.index.isin(map(int, selected_rows)), selected_columns]

# Step 4: Display original and filtered DataFrame
st.write("### Original Table:")
st.write(df)

st.write("### Filtered Table:")
st.write(filtered_df)

# Optional: Save selected rows and columns
if st.button("Save Selection"):
    st.write("Selected rows and columns saved!")
    st.write(filtered_df)
