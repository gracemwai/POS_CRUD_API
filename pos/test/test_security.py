from core.security import hash_password, verify_password, create_access_token, decode_access_token
def test_hash_password():
    password="testpassword"
    hashed_password= hash_password(password)

    assert isinstance(hashed_password, str)
    assert hashed_password !=password

def test_verify_password():
    password = "testpassword"
    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password)
    assert not verify_password("testpassword1", hashed_password) 


def test_create_access_token():
    """Isolate and test token generation."""
    user_data = {"sub": "1"}
    
    token = create_access_token(data=user_data)
    
    assert isinstance(token, str)
    assert len(token) > 0

def test_decode_access_token():
    """Isolate and test token decoding and extraction."""
    user_data = {"sub": "1"}
    
    token = create_access_token(data=user_data)
    decoded_payload = decode_access_token(token)
    assert decoded_payload["sub"] == "1"
    assert "exp" in decoded_payload

