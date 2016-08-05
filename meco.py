from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def firstTab():
    return render_template('html/home.html')

# qualifications
@app.route('/qualifications/')
@app.route('/Qualifications/')
@app.route('/QUALIFICATIONS/')
def secondTab():
    return render_template('html/qualifications.html')

# projects
@app.route('/projects/')
@app.route('/Projects/')
@app.route('/PROJECTS/')
def thirdTab():
    return render_template('html/projects.html')

# affiliations
@app.route('/affiliations/')
@app.route('/Affiliations/')
@app.route('/AFFILIATIONS/')
def fourthTab():
    return render_template('html/affiliations.html')

# safety
@app.route('/safety/')
@app.route('/Safety/')
@app.route('/SAFETY/')
def fifthTab():
    return render_template('html/safety.html')

# contact us
@app.route('/contact-us/')
@app.route('/CONTACT-US/')
@app.route('/Contact-us/')
def sixthTab():
    return render_template('html/contact-us.html')




############### 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('html/notFound.html'), 404





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
