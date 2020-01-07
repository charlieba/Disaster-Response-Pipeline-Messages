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
My motivation for this project was take the data provided by [Figure Eight](https://www.figure-eight.com/), about messages disasters and create a python pipeline to build a model to predict the category of the message disaster. 

The project include the next topics about data engineering: 
1. Extract, transform and load (ETL), merge, clean and save two datasets, messages.csv and categories.csv. 
2. Create a python pipeline to build a model to predict the category disaster of a message. 
3. Create a web app using the python library flask, creating three differents graphs using a table from a sqlite database. 

## File Descriptions
* **ETL Pipeline Preparation.ipynb**
The objective of this Jupyter Notebook is create the flow to extract, transform and load the data, this Jupyter Notebook is the base to the file process_data.py
* **ML Pipeline Preparation.ipynb**
The objective of this Python file is create a python pipeline to build a predict model, that can predict the categories of a disaster message, this Jupyter Notebook is the base to the file Process_Data.py
* **Process_data.py**
The objective of file is create the functions for the ETL, the functions that the file has are:
    * load_data
    * clean_data
    * save_data
* **Train_classifier.py**
The objective of this file is create a python pipeline to build a predict model that is able to predict the category of a disaster message, the functions that the file has are:
    * load_data
    * tokenize
    * build_model
    * evaluate_model
    * save_model

## How to Interact with the project
The project is splitted in three parts that you have to run in the next order:
1. ETL (Process_data.py): This is the first part of the project, consists in extracts the data from two datasets and merge both, then the dataset is cleaned splitting the categories and is saved in a sqlite database. 
2. Machine Learning Pipeline (Train_classifier.py): This is the second part of the project, after the ETL, the dataset has to be extracted from the sqlite database, the the pipeline is created and the model is built, after that we evaluate the model and is used to predict. 
3. Web App: Using Flask library we create a web app to show three graphs about the data: Distribution of Message Genres, Top Categories Disasters Messages, Correlation between variables. 

## Results
The main findings of the code and the model predictions can be found running the flask web app. 

## Licensing, Authors, Acknowledgements
Must give credit to [Figure Eight](https://www.figure-eight.com/), for the data. You can find the Licensing for the data and other descriptive information link available [Figure Eight](https://www.figure-eight.com/),. Otherwise, feel free to use the code here as you would like!

