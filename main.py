"""
    @package main
    Run PyQt app
"""

import sys
import os
sys.path.append('./AOI')

from PyQt5.QtQml import QQmlEngine
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtGui import QIcon
import contextSettings



if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)
    myApp.setWindowIcon(QIcon('./images/icon.png'))

    # Create a View and set its properties
    appView = QQuickView()
    appView.setMinimumHeight(640)
    appView.setMinimumWidth(1024)
    appView.setTitle('roadLaneFinding')

    # Create context
    engine = appView.engine()
    engine.quit.connect(myApp.quit)
    context = engine.rootContext()

    context = contextSettings.setAOIContext(context)

    # Show the View
    appView.setSource(QUrl('./qml/mainWindow/main.qml'))
    appView.show()

    # Execute the Application and Exit
    sys.exit(myApp.exec_())
