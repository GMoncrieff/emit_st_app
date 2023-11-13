import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    df = pd.read_csv('df_cleaned.csv')

    # Selector for choosing Categories
    selected_categories = st.multiselect('Select Categories', df['Category'].unique(), default=df['Category'].unique())

    if selected_categories:
        # Filtering dataframe based on selected Categories
        filtered_df = df[df['Category'].isin(selected_categories)]

        # Creating a Plotly figure with lines
        fig = px.line(filtered_df, x='wavelengths', y='reflectance', color='Category', line_group='ID',
                      labels={'reflectance': 'Reflectance', 'wavelengths': 'Wavelengths'},
                      title='Reflectance vs Wavelengths')

        # Defining the excluded ranges
        excluded_ranges = [(1767, 1966), (1321, 1438)]

        # Adding white rectangles to cover the excluded ranges
        for start, end in excluded_ranges:
            fig.add_vrect(x0=start, x1=end, fillcolor='white', opacity=1, layer='above', line_width=0)

        fig.update_layout(
            autosize=True,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis_rangeslider_visible=True
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Please select at least one category.")

if __name__ == "__main__":
    main()
