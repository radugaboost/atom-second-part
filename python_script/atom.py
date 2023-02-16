from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import psycopg2, logging, os
from dotenv import load_dotenv
from functions import creating_tables, filling_db

transport = AIOHTTPTransport(url="https://spacex-production.up.railway.app/")
client = Client(transport=transport, fetch_schema_from_transport=True)

launches = gql(
    """
    query {
        launches {
            mission_id
            mission_name
            rocket {
                rocket_name
                rocket_type
            }
        }
}
"""
)

result_launches = client.execute(launches)

change_schema = "ALTER TABLE launch OWNER TO postgres;\
    ALTER TABLE rocket OWNER TO postgres;\
    ALTER TABLE mission OWNER TO postgres;\
    GRANT UPDATE ON mission TO postgres;\
    GRANT UPDATE ON rocket TO postgres;\
    GRANT UPDATE ON launch TO postgres;"

load_dotenv()
DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

if __name__ == '__main__':

    with psycopg2.connect(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT) as con:

        cur = con.cursor()
        cur.execute("drop table if exists mission, rocket, launch cascade;")

        print(creating_tables(cur))
        print(filling_db(result_launches, cur))
        cur.execute(change_schema)
