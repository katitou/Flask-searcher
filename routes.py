from main import app
from src.search import search
from src.requests import log_request
from flask import render_template, request
from markupsafe import escape


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                           the_title='Search for Letters online') 


@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search(phrase, letters))
    log_request(request, results)
    return render_template('results.html', 
                           the_title='Results searching for letters', 
                           the_results=results, 
                           the_phrase=request.form['phrase'], 
                           the_letters=request.form['letters']
    )


@app.route('/viewlog')
def view_log() -> 'html':
    titles = ['Remote addr', 'User agent', 'Form Data', 'Results']
    log_list = []
    with open('search.log', 'r') as log:
        for line in log:
            log_list.append([])
            for item in line.split('|'):
                log_list[-1].append(escape(item))
    return render_template('request.html', 
                           the_title = 'View Log', 
                           row_titles = titles, 
                           data = log_list
    )