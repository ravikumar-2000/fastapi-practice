from passlib.context import CryptContext


class Hash:

    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def encryptPassword(self, password: str):
        return self.pwd_context.hash(password)

    def decryptPassword(self, password: str):
        return
