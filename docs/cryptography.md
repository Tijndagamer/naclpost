# naclpost cryptography

naclpost uses [libsodium](https://github.com/jedisct1/libsodium) via the 
[PyNaCl](https://pynacl.readthedocs.io/en/stable/) Python bindings. Since naclpost only
uses the digitale signature scheme that is implemented in libsodium, only a relatively
small part of the library is used. If one however would want to implement private posts
for a specific recipient, libsodium's public key encryption could be used. The same key
pair can be used for encryption and signing, but it would probably be better to have
separate key pairs.

libsodium offers no choice of key parameters or algorithms. The only choice we have to
make is which encoding we will employ to encode keys and signed messages. PyNaCl offers
a raw, hex, base16, base32, base64 and URLSafeBase64 encoders. naclpost will by default
use the URLSafeBase64 encoder. This setting should be easily changed.
