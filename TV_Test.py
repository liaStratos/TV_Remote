import unittest
from TV_logic import *
from TV_GUI import *
from main import *


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

        self.power_button = QPushButton()
        self.channel_radios = [QRadioButton() for _ in range(10)]
        self.volume_slider = QSlider()
        self.mute_box = QCheckBox()
        self.status_label = QLabel()
        self.channel_output_label = QLabel()
        self.title_output_label = QLabel()
        self.channel_guide = QTableWidget()

        self.tv = Television(self.power_button, self.channel_radios, self.volume_slider,
                             self.mute_box, self.status_label, self.channel_output_label,
                             self.title_output_label, self.channel_guide)

    def tearDown(self):
        self.app.quit()

    def test_power_button_clicked(self):
        self.power_button.click()
        self.assertEqual(self.tv.status, True)
        self.assertEqual(self.status_label.text(), "TV On")

        self.power_button.click()
        self.assertEqual(self.tv.status, False)
        self.assertEqual(self.status_label.text(), "TV Off")

    def test_volume_changed(self):
        self.volume_slider.setValue(5)
        self.assertEqual(self.tv.volume, 5)

    def test_mute_box_changed(self):
        self.mute_box.setChecked(True)
        self.assertEqual(self.tv.muted, True)
        self.assertEqual(self.tv.volume, 0)
        self.assertEqual(self.volume_slider.value(), 0)

        self.mute_box.setChecked(False)
        self.assertEqual(self.tv.muted, False)


if __name__ == '__main__':
    unittest.main()
