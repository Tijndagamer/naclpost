# naclpost

Proof of concept microblogging service with pubkey authentication

It is an idea similar to my [PGPost](https://github.com/Tijndagamer/PGPost), except it
will use [libsodium](https://github.com/jedisct1/libsodium) for the cryptography instead
of PGP. This will make it more flexible, with the downside that you can't use a key that
you already have and other people trust.

## Dependencies

PyPI packages:
* Flask
* PyNaCl
* PyMySQL

PyPi packages for development:
* pytest
* Flake8

## License and copyright

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
