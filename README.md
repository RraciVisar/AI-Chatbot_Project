# Mental Health Chatbot

A **machine learning-based chatbot** that assesses mental health by analyzing user input using Python, Scikit-learn, and Natural Language Processing techniques.

## Features
- Analyzes user input to identify potential mental health concerns such as anxiety, stress, and more.
- Provides appropriate suggestions based on the user's input using a trained model.
- Includes Text-to-Speech functionality to give voice feedback.

## Setup and Installation

### 1. Clone the repository
```
git clone https://github.com/VisarRraci42/AI-Chatbot_Project.git
cd AI-Chatbot_Project
```
### 2. Create a virtual environment

**For macOS/Linux:**

```
python3 -m venv .venv
source .venv/bin/activate
```
**For Windows:**
```
python -m venv .venv
.venv\Scripts\activate
```
### 3. Install the required dependencies

With your virtual environment activated, install the required packages:

```
pip install -r requirements.txt
```
### 4. Run the chatbot interface

To start the Mental Health Chatbot interface, run the following command:

```
python chatbot_interface.py
```
#### Example:

```
Input: "I'm feeling really scared about tomorrow. I cannot fall asleep."
Output: "Anxiety"
```
### File Structure

- `chatbot_data.csv`: Mental health dataset used to train the model.
- `chatbot_interface.py`: Interface for interacting with the chatbot.
- `chatbot_model_improved.pkl`: Trained model after being trained on the mental health data.
- `train_chatbot_improved.py`: Python script used to train the chatbot model using the provided data.

