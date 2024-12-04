
class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None::
        """Initializes the television with defaults"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None::
        """Toggle the power state of the tv"""
        self.__status = not self.__status

    def mute(self) -> None::
        """Toggles the mute state of the television if it is on"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = 1
            else:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None::
        """Increase the channel by one, and make sure it doesn't exceed the maximum channel"""
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None::
        """Decreases the channel by one, and make sure it doesn't exceed the minimum channel"""
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None::
        """Increase the volume by one, and make sure it doesn't exceed the maximum volume"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = Television.MAX_VOLUME
            else:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self) -> None::
        """Decreases the volume by one, and make sure it doesn't exceed the mainimum channel"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = Television.MIN_VOLUME
            else:
                if self.__volume > Television.MAX_VOLUME:
                    self.__volume -= 1
                else:
                    self.__volume = 1

    def __str__(self) -> None::
        """Returns the current state of the tv"""
        volume_display = "0 (Muted)" if self.__muted else str(self.__volume)
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"
        