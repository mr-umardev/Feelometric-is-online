# Feelometric-is-online  
Feelometric is an advanced machine learning Flask web app designed for sentiment analysis using Scikit-learn and VADER Sentiment. It transforms raw text into actionable insights, making it an ideal tool for decoding emotions and understanding public sentiment.  

The project utilizes libraries like:  
- Flask  
- Scikit-learn  
- Requests  
- NLTK  
- RE  
- vaderSentiment  

### VADER SENTIMENT  
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a powerful lexicon and rule-based sentiment analysis tool. Specifically tailored for sentiments expressed in social media, it performs excellently on texts from various domains.  
Learn more about [VADER](https://pypi.org/project/vaderSentiment/)  

### LET'S TALK ABOUT SENTIMENT ANALYSIS  
Sentiment analysis, a critical branch of Natural Language Processing, automates the detection of emotional states within text. Widely used in analyzing product reviews, movie ratings, or social media posts, it enables companies to gauge customer opinions and adjust strategies accordingly.  

Sentiment analysis goes beyond identifying text polarity (positive/negative) by exploring nuanced emotional states. For businesses, it’s a key tool for decision-making; understanding public sentiment about a product can lead to modifications, marketing shifts, or even halting production to prevent losses.  

Public sentiment can be derived from numerous sources, including interviews, surveys, and now, more prominently, social media platforms like Twitter and Facebook. These vast repositories of data offer invaluable insights into public opinion.  


### SCREENSHOT OF THE APPLICATION  
Below is a screenshot of the **Feelometric** web application:  

### Welcome Page:

![ScreenShot](./ScreenShot)


### Input taken with Calculation in Compound Percentage:

![ScreenShot](./ScreenShot1)


### Tabular Calculation:

![ScreenShot](./ScreenShot2)

### DBMS Dynamic Query Handling:

![ScreenShot](./ScreenShot3)

### Predicted value updated in Database:

![ScreenShot](./ScreenShot4)

### Visualizing with Line Chart:

![ScreenShot](./ScreenShot5)

### The Dev Team:
![ScreenShot](./ScreenShot6)

### Prerequisites

1.Python Installation: Ensure that Python is installed. If not, download and install Python from here.

2.Visual Studio Code Installation: Ensure you have Visual Studio Code installed. If not, download it from here.

3.Required Python Packages: The provided code depends on several libraries. You'll need to install them using pip in the terminal. Here's the list:

Flask
vaderSentiment
nltk
sqlite3 (This is part of the standard Python library, so no installation is needed for this).

### Steps to Set Up the Project in VS Code:

Clone the Repository (or copy the code):

If the code is on a GitHub repository, clone it by running:
bash
Copy code
git clone <your-repository-url>
If you're just starting with the code, create a new directory for your project and place the Python code in that directory.
Open VS Code:

Open Visual Studio Code and navigate to your project folder.
Set Up a Virtual Environment (Optional but recommended):

Open the integrated terminal in VS Code (Ctrl + ~).
Navigate to your project directory if you haven't already.
Create a virtual environment by running:
bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install Required Packages:

Install the required Python packages by running the following commands in the terminal:
bash
Copy code
pip install flask vaderSentiment nltk
Download NLTK Data:

The code uses NLTK's stopwords. Ensure that the NLTK data is downloaded by running the following command in Python:
python
Copy code
import nltk
nltk.download('stopwords')
Run the Flask Application:

In the VS Code terminal, make sure you're in the directory where your Python file is located (where your app.py is).
Run the Flask application with the following command:
bash
Copy code
python app.py
You should see output indicating that the Flask server has started, such as:
csharp
Copy code
* Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
Open the Web Application:

Open your web browser and navigate to http://127.0.0.1:5002/ to access the web application.
Additional Information
Templates: Ensure that you have the required HTML templates (like form.html, visualize.html, data.html, and about.html) in a folder named templates inside the same directory as your Python code.
Database: The code uses SQLite, and it will automatically create a database file named text_analysis.db in the project directory when it runs.
Now, your Flask application should be set up and running!

