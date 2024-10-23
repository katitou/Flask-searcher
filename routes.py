from main import app
from src.search import search
from flask import render_template, request


@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    return render_template('results.html', 
                           the_title='Results searching for letters', 
                           the_results=str(search(phrase, letters)), 
                           the_phrase=request.form['phrase'], 
                           the_letters=request.form['letters']
    )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                           the_title='Search for Letters online') 