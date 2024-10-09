from werkzeug.security import generate_password_hash


def hash_password(password):
    return generate_password_hash(password=password, method='pbkdf2:sha256')


if __name__ == '__main__':
    print(hash_password('admin12345'))