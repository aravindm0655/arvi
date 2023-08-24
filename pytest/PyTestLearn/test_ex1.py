import pytest
import test_ex1_frame


@pytest.fixture
def setup():
    print("open")
    yield
    print("close")

def test_1(setup):
    test_ex1_frame.loginpage1()
    test_ex1_frame.test_url1()
    print("url tested")

def test_2(setup):
    test_ex1_frame.loginpage1()
    test_ex1_frame.test_url1()
    print("url tested")
    
def test_3(setup):
    test_ex1_frame.loginpage1()
    test_ex1_frame.test_url1()
    print("url tested")
    
def test_4(setup):
    test_ex1_frame.loginpage1()
    test_ex1_frame.test_url1()
    print("url tested")


def test_5(setup):
    test_ex1_frame.loginpage1()
    test_ex1_frame.test_url1()
    print("url tested")
    
    
def test_6(setup):
    test_ex1_frame.loginpage1()
    test_ex1_frame.test_url1()
    print("url tested")

#https://blazedemo.com/