from typing import List
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class Television:
    """A class representing a television."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 10
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 10

    def __init__(self, power_button: QPushButton, channel_radios: List[QRadioButton],
                 volume_slider: QSlider, mute_box: QCheckBox, status_label: QLabel,
                 channel_output_label: QLabel, title_output_label: QLabel,
                 channel_guide: QTableWidget) -> None:
        """Initialize the Television object."""
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL

        self.power_button = power_button
        self.channel_radios = channel_radios
        self.volume_slider = volume_slider
        self.mute_box = mute_box
        self.status_label = status_label
        self.channel_output_label = channel_output_label
        self.title_output_label = title_output_label
        self.channel_guide = channel_guide

        self.power_button.clicked.connect(self.on_power_button_clicked)
        self.volume_slider.valueChanged.connect(self.on_volume_changed)
        self.mute_box.stateChanged.connect(self.on_mute_box_changed)

        self.populate_channel_guide()

    def populate_channel_guide(self) -> None:
        """Populate the channel guide table view."""
        self.channel_guide.setColumnCount(3)
        self.channel_guide.setHorizontalHeaderLabels(["Channel #", "Channel Title", "Program Title"])

        channel_titles = ["ABC", "NBC", "WOWT", "CBS", "PBS", "NICK", "DIS", "CNN", "FOX", "AMC"]
        program_titles = ["Wheel of Treasure", "Dun Dun", "Omaha News", "The Money Is Right",
                          "Wild Krafts", "Shronk II", "Open Seasoning", "Wallace and Grommet",
                          "Saturday Night Life", "The Stalking Dead"]

        for i, (channel_title, program_title) in enumerate(zip(channel_titles, program_titles)):
            self.channel_guide.insertRow(i)
            self.channel_guide.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.channel_guide.setItem(i, 1, QTableWidgetItem(channel_title))
            self.channel_guide.setItem(i, 2, QTableWidgetItem(program_title))

    def on_power_button_clicked(self) -> None:
        """Handle power button click."""
        self.status = not self.status
        self.status_label.setText("TV On" if self.status else "TV Off")
        self.update_gui()

    def on_volume_changed(self, value: int) -> None:
        """Handle volume slider value change."""
        if not self.muted and self.status:
            self.volume = value
            self.update_gui()

    def on_mute_box_changed(self, state: int) -> None:
        """Handle mute box state change."""
        self.muted = state == Qt.CheckState.Checked
        if self.muted:
            self.volume = 0
            self.volume_slider.setValue(0)
        self.update_gui()

    def update_gui(self) -> None:
        """Update GUI elements."""
        self.channel_output_label.setText(f"Channel {self.channel}")
        self.title_output_label.setText(f"Program Title {self.channel}")
        self.volume_slider.setValue(self.volume)

        for i, radio in enumerate(self.channel_radios):
            radio.setChecked(self.channel == i + 1)
