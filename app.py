from flask import *
from flask_debugtoolbar import *
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MADLIBS'
debug = DebugToolbarExtension(app)

@app.route('/story/')
def story():
    return render_template('story.html')