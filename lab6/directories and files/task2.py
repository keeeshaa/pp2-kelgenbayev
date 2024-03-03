import os

def check(path):
    status = {}
    status['exist'] = os.path.exists(path)
    status['read'] = os.access(path, os.R_OK)
    status['write'] = os.access(path, os.W_OK)
    status['execute'] = os.access(path, os.X_OK)

    return status

if __name__ == "__main__":
    path = input("Enter the path to check access: ")

    access = check(path)

    print("Existence:", access['exist'])
    print("Readability:", access['read'])
    print("Writability:", access['write'])
    print("Executability:", access['execute'])
