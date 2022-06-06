from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return """Welcome to UP Variates!</h1>"""

@app.route('/org_structure')
def org_structure():
    return """Welcome to UP Variates!</h1>"""
    return render_template('org_structure.html')


if __name__ == "__main__":
    app.run(debug=True)