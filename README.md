# MINI PROJECT 

## Project Description: Car Price Prediction Model Development and Deployment

This project focuses on developing a car price prediction model using data collected from cardekho.com through web scraping techniques. The collected data undergoes thorough data cleaning and feature engineering processes. Multiple models are constructed and evaluated, and the one with the highest accuracy is selected for deployment. Additionally, a frontend web page is created to provide a user-friendly interface, and the model is deployed using Flask.

### Data Collection:
Data is collected by implementing web scraping techniques on cardekho.com, a comprehensive online platform that provides detailed information about various car models, their specifications, and prices. The web scraping process extracts relevant data in a structured format for further analysis.

### Data Cleaning and Feature Engineering:
To ensure data quality and reliability, a rigorous data cleaning process is performed. This involves handling missing values, resolving inconsistencies, and removing irrelevant information. Feature engineering techniques are applied to extract meaningful features and enhance the predictive power of the models.

### Model Development:
Several models are developed to predict car prices based on the available features and specifications. Various machine learning algorithms and techniques, such as regression, are employed to create accurate price prediction models. The models are trained, evaluated, and compared to identify the one with the highest accuracy and performance.

### Model Deployment:
The model with the highest accuracy is selected for deployment. To provide a seamless user experience, a frontend web page is designed and implemented. This interface allows users to input car specifications and receive predicted prices based on the deployed model. The model is integrated into a Flask web application, ensuring efficient deployment and smooth interaction with the users.

Overall, this project demonstrates a comprehensive pipeline from data collection through web scraping to data cleaning, feature engineering, model development, and model deployment through a user-friendly web interface. Its primary objective is to enable users to accurately predict car prices based on various features, aiding car buyers, sellers, and automotive enthusiasts in making informed decisions.

### Getting Started
To run the deployed application locally:

1) Clone this repository to your local machine.
2) Make virtual enviurnment (python -m venv {name of your enviournment})
3) Activate the virtual enviournment ({name of your enviournment}\Scripts\activate)
4) Install Required dependencies (python setup.py)
5) Run the Flask application (python app.py)
6) Access the application in your web browser at `http://127.0.0.1:5000`.

## Contribution
If you would like to contribute to this project, you can:

- Improve the model's performance by experimenting with hyperparameters.
- Expand the dataset or implement data augmentation techniques.
- Enhance the user interface of the Flask application.
- Refactor and optimize the codebase for better maintainability.

Feel free to fork this repository, make changes, and submit pull requests.
