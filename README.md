# Notes for non-Devs

  This is a cool little corky sussy silly baka project that I made a couple years ago (without documentation, and still remember what every function does).

  It basically creates an interface on your monitor that detects mouse movement inside it, collecting coordinates, then transforming it using simple amogus maths, then sending commands to the arduino which handles everything (if correctly configured). Much simillar to what it would feel to play a match of world of Tanks.. if a tank would be controlled with a mouse.


# Notes for Devs

- Currently, uncommenting everything, except for functions 'fire()' and 'ceasefire()', without adding a third servo motor, without connecting and configuring an arduino will lead to a crash.

- The arduino model used for creation and testing was the 'tatuino diecimila griffus 28:1,1'. The premade driver for the arduino is 'Firmata'

- The default arduino ports used to connect to each axis are:
    x = 9
    y = 10
    z = 11

- All code related to axis 'Z' on /main.py reffers to a third dimension, which could not be implemented on a traditional mouse.


## Just some more notes

```py
class DHT:
    def __init__(self, data):
        self.data['one'] = '1'
        self.data['two'] = '2'
        self.data['three'] = '3'
    def showData(self):
        print(self.data)

if __name__ == '__main__': DHT().showData()
```

```py
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
```
