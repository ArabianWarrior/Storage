from src.services.auth import AuthService


#Если мы хотим протестировать какую либо функицию
#то после def обязательно нужно написать в начале функции
#test. Например: test_add_hotel, test_delete_hotel.

def test_decode_access_token():
    data = {"user_id": 1}
    jwt_token = AuthService().create_access_token(data)

    assert jwt_token
    assert isinstance(jwt_token, str)

    payload = AuthService().decode_token(jwt_token)
    assert payload
    assert payload["user_id"] == data["user_id"]

def test_verify_password():
    auth_service = AuthService()
    password = "password"
    hashed_password = auth_service.hash_password(password)

    result = auth_service.verify_password(password, hashed_password)
    assert result == True

def test_hash_password():
    password = "my_password"
    hashed = AuthService().hash_password(password)
    assert hashed != password  # хеш не равен оригиналу
    assert isinstance(hashed, str)
    assert len(hashed) > 0