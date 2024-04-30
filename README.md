# Software-Developer-Salary-Predictor-and-Explorer



This project is a software developer salary predictor and explorer, built using Python and Streamlit. It utilizes machine learning techniques to predict salaries based on various factors such as country, education level, and years of professional coding experience. Additionally, it provides data exploration features to analyze salary trends across different countries and years of experience using the Stack Overflow Developer Survey 2020 dataset.

## Features

- **Salary Prediction**: Input your country, education level, and years of experience to get an estimate of your potential salary as a software developer.
- **Data Exploration**: Explore salary trends based on different factors such as country and years of experience through interactive visualizations.
- **Machine Learning Model**: The salary prediction is powered by a linear regression model trained on the Stack Overflow survey data.
- **User-friendly Interface**: The web application is built using Streamlit, providing an intuitive interface for users to interact with.

## Usage

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the Streamlit app by executing `streamlit run app.py` in your terminal.
4. Access the application in your web browser at the provided URL (usually http://localhost:8501).

## Data Source

The Stack Overflow Developer Survey 2020 dataset is used for this project. It provides insights into the demographics, technologies, and career preferences of software developers around the world.

## Project Structure

- `app.py`: Main Python script containing the Streamlit application code.
- `save_steps.pkl`: Serialized machine learning model and encoding steps using pickle.
- `survey_results_public.csv`: Stack Overflow Developer Survey 2020 dataset.
- `requirements.txt`: List of Python packages required for running the application.

## Contributors

- Murali Monish Addagarla(https://github.com/yourusername)

