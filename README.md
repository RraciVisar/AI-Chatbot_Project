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

### Model Performance

The chatbot model was optimized using **GridSearchCV**, and the following best parameters were found:

- `svc__C`: 1
- `svc__kernel`: 'linear'
- `tfidf__max_df`: 0.75
- `tfidf__min_df`: 1
- `tfidf__ngram_range`: (1, 2)

The best cross-validation score achieved was **0.773**.

#### Model Evaluation on Test Set:
The model's performance was evaluated using precision, recall, and F1-score metrics. Below are the results:

| Category              | Precision | Recall | F1-Score | Support |
|-----------------------|-----------|--------|----------|---------|
| Anxiety               | 0.82      | 0.82   | 0.82     | 754     |
| Bipolar               | 0.86      | 0.73   | 0.79     | 554     |
| Depression            | 0.68      | 0.77   | 0.72     | 3058    |
| Normal                | 0.92      | 0.92   | 0.92     | 3325    |
| Personality Disorder  | 0.90      | 0.56   | 0.69     | 220     |
| Stress                | 0.77      | 0.54   | 0.64     | 530     |
| Suicidal              | 0.69      | 0.66   | 0.68     | 2095    |

**Overall Accuracy**: 0.78

- **Macro Average**:
  - Precision: 0.80
  - Recall: 0.72
  - F1-Score: 0.75

- **Weighted Average**:
  - Precision: 0.78
  - Recall: 0.78
  - F1-Score: 0.78
