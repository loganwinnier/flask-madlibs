from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/questions")
def display_questions():
    """displays question form on page"""

    return render_template(
        "questions.html",
        words=silly_story.prompts
    )
