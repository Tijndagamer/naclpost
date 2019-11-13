# naclpost

Proof of concept microblogging service with pubkey authentication

It is an idea similar to my [PGPost](https://github.com/Tijndagamer/PGPost), except it
will use [libsodium](https://github.com/jedisct1/libsodium) for the cryptography instead
of PGP. This will make it more flexible, with the downside that you can't use a key that
you already have and other people trust.
