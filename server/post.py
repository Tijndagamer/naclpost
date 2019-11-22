#!/usr/bin/python3
"""
    post.py
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

# Cryptography libraries
import nacl.encoding
import nacl.signing

import configparser

from db import NaclPostDb

# This should be read from a config file later.
ENCODER = nacl.encoding.URLSafeBase64Encoder


class NaclPost:
    _db = None

    def __init__(self, configfile="naclpost.ini"):
        # Read the config file
        self._config = configparser.ConfigParser()
        self._config.read(configfile)

        # Create the NaclPostDb object
        self._db = NaclPostDb(self._config["db"]["host"],
                              self._config["db"]["username"],
                              self._config["db"]["password"],
                              self._config["db"]["database"])

    def post(self, raw_text, pubkey):
        """Handle and verify an incoming post.

        The contents of the arguments should not be trusted.
        """

        pass
