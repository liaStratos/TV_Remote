class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Function defines the initial settings fot the variable
        param a: status on/off
        param b: muted on/off
        param c: volume set at minimum of 0
        param d: channel set at minimum of 0
        """

        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Function initialized the status variable
        param a: status of the television off
        """
        self.status = not self.status

    def mute(self) -> None:
        """
        Function initialized the muted variable
        param a: mute of the television off
        """
        self.muted = not self.muted

    def channel_up(self) -> None:
        """
        Function makes the channel increase on call
        param a: channel of the tv, increases by 1
        """
        if self.status:
            self.channel = (self.channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Function makes the channel decrease on call
        param a: channel of the tv, decreases by 1
        """
        if self.status:
            self.channel = (self.channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Function makes the volume increase on call
        param a: volume of the tv, increases by 1
        """
        if self.status:
            if self.volume < self.MAX_VOLUME:
                self.volume += 1
                if self.muted:
                    self.muted = False

    def volume_down(self) -> None:
        """
        Function makes the volume decrease on call
        param a: volume of the tv, decreases by 1
        """
        if self.status:
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1
                if self.muted:
                    self.muted = False

    def __str__(self) -> str:
        return f'Power - {self.status}, Channel - {self.channel}, Volume - {self.volume}.'
