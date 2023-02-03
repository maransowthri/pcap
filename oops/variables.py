class Home:
    counter = 0

    def __init__(self, address, area, prize):
        self.address = address
        self.area = area
        self.prize = prize
        # Local Variable
        cant_access = 'Ghost'
        Home.counter += 1

    def describe(self):
        print(
            f'The home located at {self.address} of area {self.area} costs {self.prize}')
    
home1 = Home('113 Malar Nagar Sivaganga', '4.5 Cents', 4_00_000)
print('Class Variable', Home.counter)
print('Instance Variable', home1.address)