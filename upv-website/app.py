from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/org_structure')
def org_structure():
    return render_template('org_structure.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)