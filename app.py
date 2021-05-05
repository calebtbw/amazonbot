import hashlib
import os

from common.license_hash import license_hash


def sha256sum(filename):
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, "rb", buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


if os.path.exists("LICENSE") and sha256sum("LICENSE") in license_hash:
    s = """
    AmazonBot - Automated Purchasing Program made in Python
    Copyright (C) 2021 Caleb T.
    
    Made for Bytesize Technologies Pte Ltd.
    """

    print(s)
else:
    print(
        "AmazonBot - Automated Purchasing Program made in Python\n"
        "Copyright (C) 2021 Caleb T.\n"
    
        "Made for Bytesize Technologies Pte Ltd."
    )


def notfound_message(exception):
    print(exception)
    print(
        f"Missing '{exception.name}' module.  If you ran 'pipenv install', try 'pipenv install {exception.name}'"
    )
    print("Exiting...")


try:
    from cli import cli
except ModuleNotFoundError as e:
    notfound_message(e)
    exit(0)

if __name__ == "__main__":
    try:
        cli.main()
    except ModuleNotFoundError as e:
        notfound_message(e)
        exit(0)