import pytest
import blaze_frame_elements

@pytest.fixture
def setup():
    print("open")
    yield
    print("close")
    
def test_1(setup):
    blaze_frame_elements.selectionpage("Paris","Rome")
    blaze_frame_elements.select_flight("/html/body/div[2]/table/tbody/tr[1]/td[1]/input")
    blaze_frame_elements.coustomer_id()

def test_2(setup):
    blaze_frame_elements.selectionpage("Paris","Rome")
    blaze_frame_elements.select_flight("/html/body/div[2]/table/tbody/tr[2]/td[1]/input")
    blaze_frame_elements.coustomer_id()
    
def test_3(setup):
    blaze_frame_elements.selectionpage("Paris","Rome")
    blaze_frame_elements.select_flight("/html/body/div[2]/table/tbody/tr[3]/td[1]/input")
    blaze_frame_elements.coustomer_id()

def test_4(setup):
    blaze_frame_elements.selectionpage("Paris","Rome")
    blaze_frame_elements.select_flight("/html/body/div[2]/table/tbody/tr[4]/td[1]/input")
    blaze_frame_elements.coustomer_id()
    
def test_5(setup):
    blaze_frame_elements.selectionpage("Paris","Rome")
    blaze_frame_elements.select_flight("/html/body/div[2]/table/tbody/tr[5]/td[1]/input")
    blaze_frame_elements.coustomer_id()
    
