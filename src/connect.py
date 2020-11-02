import psycopg2
try:
    # connection = psycopg2.connect(user = "postgres",
    #                               password = "ieatpies12",
    #                               host = "127.0.0.1",
    #                               port = "5432",
    #                               database = "Tweetversity")

    connection = psycopg2.connect(user="ggqqmgjisgeidz",
                                  password="0c1237da000717ebf0fae08a266eb311f44ea8d5e9de8c20360a146178affc4f",
                                  host="ec2-54-156-85-145.compute-1.amazonaws.com",
                                  port="5432",
                                  database="da71hnbr874rn5")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")