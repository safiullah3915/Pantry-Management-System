from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Load pantry data
def load_pantry():
    try:
        with open('pantry_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save pantry data
def save_pantry(pantry):
    with open('pantry_data.json', 'w') as file:
        json.dump(pantry, file)

@app.route('/')
def index():
    pantry = load_pantry()
    return render_template('index.html', pantry=pantry)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    quantity = request.form['quantity']
    
    pantry = load_pantry()
    pantry.append({'item_name': item_name, 'quantity': quantity})
    save_pantry(pantry)
    
    return redirect(url_for('index'))

@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item_id):
    quantity = request.form['quantity']
    
    pantry = load_pantry()
    pantry[item_id]['quantity'] = quantity
    save_pantry(pantry)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    pantry = load_pantry()
    pantry.pop(item_id)
    save_pantry(pantry)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
