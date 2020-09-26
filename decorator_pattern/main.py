from coffees import Espresso, DarkRoast, Decaf, HouseBlend
from condiments import SteamedMilk, Soy, Mocha, Whip


def main():
    # regular beverage
    espresso = Espresso("Espresso")
    print(espresso.description, espresso.cost())

    # decorated beverage
    dark_roast = DarkRoast("Dark roast")
    dark_roast_with_mocha = Mocha(dark_roast)
    double_mocha = Mocha(dark_roast_with_mocha)
    double_mocha_with_whip = Whip(double_mocha)
    print(double_mocha_with_whip.description, double_mocha_with_whip.cost())

    # another decorated beverage
    house_blend = HouseBlend("House Blend")
    house_blend_with_soy = Soy(house_blend)
    house_blend_with_soy_and_mocha = Mocha(house_blend_with_soy)
    house_blend_with_soy_and_mocha_and_whip = Whip(
        house_blend_with_soy_and_mocha
    )
    print(
        house_blend_with_soy_and_mocha_and_whip.description,
        house_blend_with_soy_and_mocha_and_whip.cost(),
    )


if __name__ == "__main__":
    main()

