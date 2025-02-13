from dotenv import load_dotenv
from google import genai
from flask import Flask, request, render_template
import os

# Load API key
load_dotenv()
api_key = os.getenv('GOOGLE_API')

# Initialze the client
client = genai.Client(api_key=api_key)

# Function to generate README
def generate_readme(title, tech, libs, desc, lic):
    prompt = f'''
        Here are few details with which I want you to create a simple README file with the following template:
        1. Title
        2. About the project
        3. Technologies Used
        4. Getting started:
            - Prerequisites (Instructions to install required packages here)
            - Installation (Instructions to clone the GitHub repo)
            - Usage (Show examples of how it can be used)
        5. License (Just mention the license without any details)
        6. Contributing
        7. Contact
        8. Acknowledgement

        Now, based on the given template, I want you to provide the markdown file **only**, without any other response.
        I want just the markdown with the following details:

        title={title}
        technologies used={tech}
        libraries used={libs}
        description={desc}
        license={lic}
    '''

    response = client.models.generate_content(model='gemini-2.0-flash', contents=[prompt])    
    return response.text if response else "Error: No response received"


# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Readme page
@app.route("/readme", methods=['GET', 'POST'])
def readme():
    if request.method == 'POST':
        title = request.form['title']
        tech = request.form['tech']
        libs = request.form['libs']
        desc = request.form['desc']
        lic = request.form['lic']

        print(f"Form Data - Title: {title}, Tech: {tech}, Libraries: {libs}, Description: {desc}, License: {lic}")

        response = generate_readme(title, tech, libs, desc, lic)

        print(f"Generated README Response: {response}")

        return render_template('readme.html', response=response)

    return render_template('readme.html', response=None)
       


# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)