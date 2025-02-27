import os
import time

import create_tables as ct
import insert_data as insert_data
import queries as queries

def main():
    db_path_tiny = '../data/tiny.db'
    db_path_small = '../data/small.db'
    db_path_medium = '../data/medium.db'
    db_path_full = '../data/full.db'

    # csv_directory_tiny = os.path.join(os.path.dirname(__file__), '..', 'data', 'imdb-tiny')
    # csv_directory_small = os.path.join(os.path.dirname(__file__), '..', 'data', 'imdb-small')
    # csv_directory_medium = os.path.join(os.path.dirname(__file__), '..', 'data', 'imdb-medium')
    # csv_directory_full = os.path.join(os.path.dirname(__file__), '..', 'data', 'imdb-full')




    # Création des tables
    #ct.create_tables(db_path_tiny)
    #ct.create_tables(db_path_small)
    #ct.create_tables(db_path_medium)
    #ct.create_tables(db_path_full)

    # Insertion des données
    #insert_data.insert_all_csv_data(db_path_tiny, csv_directory_tiny)
    #insert_data.insert_all_csv_data(db_path_small, csv_directory_small)
    #insert_data.insert_all_csv_data(db_path_medium, csv_directory_medium)
    #insert_data.insert_all_csv_data(db_path_full, csv_directory_full)

    # Exécution des requêtes
    start_time = time.time()
    
    #results = queries.firstQuery(db_path_tiny)
    #results = queries.firstQuery(db_path_small)
    #results = queries.firstQuery(db_path_medium)
    results = queries.firstQuery(db_path_full)

    for row in results:
        print(row)

    # results = queries.secondQuery(db_path)
    # for row in results:
    #     print(row)

    # results = queries.thirdQuery(db_path)
    # for row in results:
    #     print(row)

    # results = queries.forthQuery(db_path)
    # for row in results:
    #     print(row)

    # results = queries.fifthQuery(db_path)
    # for row in results:
    #     print(row)

    end_time = time.time()

    print("temps =", end_time - start_time)

if __name__ == "__main__":
    main()
