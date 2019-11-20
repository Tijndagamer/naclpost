#!/usr/bin/python3
"""
    db.py
    This file is part of naclpost.

    Copyright (c) 2019 Martijn

    naclpost is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    naclpost is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with naclpost.  If not, see <http://www.gnu.org/licenses/>.
"""


import pymysql.cursors


class NaclPostDb:
    con = None
    cur = None

    # SQL queries

    add_user = """INSERT INTO
            users
                (alias, public_key, public_key_encryption)
            VALUES
                (%(alias)s, %(public_key)s, %(public_key_encryption)s)"""

    select_user_by_pubkey = """SELECT * FROM
                                users
                               WHERE
                                public_key = %(public_key)s"""

    select_user_by_alias = """SELECT * FROM
                                 users
                                WHERE
                                 alias = %(alias)s"""

    select_user_by_pubkey_encr = """SELECT * FROM
                                     users
                                    WHERE
                          public_key_encryption = %(public_key_encryption)s"""

    select_user_by_id = """SELECT * FROM
                            users
                           WHERE
                            user_id = %(user_id)s"""

    select_post_by_id = """SELECT * FROM
                            posts
                           WHERE
                            post_id = %(post_id)s"""

    # Warning: this fetches all the user's posts from the database. For
    # something more scalable, it might be better to fetch n posts by the
    # given user.
    select_posts_by_user_id = """SELECT * FROM
                                  posts
                                 WHERE
                                  user_id = %(user_id)s"""

    def __init__(self, host, username,
                 password, db="naclpostdb", charset="utf8"):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__db = db
        self.__charset = charset

        self.connect()

    def connect():
        self.con = pymysql.connect(host=self.__host, user=self.__username,
                                   password=self.__password, db=self.__db,
                                   charset=self.__charset,
                                   cursorclass=pymysql.cursors.DictCursor)

    def disconnect():
        self.con.close()
