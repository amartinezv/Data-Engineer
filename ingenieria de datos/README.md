# Newspaper ETL Process

This project uses a web scraper to extract data from the front page of the news websites: Semana, El tiempo and El universal. It is based on the procedure ETL (Extract, Transform, and Load).

The steps of this script are the following:

* It extracts the data from the websites using the scraper in the folder 'extract'. All the data is saved first in JSON Files.

* All the data saved in JSON is processed in folder 'transform' with Pandas, it is cleaned, modified and complemented, then it is exported in a clean CSV.

* Once the data is already clean it is stored in an SQLite Database in the 'load' directory.

To use the script you have to install required libraries from requirements.txt and run the file pipeline.py
