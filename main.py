import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from TV_GUI import Ui_TV_Remote
from TV_logic import Television

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_TV_Remote()
    ui.setupUi(mainWindow)

    # Initialize the Television logic
    television = Television(ui.powerButton, [ui.channel1Radio, ui.channel2Radio, ui.channel3Radio,
                                             ui.channel4Radio, ui.channel5Radio, ui.channel6Radio,
                                             ui.channel7Radio, ui.channel8Radio, ui.channel9Radio,
                                             ui.channel10Radio], ui.volumeSlider, ui.muteBox,
                            ui.statusLabel, ui.channelOutput, ui.titleOutput, ui.channelGuide)

    mainWindow.show()

    # Prevent application from exiting when main window is closed
    sys.exit(app.exec())
