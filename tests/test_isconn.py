from src.netmeter import main

def test_netmeter():
    assert main.connected(True) is True
    assert main.connected(False) is False