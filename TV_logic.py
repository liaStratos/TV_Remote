from PyQt6.QtWidgets import *
from TV_GUI import Ui_TV_Remote


class Television(QMainWindow, Ui_TV_Remote):
    """A class representing a television."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 10
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 10

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.powerButton.clicked.connect(self.on_power_button_clicked)
        self.muteButton.clicked.connect(self.on_mute_button_clicked)
        self.volumeSlider.valueChanged.connect(self.on_volume_changed)

        self.inputRadio.clicked.connect(self.enable_channel_radios)
        self.cableRadio.clicked.connect(self.enable_channel_radios)

        self.inputRadio.toggled.connect(self.on_radio_button_toggled)
        self.cableRadio.toggled.connect(self.on_radio_button_toggled)

        self.lineEdit.returnPressed.connect(self.on_line_edit_finished)

        self.channel1Radio.clicked.connect(self.on_channel_selected)
        self.channel2Radio.clicked.connect(self.on_channel_selected)
        self.channel3Radio.clicked.connect(self.on_channel_selected)
        self.channel4Radio.clicked.connect(self.on_channel_selected)
        self.channel5Radio.clicked.connect(self.on_channel_selected)
        self.channel6Radio.clicked.connect(self.on_channel_selected)
        self.channel7Radio.clicked.connect(self.on_channel_selected)
        self.channel8Radio.clicked.connect(self.on_channel_selected)
        self.channel9Radio.clicked.connect(self.on_channel_selected)
        self.channel10Radio.clicked.connect(self.on_channel_selected)

        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL

        self.populate_channel_guide()

    def populate_channel_guide(self) -> None:
        """Populate the channel guide table view."""
        self.channelGuide.setColumnCount(3)
        self.channelGuide.setHorizontalHeaderLabels(["Channel #", "Channel Title", "Program Title"])

        channel_titles = ["ABC", "NBC", "WOWT", "CBS", "PBS", "NICK", "DIS", "CNN", "FOX", "AMC"]
        program_titles = ["Wheel of Treasure", "Dun Dun", "Omaha News", "The Money Is Right",
                          "Wild Krafts", "Shronk II", "Open Seasoning", "Wallace and Grommet",
                          "Saturday Night Life", "The Stalking Dead"]

        for i, (channel_title, program_title) in enumerate(zip(channel_titles, program_titles)):
            self.channelGuide.insertRow(i)
            self.channelGuide.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.channelGuide.setItem(i, 1, QTableWidgetItem(channel_title))
            self.channelGuide.setItem(i, 2, QTableWidgetItem(program_title))

    def enable_channel_radios(self) -> None:
        """Enable/disable channel radios based on inputRadio or cableRadio selection."""
        is_cable_selected = self.cableRadio.isChecked()
        for radio in [self.channel1Radio, self.channel2Radio, self.channel3Radio,
                      self.channel4Radio, self.channel5Radio, self.channel6Radio,
                      self.channel7Radio, self.channel8Radio, self.channel9Radio,
                      self.channel10Radio]:
            radio.setEnabled(is_cable_selected)

    def on_power_button_clicked(self) -> None:
        """Handle power button click."""
        self.status = not self.status
        if self.status:
            self.statusLabel.setText("TV On")
            self.channelGuideScroll.show()
            self.inputRadio.setEnabled(True)
            self.cableRadio.setEnabled(True)
            for i in range(1, 11):
                getattr(self, f"channel{i}Radio").setEnabled(True)
        else:
            self.statusLabel.setText("TV Off")
            self.channelGuideScroll.hide()
            self.inputRadio.setEnabled(False)
            self.cableRadio.setEnabled(False)
            for i in range(1, 11):
                getattr(self, f"channel{i}Radio").setEnabled(False)
        self.update_gui()

    def on_volume_changed(self, value: int) -> None:
        """Handle volume slider value change."""
        if not self.muted and self.status:
            self.volume = value
            self.volumeOutput.setText(str(value))
            self.update_gui()

    def on_mute_button_clicked(self):
        """Handle mute button click."""
        if self.muteButton.text() == "Mute Vol":
            self.muteButton.setText("Muted")
            self.volumeSlider.setEnabled(False)
            self.volumeOutput.setText("0")
        else:
            self.muteButton.setText("Mute Vol")
            self.volumeSlider.setEnabled(True)
            self.volumeOutput.setText(str(self.volume))

    def on_line_edit_finished(self) -> None:
        """Handle line edit input finished."""
        if self.lineEdit.isEnabled():
            input_text = self.lineEdit.text()
            self.channelOutput.setText('N/A')
            self.titleOutput.setText(input_text)

    def on_radio_button_toggled(self) -> None:
        """Handle radio button toggled."""
        self.lineEdit.setEnabled(self.inputRadio.isChecked())

    def on_cable_radio_clicked(self):
        """Handle cable radio button click."""
        if self.cableRadio.isChecked():
            for radio in [self.channel1Radio, self.channel2Radio, self.channel3Radio,
                          self.channel4Radio, self.channel5Radio, self.channel6Radio,
                          self.channel7Radio, self.channel8Radio, self.channel9Radio,
                          self.channel10Radio]:
                radio.setEnabled(True)
        else:
            for radio in [self.channel1Radio, self.channel2Radio, self.channel3Radio,
                          self.channel4Radio, self.channel5Radio, self.channel6Radio,
                          self.channel7Radio, self.channel8Radio, self.channel9Radio,
                          self.channel10Radio]:
                radio.setEnabled(False)
                radio.setChecked(False)

    def on_channel_selected(self) -> None:
        """Handle channel radio button selection."""
        if self.status:
            for i in range(1, 11):
                radio_button = getattr(self, f"channel{i}Radio")
                if radio_button.isChecked():
                    channel_number = i
                    channel_title, program_title = self.get_channel_program_titles(channel_number)
                    self.channelOutput.setText(f"{channel_title}")
                    self.titleOutput.setText(f"{program_title}")
                    break

    @staticmethod
    def get_channel_program_titles(channel_number: int) -> tuple[str, str]:
        """Return channel and program titles based on the channel number."""
        channel_mapping = {
            1: ("ABC", "Wheel of Treasure"),
            2: ("NBC", "Dun Dun"),
            3: ("WOWT", "Omaha News"),
            4: ("CBS", "The Money Is Right"),
            5: ("PBS", "Wild Krafts"),
            6: ("NICK", "Shronk II"),
            7: ("DIS", "Open Seasoning"),
            8: ("CNN", "Wallace and Grommet"),
            9: ("FOX", "Saturday Night Life"),
            10: ("AMC", "The Stalking Dead")
        }
        return channel_mapping.get(channel_number, ("N/A", "N/A"))

    def update_gui(self) -> None:
        """Update the GUI based on status, volume, and channel."""
        self.volumeSlider.setEnabled(self.status)
        self.muteButton.setEnabled(self.status)
        self.volumeSlider.setValue(self.volume)

        if self.status:
            self.nowPlaying.setText("Now Playing...")
        else:
            self.nowPlaying.setText("TV Off")
            self.channelOutput.setText("N/A")
            self.titleOutput.setText("N/A")
