import os
import sqlite3
import csv

def insert_data_from_csv(db_path, table_name, csv_dir):
    csv_filename = os.path.join(csv_dir, f"{table_name}.csv")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    print(f"Table '{table_name}' vidée avec succès.")

    with open(csv_filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        raw_headers = next(reader)  

        cleaned_columns = [col.strip("()'\",") for col in raw_headers]

        columns = ', '.join(f'"{col}"' for col in cleaned_columns)
        placeholders = ', '.join('?' for _ in cleaned_columns)

        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        for row in reader:
            values = [None if v == '' else v for v in row]
            cursor.execute(sql, values)

    conn.commit()
    conn.close()

def insert_all_csv_data(db_path, csv_dir):
    tables = [
        "movies",
        "persons",
        "characters",
        "directors",
        "genres",
        "knownformovies",
        "principals",
        "professions",
        "ratings",
        "titles",
        "writers"
    ]
    
    for table in tables:
        print(f"Insertion des données dans la table '{table}' à partir de {table}.csv")
        insert_data_from_csv(db_path, table, csv_dir)

if __name__ == '__main__':
    csv_directory = os.path.join(os.path.dirname(__file__), '..', 'data', 'imdb-tiny')
    insert_all_csv_data("data.db", csv_directory)
