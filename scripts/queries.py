import sqlite3

def firstQuery(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Requête SQL corrigée
    cursor.execute('''
        SELECT persons.pid, persons.primaryName, movies.primaryTitle
        FROM persons 
        JOIN characters ON persons.pid = characters.pid 
        JOIN movies ON characters.mid = movies.mid
        WHERE persons.primaryName = 'Jean Reno'
    ''')

    # Récupérer et afficher les résultats
    results = cursor.fetchall()
    for row in results:
        print(row)  # Affichage des résultats

    conn.close()

# Exécution de la requête
firstQuery('data.db')
