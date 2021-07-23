from cx_Oracle import connect, DatabaseError, version
def db_connectivity():
    try:
        # database_connection = connect(CUST_CONN_DETAILS)
        database_connection = connect('akshay/akshay@157.245.103.106:1521/ORCLCDB.localdomain')
        # docker_ora	akshay@//157.245.103.106:1521/ORCLCDB.localdomain
        database_cursor = database_connection.cursor()
        print('Hello')
    except DatabaseError as e:
        # logging.error(f"Error {e.args[0]}: {e.args[0]}")
        database_connection.rollback()
        # sys.exit(1)
    else:
        # logging.info(
            # f'Connection has been Established. Running in DB Version{version[0]}')
        return database_connection, database_cursor

db_connectivity()