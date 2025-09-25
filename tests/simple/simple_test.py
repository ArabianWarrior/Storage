# # tests/simple/test_basic_auth.py
# import jwt
# from passlib.context import CryptContext
# from datetime import datetime, timezone, timedelta

# # Скопируй только логику без импортов
# class SimpleAuthTest:
#     pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
#     def hash_password(self, password: str) -> str:
#         return self.pwd_context.hash(password)
    
#     def verify_password(self, plain_password: str, hashed_password: str) -> bool:
#         return self.pwd_context.verify(plain_password, hashed_password)

# def test_hash_password():
#     auth = SimpleAuthTest()
#     password = "test123"
#     hashed = auth.hash_password(password)
#     assert hashed != password
#     assert len(hashed) > 0

# def test_verify_password():
#     auth = SimpleAuthTest()
#     password = "test123"
#     hashed = auth.hash_password(password)
#     assert auth.verify_password(password, hashed) == True
#     assert auth.verify_password("wrong", hashed) == False