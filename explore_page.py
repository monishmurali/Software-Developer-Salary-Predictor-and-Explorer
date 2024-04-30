import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'other'
    return categorical_map

def changeExp(yearsExp):
    if yearsExp =='Less than 1 year':
        return 0.5
    if yearsExp == 'More than 50 years':
        return 50
    return float(yearsExp)

def changeEdu(x):
    if 'B.A.' in x:
        return 'Bachelors degree'
    if 'M.A.' in x:
        return 'Masters degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post Graduation'
    return 'Less than a Bachelors'

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    cat_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(cat_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "other"]
    df["YearsCodePro"] = df["YearsCodePro"].apply(changeExp)
    df['EdLevel'] = df['EdLevel'].apply(changeEdu)
  
    return df

df = load_data()

def show_explore():
    st.title("Explore Software Engineer Salary")

    st.write(
        """
     ### Stack Overflow Developer Survey 2020

     """
    )
    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()

    # Convert data to list
    data_values = data.values.tolist()
    data_labels = data.index.tolist()

    ax1.pie(data_values, labels=data_labels, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.write(""" ### Number of data from different countries""")
    st.pyplot(fig1)

    st.write("""
             ### Mean Salary Based on country
             """)
    df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write("""
             ### Mean Salary Based on Experience
             """)

    df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)




