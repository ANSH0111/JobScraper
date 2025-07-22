from flask import Flask, render_template, request
from scraper import scrape_jobs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    jobs = []
    if request.method == 'POST':
        role = request.form.get('role')
        location = request.form.get('location')
        jobs = scrape_jobs(role, location)  # Function called to fetch available jobs.
    return render_template('index.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)