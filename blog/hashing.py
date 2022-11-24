from passlib.context import CryptContext


class Hash:

    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def encryptPassword(self, password: str):
        return self.pwd_context.hash(password)

    def verifyPassword(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)
