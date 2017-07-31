# simple-password-cracker
Educational script for cracking passwords with a wordlist given a hash.

First, you need a wordlist. This is any file with a list of possible passwords in plain text.

## Usage

To create a hash for the cracker to work with, use `hash.py`

```shell
python hash.py md5 password123 >password.txt
```

You'll get a file, `password.txt`. This contains the hash for *password123*

To try cracking the password, use `cracker.py`.

```shell
python cracker.py md5 password.txt rockyou.txt
```
```
Cracking...
Found password:  password123
Completed in  0.00323796272278 seconds
Done.
```

### Supported hashes
*md5*
*sha1*
*sha224*
*sha256*
*sha512*
