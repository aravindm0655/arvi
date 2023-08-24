import pytest
import from_excel


@pytest.fixture
def setup():
    print("open")
    yield
    print("close")

def test_1(setup):
    from_excel.loginpage1("aravind","mjbvfdtryctvubijl")
    from_excel.test_url1()
    print("url tested")

def test_2(setup):
    from_excel.loginpage1("aravind","mjbvfdtryctvubijl")
    from_excel.test_url1()
    print("url tested")
    
def test_3(setup):
    from_excel.loginpage1("aravind","mjbvfdtryctvubijl")
    from_excel.test_url1()
    print("url tested")
    
def test_4(setup):
    from_excel.loginpage1("aravind","mjbvfdtryctvubijl")
    from_excel.test_url1()
    print("url tested")


def test_5(setup):
    from_excel.loginpage1("aravind","mjbvfdtryctvubijl")
    from_excel.test_url1()
    print("url tested")
    
    
def test_6(setup):
    from_excel.loginpage1("aravind","mjbvfdtryctvubijl")
    from_excel.test_url1()
    print("url tested")

