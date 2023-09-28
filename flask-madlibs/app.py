from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)
# TODO: move to stories
stories = {"Silly Story": silly_story, "Excited Story": excited_story}
current_story = ""


@app.get("/")
def display_home_page():
    """Displays homepage of template options"""
    global stories

    return render_template(
        "home.html",
        stories=stories
    )


@app.get("/questions")
def display_questions():
    """Displays question form on page."""

    global stories
    global current_story

    selected_story = request.args.get("story-dropdown")
    current_story = stories[selected_story]

    return render_template(
        "questions.html",
        words=current_story.prompts,
        # id = storyid
    )

# TODO: inject story id into url


@app.get("/results")
def show_result():
    """Show the story result."""

    result = current_story.get_result_text(request.args)

    return render_template('results.html', story=result)
