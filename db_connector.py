import pymysql
import datetime


schema_name = 'sql8620853'

conn = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8620853', passwd='3YplB3ZVVP', db='sql8620853')
conn.autocommit(True)

# Getting a cursor from Database
# cursor = conn.cursor()

# Inserting data into table
# statementToExecute = "CREATE TABLE `"+schema_name+"`.`usersRotem`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL,`creation_date` DATETIME, PRIMARY KEY (`user_id`));"
# cursor.execute(statementToExecute)

# cursor.close()
# conn.close()


def add_user(username, user_id):


    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Get the current timestamp
    user_creation_time = datetime.datetime.now()

    if not cursor.execute(f"SELECT user_name FROM {schema_name}.usersRotem WHERE user_id = {user_id}"):
        # Inserting data into table
        cursor.execute(f"INSERT into {schema_name}.usersRotem (user_id, user_name, creation_date) VALUES ({user_id}, '{username}', '{user_creation_time}')")
    else:
        cursor.close()
        conn.close()
        return 1
    cursor.close()
    conn.close()


def del_user(user_id):

    # Establishing a connection to DB

    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    if cursor.execute(f"SELECT user_name FROM {schema_name}.usersRotem WHERE user_id = {user_id}"):

        # Deleting data(user) from table by their id
        cursor.execute(f"DELETE FROM {schema_name}.usersRotem WHERE id = {user_id}")
    else:
        # Return error message if user_id doesn't exist
        cursor.close()
        conn.close()
        return 1

    cursor.close()
    conn.close()


def update_user(new_name, user_id):

    # Establishing a connection to DB

    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    if cursor.execute(f"SELECT user_name FROM {schema_name}.usersRotem WHERE user_id = {user_id}"):

        # Updating user's name in the table
        cursor.execute(f"UPDATE {schema_name}.usersRotem SET user_name = '{new_name}' WHERE user_id = {user_id}")
    else:
        # Return error message if user_id doesn't exist
        cursor.close()
        conn.close()
        return 1

    cursor.close()
    conn.close()


def get_user(user_id):

    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Retrieve the user's name by their id
    cursor.execute(f"SELECT user_name FROM usersRotem WHERE user_id = {user_id}")
    try:
        result = cursor.fetchone()
        return str(result[0])
    except:
        # Return error message/sign if user_id doesn't exist
        return 'error_no_such_id'

    # Close the cursor and connection
    cursor.close()
    conn.close()






