class AmericanDevice:
    def __init__(self, power=110):
        self.power = power


class EuropeanSocket:
    def provide_electricity(self):
        return 220


class Adapter:
    def __init__(self, american_device):
        self.american_device = american_device

    def provide_electricity(self, european_socket):
        self.american_device.power = european_socket.provide_electricity() / 2
        return f"connected and powered with {self.american_device.power} V"


american_device1 = AmericanDevice(108)
european_socket1 = EuropeanSocket()
adapter1 = Adapter(american_device1)
print(adapter1.provide_electricity(european_socket1))
