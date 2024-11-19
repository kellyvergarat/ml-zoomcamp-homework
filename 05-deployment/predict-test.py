#!/usr/bin/env python
"""
This script sends a customer's data to a prediction service and prints the response.
If the customer is predicted to churn, it prints a message indicating that a promotional email should be sent.

Modules:
    requests: To send HTTP requests.

Constants:
    url (str): The URL of the prediction service.
    customer_id (str): The ID of the customer.
    customer (dict): The customer's data.

Steps:
1. Define the URL of the prediction service.
2. Define the customer ID.
3. Define the customer's data in a dictionary.
4. Send a POST request to the prediction service with the customer's data.
5. Parse the JSON response from the prediction service.
6. Print the response.
7. Check if the customer is predicted to churn.
8. Print a message indicating whether to send a promotional email based on the prediction.
"""
# coding: utf-8

import requests

host = 'https://compute.amazonaws.com/'
url = f'http://{host}/predict'

customer_id = 'xyz-123'
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 24,
    "monthlycharges": 29.85,
    "totalcharges": (24 * 29.85)
}


response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)