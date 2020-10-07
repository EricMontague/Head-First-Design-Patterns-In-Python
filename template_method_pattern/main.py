from coffee import Coffee
from tea import Tea


def main():
    tea = Tea()
    coffee = Coffee()

    tea.prepare_recipe()
    print()
    coffee.prepare_recipe()



if __name__ == "__main__":
    main()

