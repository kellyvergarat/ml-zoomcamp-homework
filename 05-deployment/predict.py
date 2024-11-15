import pickle  # Import the pickle module to load the pre-trained model

from flask import Flask  # Import Flask class from flask module to create a web application
from flask import request  # Import request object to handle incoming HTTP requests
from flask import jsonify  # Import jsonify function to convert Python dictionaries to JSON

# Define the path to the pre-trained model file
model_file = 'model_C=1.0.bin'

# Load the pre-trained model and the DictVectorizer from the file
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Create a Flask web application instance
app = Flask('churn')

# Define a route for the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the incoming request
    customer = request.get_json()

    # Transform the customer data using the DictVectorizer
    X = dv.transform([customer])
    # Predict the probability of churn using the pre-trained model
    y_pred = model.predict_proba(X)[0, 1]
    # Determine if the customer is likely to churn (probability >= 0.5)
    churn = y_pred >= 0.5

    # Create a result dictionary with the churn probability and churn status
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)  #parsing from numpy boolean to python boolean
    }

    # Return the result as a JSON response
    return jsonify(result)

# Run the Flask web application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)