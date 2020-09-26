from duck_subclasses import MallardDuck, ModelDuck
from fly_behaviors import FlyRocketPowered


def main():
    """Duck simular program."""
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()


if __name__ == "__main__":
    main()

