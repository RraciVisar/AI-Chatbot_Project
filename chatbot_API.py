from flask import Flask, request, jsonify
import pickle

# Assuming your trained chatbot model is stored in a pickle file.
with open('chatbot_model_improved.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the request JSON body
    data = request.get_json()
    user_input = data.get('message', '')

    # Predict mental health status using the model
    prediction = model.predict([user_input])
    result = prediction[0]

    # Return the result as JSON
    return jsonify({'status': result})

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#Testing