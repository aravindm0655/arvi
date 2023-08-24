import pytest
import cred
@pytest.fixture

def setup():
    print("open")
    yield
    print("close")

def test_1(setup):
    cred.loginpage('student',"Password123")
    cred.test_url()
    print("url tested")

def test_2(setup):
    cred.loginpage('student',"Password123")
    cred.test_url()
    print("url tested")
    
def test_3(setup):
    cred.loginpage('student',"Password123")
    cred.test_url()
    print("url tested")
    
def test_4(setup):
    cred.loginpage('student',"Password123")
    cred.test_url()
    print("url tested")


def test_5(setup):
    cred.loginpage('student',"Password123")
    cred.test_url()
    print("url tested")
    
    
def test_6(setup):
    cred.loginpage('student',"Password123")
    cred.test_url()
    print("url tested")





    
