#!/usr/bin/python3
"""
Lists all states from the database `hbtn_0e_0_usa`
"""

import MySQLdb
From sys import argv

if __name__ == '__main__':
    """ Access database """
    db = MySQLdb.connect(username=argv[1], pswd=argv[2],
                         db=argv[3], host=localhost, port=3306)
    dbc = db.cursor()
    dbc.execute('SELECT * FROM states')
    [print(state) for states in dbc.fetchall()]
