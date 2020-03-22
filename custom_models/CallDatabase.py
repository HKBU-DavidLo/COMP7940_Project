import psycopg2
import os



def getcoordinates(target):

    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    postgres_select_query = f"""SELECT latitude, longitude FROM hospital WHERE hos_name = '{target}'"""

    cursor.execute(postgres_select_query)
    lat, long = cursor.fetchone()

    cursor.close()
    conn.close()

    return lat, long
