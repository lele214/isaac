from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():

    # connect to database
    conn = sqlite3.connect(r'data\tboi_items.db')
    cursor = conn.cursor()
    
    # list by item_id
    cursor.execute("SELECT name, item_id, image_url, quote, quality, recharge, item_pool FROM items ORDER BY item_id")
    items = cursor.fetchall()
    
    conn.close()
    
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)


