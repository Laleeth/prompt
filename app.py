from flask import Flask, render_template, request
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

import pandas as pd

@app.route('/prompts')
def prompts():
    # Read the Excel file
    df = pd.read_excel('ai.xlsx')

    # Get the unique values from the "ai_tool" column
    unique_values = df['AI_TYPE'].unique()

    # Define the items per page
    items_per_page = 54

    # Python logic to generate numbers
    

    # Convert the DataFrame to a list of dictionaries for easy processing in the template
    data = df.to_dict('records')

   # Get the page number from the query parameters
    page = request.args.get('page', type=int, default=1)

    # Calculate the start and end index for the current page
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    # Get the data for the current page
    data = df.iloc[start_index:end_index].to_dict('records')

    # Calculate the total number of pages
    total_pages = (len(df) // items_per_page) + 1

    return render_template('prompts.html', data=data, unique_values=unique_values, total_pages=total_pages, current_page=page)

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

