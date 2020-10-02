class HomeTheaterFacade:

    def __init__(self, amplifier, tuner, dvd_player, cd_player, projector, screen, lights, popper):
        self._amplifier = amplifier
        self._tuner = tuner
        self._dvd_player = dvd_player
        self._cd_player = cd_player
        self._projector = projector
        self._screen = screen
        self._lights = lights
        self._popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self._popper.on()
        self._popper.pop()
        self._lights.dim(10)
        self._screen.down()
        self._projector.on()
        self._projector.wide_screen_mode()
        self._amplifier.on()
        self._amplifier.set_dvd_player(self._dvd_player)
        self._amplifier.set_surround_sound()
        self._amplifier.set_volume(5)
        self._dvd_player.on()
        self._dvd_player.set_movie(movie)
        self._dvd_player.play_track(1)

    def end_movie(self):
        print("Shutting movie theater down...")
        self._popper.off()
        self._lights.on()
        self._screen.up()
        self._projector.off()
        self._amplifier.off()
        self._dvd_player.stop()
        self._dvd_player.eject()
        self._dvd_player.off()

    def listen_to_cd(self, cd_title):
        print("Get ready for an audiophile experience...")
        self._lights.on()
        self._amplifier.on()
        self._amplifier.set_volume(5)
        self._amplifier.set_cd_player(self._cd_player)
        self._amplifier.set_stereo_sound()
        self._cd_player.on()
        self._cd_player.set_cd_title(cd_title)
        self._cd_player.play_track(3)

    def end_cd(self):
        print("Shutting down cd...")
        self._amplifier.off()
        self._amplifier.set_cd_player(self._cd_player)
        self._cd_player.eject()
        self._cd_player.off()

    def listen_to_radio(self, frequency):
        print("Tuning in the airwaves...")
        self._tuner.on()
        self._tuner.set_frequency(frequency)
        self._amplifier.on()
        self._amplifier.set_volume(5)
        self._amplifier.set_tuner(self._tuner)

    def end_radio(self):
        print("Shutting down the tuner...")
        self._tuner.off()
        self._amplifier.off()
        

    

    