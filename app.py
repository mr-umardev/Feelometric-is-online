from flask import Flask, request, render_template 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
import sqlite3  # For database operations

nltk.download('stopwords')

stop_words = stopwords.words('english')

app = Flask(__name__)

# Initialize SQLite database
DATABASE = 'text_analysis.db'

def init_db():
    """Initialize the SQLite database and create the table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TextEntries (
            original_text TEXT NOT NULL,
            processed_text TEXT NOT NULL,
            sentiment_score REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Decorator to preprocess text before analysis
def preprocess_text(func):
    def wrapper(*args, **kwargs):
        if 'text1' in request.form:
            text1 = request.form['text1']
            if text1:
                # Remove digits
                text_final = ''.join(c for c in text1 if not c.isdigit())
                # Remove stopwords
                processed_doc1 = ' '.join([word for word in text_final.split() if word not in stop_words])
                return func(processed_doc1, text1, *args, **kwargs)
            else:
                # Return without processing if the input is empty
                return func(None, None, *args, **kwargs)
        return func(None, None, *args, **kwargs)  # In case 'text1' is not in the form
    return wrapper

@app.route('/', methods=['GET', 'POST'])
@preprocess_text
def my_form(processed_doc1=None, original_text=None):
    if request.method == 'POST' and processed_doc1 is not None:
        # Sentiment analysis using VADER
        sa = SentimentIntensityAnalyzer()
        dd = sa.polarity_scores(text=processed_doc1)
        compound = round((1 + dd['compound']) / 2, 2)

        # Store the text and sentiment score in the database
        store_in_db(original_text, processed_doc1, compound)

        # Output to form.html
        return render_template(
            'form.html', 
            final=compound, 
            text1=original_text,  # Pass original text for display
            text2=dd['pos'], 
            text5=dd['neg'], 
            text4=compound, 
            text3=dd['neu']
        )
    return render_template('form.html')

def store_in_db(original_text, processed_text, sentiment_score):
    """Store the user-entered text, processed text, and sentiment score in the SQLite database."""
    if original_text:  # Only store if there's text
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO TextEntries (original_text, processed_text, sentiment_score)
            VALUES (?, ?, ?)
        ''', (original_text, processed_text, sentiment_score))
        conn.commit()
        conn.close()

@app.route('/visualize')
def visualize():
    """Display the stored entries from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT original_text, processed_text, sentiment_score FROM TextEntries')
    rows = cursor.fetchall()
    conn.close()
    sentiment_scores = [row[2] for row in rows]  # Extract sentiment scores
    original_texts = [row[0] for row in rows]  # Extract original texts

    return render_template(
        'visualize.html', 
        sentiment_scores=sentiment_scores, 
        original_texts=original_texts
    )

@app.route('/data', methods=['GET', 'POST'])
def data():
    """Handle dynamic SQL queries input by the user."""
    query_result = None
    if request.method == 'POST':
        query = request.form['query']
        query_result = execute_query(query)
    return render_template('data.html', query_result=query_result)

def execute_query(query):
    """Execute the user-provided SQL query and return the results."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        return f"Error executing query: {e}"

@app.route('/about')
def about():
    return render_template('about.html')  # Create an about.html file

if __name__ == "__main__":
    init_db()  # Ensure the database is initialized before running the app
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
