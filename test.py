from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)
def main():
    print(get_password_hash("example"))



if (__name__ == "__main__"):
    main()