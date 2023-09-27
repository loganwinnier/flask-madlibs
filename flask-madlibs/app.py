from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def display_home_page():
    """Displays homepage of template options"""
    stories = {"Silly Story": silly_story, "Excited Story": excited_story}

    return render_template(
        "home.html",
        stories=stories
    )


@app.get("/questions")
def display_questions():
    """Displays question form on page."""

    return render_template(
        "questions.html",
        words=silly_story.prompts
    )


@app.get("/results")
def show_result():
    """Show the story result."""

    result = silly_story.get_result_text(request.args)

    return render_template('results.html', story=result)
