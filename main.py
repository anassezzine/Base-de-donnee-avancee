import database as db
import mysql.sqlite_trigger_handler as sth

if __name__ == "__main__":

   db.createMySQLDatabase("tiny", False)
   #db.export_mysqlDB_to_mongoDB("imdb", "tiny")
   
   #db.mysqlRequest(1)
   
   #db.mongodbRequest(1)

   #db.mongoDBmoviesStructure()

   # version 1
   # # changer le mid
   # sth.sqlite_trigger_handler("INSERT", {
   #       "mid": "t111",
   #       "titleType": "movie",
   #       "primaryTitle": "Title 111",
   #       "originalTitle": "Original Title 111",
   #       "isAdult": 0,
   #       "startYear": "2022-01-01",
   #       "endYear": "2022-01-02",
   #       "runtimeMinutes": 120
   #    }, "movies")


   # version 2
   # db.mysql_trigger_tomongodb()

   # db.mongo_trigger_tomysql()