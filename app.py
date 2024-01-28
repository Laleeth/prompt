from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    # Read the Excel file
    df = pd.read_excel('your_excel.xlsx')

    # Convert the DataFrame to a list of dictionaries for easy processing in the template
    data = df.to_dict('records')

    # Render the template and pass the data
    return render_template('index.html', data=data)

@app.route('/home')
def home_page():
    # Your home page logic
    return render_template('home.html')

@app.route('/prompts')
def prompts():
    # Read the Excel file
    df = pd.read_excel('your_excel.xlsx')

    # Convert the DataFrame to a list of dictionaries for easy processing in the template
    data = df.to_dict('records')

    # Render the template and pass the data
    return render_template('prompts.html', data=data)


@app.route('/ai_business_ideas')
def ai_business_ideas():
    # Your AI Business Ideas page logic
    return render_template('ai_business_ideas.html')

@app.route('/indexx')
def indexx():
    # Your AI Business Ideas page logic
    return render_template('indexx.html')

# @app.route('/check')
# def check():
#     # Your AI Business Ideas page logic
#     return render_template('check.html')

@app.route('/chatgpt_prompts')
def chatgpt_prompts():
    # Your ChatGPT Prompts page logic
    return render_template('chatgpt_prompts.html')

@app.route('/chatgpt_plugins')
def chatgpt_plugins():
    # Your Chat GPT Plugins page logic
    return render_template('chatgpt_plugins.html')

@app.route('/midjourney_prompts')
def midjourney_prompts():
    # Your Midjourney Prompts page logic
    return render_template('midjourney_prompts.html')

# if __name__ == '__main__':
#     app.run(debug=True)
