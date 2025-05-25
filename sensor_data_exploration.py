import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Load dataset
#Streamlit cache to speed up data loading
@st.cache_data

# Function to load data locally
def load_data():    
    return pd.read_csv("fndds_ingredient_nutrient_value.csv")

df = load_data()
# Streamlit App Title and Description
st.title("Nutrient Data Analysis Dashboard")
st.markdown("Explore nutrient values, trends, and ingredient-level statistics from USDA dataset.")

# Clean and preprocess
df['Nutrient value'] = pd.to_numeric(df['Nutrient value'], errors='coerce')
df.dropna(subset=['Nutrient value'], inplace=True)

# Sidebar Filters
selected_nutrient = st.sidebar.selectbox("Choose a Nutrient Code", df['Nutrient code'].unique())
filtered_df = df[df['Nutrient code'] == selected_nutrient]

# -------------------- Chart 1: Top 10 Nutrient Values by Ingredient --------------------
st.subheader("Top 10 Ingredients by Nutrient Value")
top10 = filtered_df.groupby('Ingredient description')['Nutrient value'].mean().nlargest(10).reset_index()

fig1 = px.bar(top10, x='Nutrient value', y='Ingredient description', orientation='h',
              title='Top 10 Ingredients with Highest Nutrient Values',
              labels={'Nutrient value': 'Avg Nutrient Value', 'Ingredient description': 'Ingredient'})
st.plotly_chart(fig1)

# -------------------- Chart 2: Nutrient Value Distribution --------------------
st.subheader("Nutrient Value Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df['Nutrient value'], kde=True, bins=30, ax=ax2)
ax2.set_title("Distribution of Nutrient Values")
ax2.set_xlabel("Nutrient Value")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# -------------------- Chart 3: Nutrient Value by Year --------------------
st.subheader("Nutrient Value by SR AddMod Year")
year_data = filtered_df.dropna(subset=['SR AddMod year'])
fig3 = px.box(year_data, x='SR AddMod year', y='Nutrient value',
              title='Nutrient Value Trends by Year',
              labels={'SR AddMod year': 'Year', 'Nutrient value': 'Value'})
st.plotly_chart(fig3)

# -------------------- Chart 4: Derivation Code Comparison --------------------
st.subheader("Nutrient Value by Derivation Code")
fig4 = px.violin(filtered_df, x='Derivation code', y='Nutrient value', box=True, points='all',
                 title='Comparison by Derivation Code')
st.plotly_chart(fig4)


# -------------------- Chart 5: Line Chart by Foundation Year --------------------
st.subheader("Trend of Nutrient Value by Foundation Year")
line_data = filtered_df.dropna(subset=['Foundation year acquired'])
line_data = line_data.groupby('Foundation year acquired')['Nutrient value'].mean().reset_index()

if not line_data.empty:
    fig5 = px.line(line_data, x='Foundation year acquired', y='Nutrient value',
                   title='Average Nutrient Value Over Foundation Years')
    st.plotly_chart(fig5)
else:
    st.info("No foundation year data available for selected nutrient.")

# -------------------- Chart 6: Scatter Plot (SR AddMod Year vs Nutrient Value) --------------------
st.subheader("Scatter: SR AddMod Year vs Nutrient Value")
scatter_data = filtered_df.dropna(subset=['SR AddMod year'])
fig6 = px.scatter(scatter_data, x='SR AddMod year', y='Nutrient value',
                  color='Ingredient description', title='Scatter Plot of Year vs Nutrient Value')
st.plotly_chart(fig6)

# -------------------- Chart 7: Correlation Heatmap --------------------
st.subheader("Correlation Heatmap (Numeric Columns)")
numeric_cols = df.select_dtypes(include='number')

if numeric_cols.shape[1] >= 2:
    corr = numeric_cols.corr()
    fig7, ax7 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax7)
    ax7.set_title("Correlation Heatmap")
    st.pyplot(fig7)
else:
    st.info("Not enough numeric columns for correlation heatmap.")

# -------------------- Download Filtered Data --------------------
st.subheader("Download Filtered Data")
st.markdown("Export filtered nutrient dataset as CSV.")
st.download_button(
    label="📥 Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name='filtered_nutrient_data.csv',
    mime='text/csv'
)

# -------------------- Extra Info --------------------
st.markdown("""
### Notes:
- **Nutrient Code**: Represents different types of nutrients (protein, calcium, etc.)
- **Derivation Code**: How nutrient value was derived.
- **SR AddMod year**: Year of nutrient value addition/modification.
- This dashboard allows filtering by nutrient type for tailored insights.
""")
