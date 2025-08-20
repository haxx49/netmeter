from src import netmeter

def test_netmeter():
    assert netmeter.main.connected(True) == True
    assert netmeter.main.connected(False) == False