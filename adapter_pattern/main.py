from turkey_adapter import TurkeyAdapter
from turkeys import WildTurkey
from ducks import MallardDuck


def main():
    mallard_duck = MallardDuck()

    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    test_duck(mallard_duck)

    print("\nThe Turkey Adpater says...")
    test_duck(turkey_adapter)


def test_duck(duck):
    duck.quack()
    duck.fly()


if __name__ == "__main__":
    main()
