import sqlite3

def create_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('PRAGMA foreign_keys = ON;')

    tables = [
        'movies',
        'persons',
        'characters',
        'directors',
        'genres',
        'knownformovies',
        'principals',
        'professions',
        'ratings',
        'titles',
        'writers',
        'episodes'
    ]

    for table in tables:
        cursor.execute(f'DROP TABLE IF EXISTS {table};')
        print(f"tables {table} supprimer;")

    # Création de la table 'movies'
    cursor.execute('''
        CREATE TABLE movies (
            mid TEXT PRIMARY KEY,
            titleType TEXT,
            primaryTitle TEXT,
            originalTitle TEXT,
            isAdult INTEGER,
            startYear INTEGER,
            endYear INTEGER,
            runtimeMinutes INTEGER
        )
    ''')

    # Création de la table 'persons' 
    cursor.execute('''
        CREATE TABLE persons (
            pid TEXT PRIMARY KEY,
            primaryName TEXT,
            birthYear INTEGER,
            deathYear INTEGER
        )
    ''')

    # Création de la table 'characters'
    cursor.execute('''
        CREATE TABLE characters (
            mid TEXT,
            pid TEXT,
            name TEXT,
            FOREIGN KEY (mid) REFERENCES movies(mid),
            FOREIGN KEY (pid) REFERENCES persons(pid)
        )
    ''')

    # Création de la table 'directors'
    cursor.execute('''
        CREATE TABLE directors (
            mid TEXT,
            pid TEXT,
            PRIMARY KEY (mid, pid),
            FOREIGN KEY (mid) REFERENCES movies(mid),
            FOREIGN KEY (pid) REFERENCES persons(pid)
        )
    ''')

    # Création de la table 'genres'
    cursor.execute('''
        CREATE TABLE genres (
            mid TEXT,
            genre TEXT,
            FOREIGN KEY (mid) REFERENCES movies(mid)
        )
    ''')

    # Création de la table 'knownformovies'
    cursor.execute('''
        CREATE TABLE knownformovies (
            pid TEXT,
            mid TEXT,
            FOREIGN KEY (pid) REFERENCES persons(pid),
            FOREIGN KEY (mid) REFERENCES movies(mid)
        )
    ''')

    # Création de la table 'principals'
    cursor.execute('''
        CREATE TABLE principals (
            mid TEXT,
            ordering INTEGER,
            pid TEXT,
            category TEXT,
            job TEXT,
            PRIMARY KEY (mid, ordering),
            FOREIGN KEY (mid) REFERENCES movies(mid),
            FOREIGN KEY (pid) REFERENCES persons(pid)
        )
    ''')

    # Création de la table 'professions'
    cursor.execute('''
        CREATE TABLE professions (
            pid TEXT,
            jobName TEXT,
            PRIMARY KEY (pid, jobName),
            FOREIGN KEY (pid) REFERENCES persons(pid)
        )
    ''')

    # Création de la table 'ratings'
    cursor.execute('''
        CREATE TABLE ratings (
            mid TEXT PRIMARY KEY,
            averageRating REAL,
            numVotes INTEGER,
            FOREIGN KEY (mid) REFERENCES movies(mid)
        )
    ''')

    # Création de la table 'titles'
    cursor.execute('''
        CREATE TABLE titles (
            mid TEXT,
            ordering INTEGER,
            title TEXT,
            region TEXT,
            language TEXT,
            types TEXT,
            attributes TEXT,
            isOriginalTitle INTEGER,
            FOREIGN KEY (mid) REFERENCES movies(mid)
        )
    ''')

    # Création de la table 'writers'
    cursor.execute('''
        CREATE TABLE writers (
            mid TEXT,
            pid TEXT,
            PRIMARY KEY (mid, pid),
            FOREIGN KEY (mid) REFERENCES movies(mid),
            FOREIGN KEY (pid) REFERENCES persons(pid)
        )
    ''')

    # Création de la table 'episodes'
    cursor.execute('''
        CREATE TABLE episodes (
            mid TEXT PRIMARY KEY,
            parentMid TEXT,
            seasonNumber INTEGER,
            episodeNumber INTEGER,
            FOREIGN KEY (mid) REFERENCES movies(mid),
            FOREIGN KEY (parentMid) REFERENCES movies(mid)
        )
    ''')

    conn.commit()
    conn.close()

create_tables('data.db')