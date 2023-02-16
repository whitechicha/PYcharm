from flask import Flask, render_template, request

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


app = Flask(__name__)
@app.route('/')
def hello()->str:
    return'Hello from Flask'
@app.route('/search4', methods =['POST'])
def do_search()-> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you results: '
    results = str(serach4letters(pharse, letters))
    return render_template('results.html',
                       the_phrase = phrase,
                       the_letters = letters,
                       the_title = title,
                       the_results = results,)
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome")
app.run()
