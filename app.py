from flask import *
from flask_debugtoolbar import *
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MADLIBS'
debug = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/story')
def story():
    return render_template('story.html', place=request.args['place-input'], noun=request.args['noun-input'])