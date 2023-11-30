# web-scraper
Assignment 3
Problem:
Create a web scraper program to find out specific data structure from Web.
In our case, we will try to scrape Disease Names and Details about each disease.

Expected Output:
The output must contain the following data:

    Disease Name
    Overview
    Key Facts
    Symptoms
    Causes
    Types
    Risk factors
    Diagnosis
    Prevention
    Specialist to visit
    Treatment
    Home-care
    Alternatives therapies
    Living with
    FAQs - All Questions and Answers
    References - Array of Links

Try scraping as many datapoints as you can.
You may add any other relevant data to the output you think is appropriate.

Hint:
You may check https://www.1mg.com/all-diseases as a reference.
This URL has a list of Disease names which are sorted alphabetically.
It is a 2 step process:

    Scrape each disease name and their details URL and save the basic data.
    Your program should then go to the details URL to scrape the other datapoints mentioned above.

Preferred technology stack - Python, JavaScript