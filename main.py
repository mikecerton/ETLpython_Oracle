import couchDB_connector
import oracle_connector

ora_conn = oracle_connector.start_connect()

data = couchDB_connector.load_data()

if ora_conn:
    for d in data:
        sql_insert = """INSERT INTO TPS09_Feedback (FeedCode, CusCode, point, DW09_Feedback, KnowFrom, 
                        timestamp, Favorite_place) VALUES (:1, :2, :3, :4, :5, TO_DATE(:6,'DD/MM/YYYY'), :7)"""
        oracle_connector.insert_data(ora_conn, sql_insert, d)
    