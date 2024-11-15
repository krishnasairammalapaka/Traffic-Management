from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traffic_management')
def traffic_management():
    return render_template('traffic_management.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/emergency-contact')
def emergency_contact():
    return render_template('emergency_contact.html')

if __name__ == '__main__':
    app.run(debug=True)
