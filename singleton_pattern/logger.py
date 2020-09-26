# Overidding the __new__ method


class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating object")
            cls._instance = object.__new__(cls)
            # extra stuff here
        return cls._instance


old_logger = Logger()
new_logger = Logger()
print(old_logger == new_logger)
