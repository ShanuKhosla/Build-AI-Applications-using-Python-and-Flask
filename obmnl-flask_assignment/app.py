# Import libraries
from flask import Flask, request, url_for, redirect, render_template

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
    if request.method == 'GET':
        return render_template("form.html")
    if request.method == "POST":
        new_transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': int(request.form['amount'])
        }
        transactions.append(new_transaction)
        return redirect(url_for("get_transaction"))


# Update operation
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_transaction(id):
    transaction_id = next((t for t in transactions if t['id'] == id), None)
    if transaction_id == None:
        return "Transaction not found", 404
    if request.method == "GET":
        return render_template("edit.html", transaction=transaction_id)
    if request.method == "POST":
        transaction_id["date"] = request.form["date"]
        transaction_id["amount"] = int(request.form["amount"])
        return redirect(url_for("get_transaction"))
# Delete operation


@app.route("/delete/<int:id>", methods=["POST"])
def delete_transactions(id):
    transaction_id = next((t for t in transactions if t["id"] == id), None)
    if transaction_id == None:
        return "Transaction not found", 404

    transactions.remove(transaction_id)

    return redirect(url_for("get_transaction"))


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
