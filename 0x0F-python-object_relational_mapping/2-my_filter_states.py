#!/usr/bin/python3
"""
Takes in an argument and displays all values in the `states` table
 of `hbtn_0e_0_usa` where `name` matches the argument
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(username=argv[1], pswd=argv[2], db=argv[3],
                         host="localhost", port=3306)
    dbc = db.cursor()
    dbc.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(argv[4]).strip("'"))
    [print(state) for states in dbc.fetchall()]
