a. This project is about 'House price Prediction using Machine Learning'.
b. We have used Benguluru house price database.
c. The database is stored in 'benguluru_house_prices.csv'.
d. Methodology
    1. Data Preprocessing:
       In this step we have filtered incorrect/malicious data from our database.
    2. Feature Engineering:
       In this step we have created additional data (as per our need) 
       using available data.
    3. Removing Outliers:
       Using the data generated from feature engineering, we removed 
       incorrect data from our database.
    4. One-Hot-Encoding:
       In our database, the location names were of categorical type, so for 
       we have used one-hot-encoding to encode those names into 0's and 1's.
    5. Building ML Model:
       After one-hot-encoding we splitted our database into training and testing
       data sets. We then used gridsearch CV to find optimal/most accurate 
       ML technique.(which turned out to be Linear Regression)
    6. Making Graphical User Interface:
       We have made a simple GUI for ease of use.

e. Following are details of each files present in this folder
    1. bhp-code.ipynb:
       This file contains all the python code that we have used in this project
       which includes everything from importing database, preprocessing it,     
       building and comparing different machine learning models, to making 
       GUI for ease of use. (For more information read project report)
 
    2. banglore_home_prices_model.pickle:
       As using 'bhp-code.ipynb' file again and again becomes very tedious and
       takes a lot of time (because we would have to re-run entire code), 
       we stored our trained model in 'banglore_home_prices_model.pickle' file 
       using pickle library. This file can then be imported in any python file
       without wasting too much time.

    3. bhp-PreProcessed.csv:
       After performing data pre-processing on our 'benguluru_house_prices.csv' 
       file we stored the resulting dataframe into 'bhp-PreProcessed.csv' file. 
       We can use this file to directly for skipping all the data pre-processing steps.
    
    4. columns.json:
       After performing one-hot-encoding on locations in our database, 
       we stored the column heads in this file, so that it can then be 
       easily loaded in bhp-GUI.ipynb file.
    
    5. bhp-GUI.ipynb:
       In this file we used previosuly created model file i.e. 
       'banglore_home_prices_model.pickle' and column head file 
       i.e. 'columns.json' to make a user friendly GUI. 
       Later we added this GUI to our main 'bhp-code.ipynb' file.

    *The two png images are used to describe the outliers in data at that particular location (more information in report).


