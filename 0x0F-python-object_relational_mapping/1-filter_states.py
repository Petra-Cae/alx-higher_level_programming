#!/usr/bin/python3
""" lists all states with a name starting with upper case N
 from the hbtn_0e_0_usa database
"""

from sys import argv
import MySQLdb
from unicodedata import name

if __name__ == "__main__":
    """Access database"""
    db = MySQLdb.connect(user=argv[1], pswd=argv[2], db=argv[3])
    dbc = db.cursor()
    dbc.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(row) for row in dbc.fetchall() if row[1][0] == "N"]
