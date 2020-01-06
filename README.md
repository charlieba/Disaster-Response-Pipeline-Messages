# Disaster Response Pipeline Project

## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#project-motivation)
3. [File Descriptions](#file-descriptions)
4. [How to Interact with the project](#how-to-interact-with-the-project)
5. [Results](#results)
6. [Licensing, Authors, Acknowledgements, etc.](#licensing-authors-acknowledgements)

## Installation:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Project Motivation
My motivation for this project was take a look of the Airbnb public data on Seattle, and answer the next questions:
1. What is the most expensive city in Seattle for rent an Airbnb?
2. What is the better date to travel to Seattle and find a good price for an Airbnb?
3. What city of Seattle has more options to look for a Airbnb that accomplish my requirements?
4. What variables are important for predicting the price of an Airbnb in Seattle?

## File Descriptions
* **Knowing the datasets.ipynb**
The objective of this Jupyter Notebook is get an idea of how is the data, and what are the important variables to answer our questions. In this file i have used basics functions to know the data, like the _describe_ function and _head_. 
* **Mean of price per location and Distribution.ipynb**
The objective of this Jupyter Notebook is answer the question about the mean of price per city and know the distributions of Airbnb around Seattle. In this file i use the functions to merge datasets, and answer the questions using barplot and boxplot. 
* **Mean price during the year.ipynb**
The objective of this Jupyter Notebook is answer the question about the mean of price during the year, with the goal to know what time is the best to travel to Seattle. In this file i use functions to format the date and a TimeSeriesPlot to see the insights.
* **Prediction Price Model.ipynb**
The objective of this Jupyter Notebook is know the variables that have correlation with the price. In this file i use two datasets, litings.csv, scraped.csv and a heatmap to see the correlation. In this file you can see functions to fill NA's and dummy variables with the goal to get a better prediction.

## How to Interact with the project
The project is splitted in the questions that we want to answer, the best way to interact with is starting with the file **Business Understanding and Data Understanding.ipynb** then you can proceed to check depends of what question do you want to see how to resolve. You can use the next dictionary with the questions and files. 
1. What is the most expensive city in Seattle for rent an Airbnb? This question is answered in the file **Mean of price per location and Distribution.ipynb**.
2. What is the better date to travel to Seattle and find a good price for an Airbnb? This question is answered in the file **Mean price during the year.ipynb**.
3.  What city of Seattle has more options to look for a Airbnb that accomplish my requirements? This question is answered in the file **Mean of price per location and Distribution.ipynb**.
4. What variables are important for predicting the price of an Airbnb in Seattle? This question is answered in the file **Prediction Price Model.ipynb**.

## Results
The main findings of the code can be found at the post available [here](https://medium.com/@giovanib07/4-facts-that-will-make-you-thing-when-you-have-to-rent-a-airbnb-in-seattle-a8f42857389e).

## Licensing, Authors, Acknowledgements
Must give credit to Airbnb for the data. You can find the Licensing for the data and other descriptive information at the airbnb link available [here](http://insideairbnb.com/get-the-data.html). Otherwise, feel free to use the code here as you would like!

