import psycopg2
from psycopg2 import Error

try:
    # connection = psycopg2.connect(user="postgres",
    #                               password="ieatpies12",
    #                               host="127.0.0.1",
    #                               port="5432",
    #                               database="Tweetversity")

    connection = psycopg2.connect(user="ggqqmgjisgeidz",
                                  password="0c1237da000717ebf0fae08a266eb311f44ea8d5e9de8c20360a146178affc4f",
                                  host="ec2-54-156-85-145.compute-1.amazonaws.com",
                                  port="5432",
                                  database="da71hnbr874rn5")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE Sentiments
          (ID INT PRIMARY KEY NOT NULL,
          INSTITUTION VARCHAR NOT NULL,
          TWEET VARCHAR,
          SENTIMENT VARCHAR,
          NATIONAL_RANK BIGINT); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print ("Error while creating PostgreSQL table", error)
finally:
# closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")