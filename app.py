from flask import Flask  
from dotenv import load_dotenv  
import os

load_dotenv()

app = Flask(__name__)  
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your secure Flask web app!"

if __name__ == '__main__':
    app.run(debug=True)
