#!/usr/bin/python3
"""
    exceptions.py
    Custom exceptions for the naclpost server
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


class Error(Exception):
    """Base class for custom exceptions."""

    pass


class UnknownPublicKeyError(Error):
    """Exception raised when a given public key is either not registered with
    the service, or has a wrong encoding scheme.

    Attributes:
        pubkey -- the public key that caused the exception to be raised
    """

    def __init__(self, pubkey):
        self.pubkey = pubkey

class InvalidIdError(Error):
    """Exception raised when a given ID is not of the type or form that we
    expect it to be.

    Attributes:
        eid -- the id that caused the exception to be raised
    """

    def __init__(self, eid):
        self.eid = eid

class AlreadyRegisteredError(Error):
    """Exception raised when a certain public key or alias is already
    registered with the service.

    Attributes:
        value -- the public key or alias that is already registered.
    """

    def __init__(self, value):
        self.value = value
