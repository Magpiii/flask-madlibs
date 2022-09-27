from flask import *
from flask_debugtoolbar import *
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MADLIBS'
debug = DebugToolbarExtension(app)

@app.route('/index.html')
def ask_questions():
    prompts = story.prompts

    return render_template('/index.html', prompts=prompts)

@app.route('/Templates/story')
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template('/Templates/story.html', text=text)