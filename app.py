from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About Us Page
@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

# Route for the Membership Page
@app.route('/membership')
def membership():
    return render_template('membership.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
