Mental Health Chatbot

A machine learning-based chatbot that assesses mental health by analyzing user input using Python, Scikit-learn, and Natural Language Processing techniques.

Features

Analyzes user input to identify potential mental health concerns such as anxiety, stress, and more.
Provides appropriate suggestions based on the user's input using a trained model.
Includes Text-to-Speech functionality to give voice feedback.
Setup and Installation

1. Clone the repository
bash
Copy code
git clone https://github.com/VisarRraci42/AI-Chatbot_Project.git
cd AI-Chatbot_Project
2. Create a virtual environment
For macOS/Linux:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
For Windows:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the chatbot
bash
Copy code
python src/chatbot_interface.py
Example

text
Copy code
Input: "I'm feeling really anxious about tomorrow."
Output: "It seems like you're experiencing anxiety. Take a deep breath and try to focus on the present moment."
File Structure

/data: Contains the dataset used for training the model.
/models: Pre-trained models used for predictions.
/src: Contains the Python scripts for training the chatbot, running the interface, and more.
Technologies Used

Python: Main programming language.
Scikit-learn: For machine learning.
Natural Language Processing (NLP): To process and analyze user inputs.
Pygame: For interactive interface elements.
gTTS (Google Text-to-Speech): For converting text responses into speech.
