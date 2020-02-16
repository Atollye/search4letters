#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
from letters_search import search4letters

app = Flask(__name__)

@app.route('/results', methods=['POST','GET'])
def do_search():
    if request.method=='POST':
        phrase=request.form['phrase']
        letters=request.form['letters']
        result = str(search4letters(phrase,letters))
        title = 'Here are your results'
        return render_template('results.html',  the_title=title,
                                                the_letters=letters,
                                                the_phrase=phrase,
                                                the_result=result)
    else:
        return redirect('/entry')

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on web')


app.run()

"""
 > Почему мы пишем methods=['POST'] в /search, а не в /entry?
 > Почему не ловятся tcpdump'ом ответы и запросы по порту 5000?
 The method is not allowed for the requested URL
 The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.0
"""
