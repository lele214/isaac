from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
#app.config['TEMPLATES_AUTO_RELOAD'] = True  #temporaire
@app.route('/')
def index():
    # Récupérer les filtres depuis l'URL
    quality_filter = request.args.get('quality', None)
    recharge_filter = request.args.get('recharge', None)
    pool_filter = request.args.get('pool', None)
    
    # Connexion à la base de données
    conn = sqlite3.connect(r'data\tboi_items.db')
    cursor = conn.cursor()
    
    # Construire la requête SQL avec les filtres
    query = "SELECT name, item_id, image_url, quote, quality, recharge, item_pool FROM items WHERE 1=1"
    params = []
    
    # Filtre par quality
    if quality_filter:
        query += " AND quality = ?"
        params.append(quality_filter)
    
    # Filtre par type (actif/passif)
    if recharge_filter == 'active':
        query += " AND recharge != '' AND recharge IS NOT NULL"
    elif recharge_filter == 'passive':
        query += " AND (recharge = '' OR recharge IS NULL)"
    
    # Filtre par item_pool
    if pool_filter:
        query += " AND item_pool LIKE ?"
        params.append(f'%{pool_filter}%')
    
    # Trier par item_id
    query += " ORDER BY item_id"
    
    # Exécuter la requête
    cursor.execute(query, params)
    items = cursor.fetchall()
    
    conn.close()
    
    return render_template('index.html', items=items, 
                          current_quality=quality_filter,
                          current_recharge=recharge_filter,
                          current_pool=pool_filter)

if __name__ == '__main__':
    app.run(debug=False)