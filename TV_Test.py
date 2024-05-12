import unittest
from PyQt6.QtWidgets import QApplication
from TV_logic import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.tv = Television()

    def test_initial_status(self):
        self.assertFalse(self.tv.status)
        self.assertEqual(self.tv.volume, 0)
        self.assertEqual(self.tv.channel, 0)

    def test_power_button_clicked(self):
        # Initially, TV is off
        self.assertEqual(self.tv.statusLabel.text(), "TV Off")

        # Click power button to turn on
        self.tv.on_power_button_clicked()
        self.assertTrue(self.tv.status)
        self.assertEqual(self.tv.statusLabel.text(), "TV On")

        # Click power button again to turn off
        self.tv.on_power_button_clicked()
        self.assertFalse(self.tv.status)
        self.assertEqual(self.tv.statusLabel.text(), "TV Off")

    # Add more test cases for other methods as needed

    def tearDown(self):
        self.app.quit()


if __name__ == "__main__":
    unittest.main()
