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

import exceptions as exc


class NaclPostDb:
    con = None
    cur = None

    # SQL queries

    # Add a user to the database; specify alias and public keys for signing
    # and encryption.
    _add_user = """INSERT INTO
            users
                (alias, public_key, public_key_encryption)
            VALUES
                (%(alias)s, %(public_key)s, %(public_key_encryption)s)"""

    # Add a user to the database, but only specify the alias and public key
    # for signing, not for encryption.
    _add_user_no_encr = """INSERT INTO
            users
                (alias, public_key)
            VALUES
                (%(alias)s, %(public_key)s)"""

    # Add a new post to the database.
    _add_post = """INSERT INTO
                    posts
                        (user_id, post_text)
                  VALUES
                        (%(user_id)s, %(post_text)s)"""

    # Select a user by their public key for signing
    _select_user_by_pubkey = """SELECT * FROM
                                users
                               WHERE
                                public_key = %(public_key)s"""

    # Select a user by their alias
    _select_user_by_alias = """SELECT * FROM
                                 users
                                WHERE
                                 alias = %(alias)s"""

    # Select a user by their public key for encryption
    _select_user_by_pubkey_encr = """SELECT * FROM
                                     users
                                    WHERE
                          public_key_encryption = %(public_key_encryption)s"""

    # Select a user by their user ID
    _select_user_by_id = """SELECT * FROM
                            users
                           WHERE
                            user_id = %(user_id)s"""

    # Select a post by its ID
    _select_post_by_id = """SELECT * FROM
                            posts
                           WHERE
                            post_id = %(post_id)s"""

    # Warning: this fetches all the user's posts from the database. For
    # something more scalable, it might be better to fetch n posts by the
    # given user.
    _select_posts_by_user_id = """SELECT * FROM
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
        self.cur = self.con.cursor()

    def connect(self):
        """Connect to the database."""

        self.con = pymysql.connect(host=self.__host, user=self.__username,
                                   password=self.__password, db=self.__db,
                                   charset=self.__charset,
                                   cursorclass=pymysql.cursors.DictCursor)

    def disconnect(self):
        """Close the connection with the database."""

        self.con.close()

    #
    # Simple get methods
    #

    def get_user_by_pubkey(self, pubkey):
        """Get all information of a user selected via the public key for
        signatures."""

        self.cur.execute(self._select_user_by_pubkey, {"public_key": pubkey})
        return self.cur.fetchone()

    def get_user_by_id(self, user_id):
        """Get all information of a user selected via the user id."""

        try:
            user_id = int(user_id)
        except ValueError:
            raise exc.InvalidIdError(user_id)

        self.cur.execute(self._select_user_by_id, {"user_id": user_id})
        return self.cur.fetchone()

    def get_user_by_alias(self, alias):
        """Get all information of a user selected via the alias."""

        self.cur.execute(self._select_user_by_alias, {"alias": alias})
        return self.cur.fetchone()

    def get_user_by_pubkey_encr(self, pubkey):
        """Get all information of a user selected via their public key for
        encryption."""

        self.cur.execute(self._select_user_by_pubkey_encr,
                         {"public_key_encryption": pubkey})
        return self.cur.fetchone()

    def get_post_by_post_id(self, post_id):
        """Get a post by its id."""

        try:
            post_id = int(post_id)
        except ValueError:
            raise exc.InvalidIdError(post_id)

        self.cur.execute(self._select_post_by_id, {"post_id": post_id})
        return self.cur.fetchone()

    def get_posts_by_user_id(self, user_id):
        """Get all posts made by a given user.

        Warning: this method currently doesn't scale at all.
        """

        try:
            user_id = int(user_id)
        except ValueError:
            raise exc.InvalidIdError(user_id)
        self.cur.execute(self._select_posts_by_user_id, {"user_id": user_id})
        return self.cur.fetchall()

    #
    # Simple check methods
    #

    def pubkey_is_registered(self, pubkey):
        """Check if a given public key for signing is registered with the
        service."""

        if self.get_user_by_pubkey(pubkey) is None:
            return False

        return True

    def alias_is_registered(self, alias):
        """Check if a given alias is registered with the service."""

        if self.get_user_by_alias(alias) is None:
            return False

        return True

    def pubkey_encr_is_registered(self, pubkey):
        """Check if a given public key for encryption is registered with the
        service."""

        if self.get_user_by_pubkey_encr(pubkey) is None:
            return False

        return True

    #
    # Write methods
    #

    def register_user(self, alias, public_key, public_key_encr=None):
        """Register a new user with the service."""

        if self.alias_is_registered(alias):
            # The given alias is already registered.
            raise exc.AlreadyRegisteredError(alias)

        if self.pubkey_is_registered(public_key):
            # The given public key for signing is already registered.
            raise exc.AlreadyRegisteredError(public_key)

        if public_key_encr is not None:
            if self.pubkey_encr_is_registered(public_key_encr):
                raise exc.AlreadyRegisteredError(public_key_encr)

            # Register a user with a public key for encryption.
            self.cur.execute(self._add_user,
                             {"alias": alias, "public_key": public_key,
                              "public_key_encryption": public_key_encr})
            self.con.commit()
        else:
            # Register a user without a public key for encryption.
            self.cur.execute(self._add_user_no_encr,
                             {"alias": alias, "public_key": public_key})
            self.con.commit()

    def add_post(self, user_id, post):
        """Add a new post."""

        self.cur.execute(self._add_post,
                         {"user_id": user_id, "post_text": post})
        self.con.commit()
