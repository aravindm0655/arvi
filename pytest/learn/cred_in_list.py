import pytest
@pytest.mark.parametrize("username,password",
                        [
                             ("arvi","1234",),
                             ("arul","1234"),
                             ("nandha","1234")
                        ]
                        ) 
def test_login(username, password):
    print(username)
    print(password) 