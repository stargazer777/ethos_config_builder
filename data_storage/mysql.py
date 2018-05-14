# Connect to MySQL data_storage
import MySQLdb
import os
from ConfigParser import SafeConfigParser


def connection():
    # Connect to mysql
    myconf_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'config', 'mysql_config.ini')
    ethos_manger_value = ['ethos_manager']

    config = SafeConfigParser()
    config.read(myconf_path)

    if config.has_section('ethos_manager'):
        try:
            db_host = config.get('ethos_manager', 'db_host')
        except:
            print "db_host could not be found in config."
        try:
            db_user = config.get('ethos_manager', 'db_user')
        except:
            print "db_user could not be found in config"
        try:
            db_pass = config.get('ethos_manager', 'db_pass')
        except:
            print "db_pass could not be found in config"
        try:
            db_schema = config.get('ethos_manager', 'db_schema')
        except:
            print "db_schema could not be found in config"
    else:
        print "Invalid Config File - mysql_config.ini"

    try:
        db = MySQLdb.connect(db_host, db_user, db_pass, db_schema)
    except:
        print "MySQL login failed"

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
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        #MySQL return error
        db.rollback()
        print "MySQL insert failed: e"

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




