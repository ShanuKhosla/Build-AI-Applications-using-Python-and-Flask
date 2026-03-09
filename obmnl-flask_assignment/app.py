# Import libraries
from flask import Flask, requests, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


# Read operation
@app.route('/', methods=['GET'])
def get_transaction():
    return render_template('transactions.html', transactions=transactions)

# Create operation


@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if requests.method == 'GET':
        return render_template("form.html")
    if requests.method == "POST":
        new_transaction = {
            'id': len(transactions) + 1,
            'date': requests.form['date'],
            'amount': int(requests.form['amount'])
        }
        transactions.append(new_transaction)
        return redirect(url_for(""))


# Update operation

# Delete operation

# Run the Flask app
