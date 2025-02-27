import sqlite3

def firstQuery(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    res = cursor.execute('''
        SELECT persons.pid, persons.primaryName, movies.primaryTitle
        FROM persons 
        JOIN characters ON persons.pid = characters.pid 
        JOIN movies ON characters.mid = movies.mid
        WHERE persons.primaryName = 'Jean Reno'
    ''')

    results = res.fetchall() 
    conn.close()
    return results


def secondQuery(db_path):  
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    res = cursor.execute('''
                      SELECT m.primaryTitle, r.averageRating
                      FROM movies m
                      JOIN ratings r ON m.mid = r.mid 
                      JOIN genres g ON m.mid = g.mid
                      WHERE g.genre = 'Horror' 
                      AND m.startYear BETWEEN 2000 and 2009
                      ORDER BY r.averageRating DESC
                      LIMIT 3;
    ''')
    results = res.fetchall()
    conn.close
    return results



def thirdQuery(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    res = cursor.execute('''
                      SELECT p.*
                        FROM persons p
                        WHERE p.pid IN (
                            SELECT w.pid
                            FROM writers w
                            WHERE w.mid NOT IN (
                                SELECT t.mid
                                FROM titles t
                                WHERE t.region = 'ES'
                            )
                        );
                      ''')
    
    results = res.fetchall() 
    conn.close()
    return results

def forthQuery(db_path): 
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    res = cursor.execute('''
                    WITH max_roles_per_person_movie AS (
                      SELECT MAX(role_count) as max_roles
                        FROM (
                            SELECT COUNT(*) AS role_count 
                            FROM persons p 
                            JOIN characters c ON p.pid = c.pid 
                            JOIN movies m ON c.mid = m.mid 
                            GROUP BY c.pid, c.mid
                        )
                    )
                    SELECT p.primaryName, m.primaryTitle, COUNT(*) AS role_count 
                    FROM persons p, max_roles_per_person_movie
                    JOIN characters c ON p.pid = c.pid 
                    JOIN movies m ON c.mid = m.mid 
                    GROUP BY c.pid, c.mid 
                    HAVING role_count = max_roles
                    ORDER BY role_count DESC;
                    ''')
    
    results = res.fetchall() 
    conn.close()
    return results

def fifthQuery(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    res = cursor.execute('''
                      SELECT DISTINCT persons.primaryName FROM persons
                      INNER JOIN knownformovies ON persons.pid = knownformovies.pid
                      INNER JOIN movies ON knownformovies.mid = movies.mid
                      INNER JOIN ratings ON movies.mid = ratings.mid
                      WHERE movies.startYear < (SELECT startYear FROM movies WHERE primaryTitle = 'Avatar') 
                      AND ratings.numVotes < 200000
                      AND movies.mid NOT IN (
                        SELECT movies.mid
                        FROM movies
                        INNER JOIN ratings ON movies.mid = ratings.mid
                        WHERE movies.startYear >= (SELECT startYear FROM movies WHERE primaryTitle = 'Avatar') 
                      AND ratings.numVotes > 200000)
                     '''
    )
    
    results = res.fetchall() 
    conn.close()
    return results
