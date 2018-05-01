# Connect to MySQL data_storage
import MySQLdb
import os
from ConfigParser import SafeConfigParser


def connection():
    # Connect to mysql
    config = SafeConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\config\mysql_config.ini'))
    db_host = config.get('ethos_manager', 'db_host')
    db_user = config.get('ethos_manager', 'db_user')
    db_pass = config.get('ethos_manager', 'db_pass')
    db_schema = config.get('ethos_manager', 'db_schema')

    try:
        db = MySQLdb.connect(db_host, db_user, db_pass, db_schema)
    except:
        print "MySQL login failed"
        return -1
    return db


def return_row(sql_str):
    db = connection()
    #Build cursor
    cursor = db.cursor()
    try:
        cursor.execute(sql_str)
    except:
        print "Error MySQL object failed"
        return -1

    try:
        data = cursor.fetchone()
    except:
        return -1
    return data


def insert(sql_str):
    rc = 0
    db = connection()
    # Build cursor
    cursor = db.cursor()
    try:
        #Execute the SQL
        cursor.execute(sql_str)
        rc = cursor.rowcount
        db.commit()
    except:
        #MySQL return error
        db.rollback()
        print "MySQL insert failed"

    db.close()
    return rc


def insert_get_id(sql_str):
    db = connection()
    # Build cursor
    cursor = db.cursor()
    try:
        # Execute the SQL
        cursor.execute(sql_str)

        db.commit()
        last_row_id = cursor.lastrowid
    except:
        # MySQL return error
        db.rollback()
        print "MySQL insert failed"

    db.close()
    return last_row_id




