####Just notes

class DHT:
    def __init__(self, data):
        self.data['one'] = '1'
        self.data['two'] = '2'
        self.data['three'] = '3'
    def showData(self):
        print(self.data)

if __name__ == '__main__': DHT().showData()




class DHT:
    def __init__(self):
        self.data = {}
        self.data['one'] = '1'
        self.data['two'] = '2'
        self.data['three'] = '3'
    def showData(self):
        print(self.data)

if __name__ == '__main__':
    DHT().showData()
