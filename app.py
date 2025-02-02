import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Add title
st.title("Data Analysis Application")
st.subheader("This is the Data Analysis Application to analyze the dataset and plot the data.") 

# Create a dropdown list to choose the dataset
dataset_name = st.selectbox("Select a dataset", ["tips", "iris", "titanic", "Upload your own dataset"])

# Load the selected dataset
if dataset_name == "tips":
    data = sns.load_dataset("tips")
elif dataset_name == "iris":
    data = sns.load_dataset("iris")
elif dataset_name == "titanic":
    data = sns.load_dataset("titanic")
elif dataset_name == "Upload your own dataset":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    else:
        data = None

# Display the dataset
if data is not None:
    st.write(data.head())
    st.write("Shape of the dataset:", data.shape)
    st.write("Columns of the dataset:", data.columns)
    st.write("Number of the columns of the dataset:", len(data.columns))
    st.write("Number of the rows of the dataset:", len(data))
    st.write("Summary of the dataset:", data.describe())
    st.write("Missing values of the dataset:", data.isnull().sum())
    st.write("Data types of the dataset:", data.dtypes)

    # Select the specific column for the x_axis and y_axis from the dataset
    x_axis = st.selectbox("Select the x-axis", data.columns)
    y_axis = st.selectbox("Select the y-axis", data.columns)
    plot_type = st.selectbox("Select the plot type", ["scatter", "line", "bar", "box", "hist", "kde", "violin", "pairplot"])

    # Plot the data
    if plot_type == "pairplot":
        fig = sns.pairplot(data)
        st.pyplot(fig)
    else:
        fig, ax = plt.subplots()
        if plot_type == "scatter":
            sns.scatterplot(x=x_axis, y=y_axis, data=data, ax=ax)
        elif plot_type == "line":
            sns.lineplot(x=x_axis, y=y_axis, data=data, ax=ax)
        elif plot_type == "bar":
            sns.barplot(x=x_axis, y=y_axis, data=data, ax=ax)
        elif plot_type == "box":
            sns.boxplot(x=x_axis, y=y_axis, data=data, ax=ax)
        elif plot_type == "hist":
            sns.histplot(data[x_axis], ax=ax)
        elif plot_type == "kde":
            sns.kdeplot(data[x_axis], ax=ax)
        elif plot_type == "violin":
            sns.violinplot(x=x_axis, y=y_axis, data=data, ax=ax)

        # Display the plot
        st.pyplot(fig)
else:
    st.write("No dataset loaded. Please upload a file or select a dataset from the dropdown.")

# Add balloons
st.balloons()

# Add the footer
st.write("Created by Wazir Kifayat")
st.write("Thank you for using this application")