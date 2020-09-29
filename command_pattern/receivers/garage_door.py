class GarageDoor:
    def __init__(self):
        self._open = False

    def open(self):
        self._open = True
        print("Garage door is open")

    def close(self):
        self._open = False
        print("Garage door is closed")

    def stop(self):
        print("Garage door is stopped")

    def light_on(self):
        print("Garage light is on")

    def light_off(self):
        print("Garage light is off")
