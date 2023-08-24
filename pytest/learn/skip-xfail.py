import pytest
import sys
@pytest.mark.skipif (sys.version_info< (3,9), reason="version is less")
def test_login():
    print("login done")
@pytest.mark.skip
def test_addtocart():
    print("items added")
@pytest.mark.xfail
def test_logout():
    print("logout done")