from amplifier import Amplifier
from cd_player import CDPlayer
from dvd_player import DvdPlayer
from popcorn_popper import PopcornPopper
from projector import Projector
from screen import Screen
from theater_lights import TheaterLights
from tuner import Tuner
from home_theater_facade import HomeTheaterFacade



def main():
    amp = Amplifier("Top-O-Line-Amplifier")
    tuner = Tuner("Top-O-Line AM/FM Tuner", amp)
    dvd_player = DvdPlayer("Top-O-Line DVD Player", amp)
    cd_player = CDPlayer("Top-O-Line CD Player", amp)
    projector = Projector("Top-O-Line Projector", dvd_player)
    lights = TheaterLights("Theater Ceiling Lights")
    screen = Screen("Theater Screen")
    popper = PopcornPopper("Popcorn Popper")

    home_theater = HomeTheaterFacade(
        amp, tuner, dvd_player, cd_player, projector, screen, lights, popper
    )
    home_theater.watch_movie("Lord of the Rings")
    print()
    home_theater.end_movie()
    print()


    # home_theater.listen_to_cd("All Blues")
    # print()
    # home_theater.end_cd()
    # print()

    # home_theater.listen_to_radio(98.5)
    # print()
    # home_theater.end_radio()



if __name__ == "__main__":
    main()