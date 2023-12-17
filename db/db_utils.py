import mysql.connector
from mysql.connector import errorcode
import logging
from db.config import data

host, user, password = data["host"], data["user"], data["passwd"]
DB_NAME = 'game_users_db'


def connect_to_mysql_database(db_name):

    """
    Connects to a MySQL database using credentials from a JSON file.

    Args:
        db_name (str): The name of the MySQL database.

    Returns:
        mysql.connector.MySQLConnection: A MySQL database connection object.

    Raises:
        mysql.connector.Error: If there is an error during the database
        connection process.
    """

    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return db_connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        raise e
    except ValueError as e:
        print(f"ValueError: {e}")
        raise e
    except Exception as e:
        logging.exception(f"Unexpected error occurred: {e}")
        raise e


def get_cursor_and_connection(db_name):

    """
    Connects to a MySQL database and returns a cursor and database connection.

    Args:
        db_name (str): The name of the MySQL database.

    Returns:
        Tuple[mysql.connector.cursor.MySQLCursor,
        mysql.connector.MySQLConnection]:
            A tuple containing a MySQL cursor and database connection.
    """

    db_connection = connect_to_mysql_database(db_name)
    cursor = db_connection.cursor()
    return cursor, db_connection


def create_database(db_name):

    """
    Creates a MySQL database with the specified name.

    Args:
        db_name (str): The name of the MySQL database to be created.
    """

    try:
        cursor, _ = get_cursor_and_connection(db_name)
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))

    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def connect_to_database_or_create_if_not_exists(db_name):

    """
    Connects to a MySQL database or creates it if it does not exist.

    Args:
        db_name (str): The name of the MySQL database.

    Raises:
        mysql.connector.Error: If there is an error during the database
        connection or creation process.
    """
    db_connection = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Database {} does not exist.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(db_name)
            print("Database {} created successfully.".format(db_name))
            db_connection.database = db_name
        else:
            print(err)
    print(f"You are using {db_name} database.")
