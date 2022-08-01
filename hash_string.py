import hashlib

salt = "bd0af5dc9f694579bfe26995dede154e"  # should be hard-coded


def hash_string(_str: str):
    return hashlib.sha256((_str + salt).encode('utf-8')).hexdigest()


if __name__ == '__main__':
    s = "Python Bootcamp"
    print(hash_string(s))
