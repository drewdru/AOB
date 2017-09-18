import QtQuick 2.6
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.1
import QtQuick.Controls.Material 2.1
// import QtMultimedia 5.6 // Python 3.5.2 PyQt5 5.9 DEAD END: libdeclarative_multimedia.so: (libQt5MultimediaQuick_p.so.5: cannot open shared object file: No such file or directory)libdeclarative_multimedia.so: (libQt5MultimediaQuick_p.so.5: cannot open shared object file: No such file or directory)

import "main.js" as App

import "../../AOI/qml/views"
import "../../AOI/qml/drawers"

Rectangle {

    Material.theme: Material.Dark
    Material.accent: Material.Red
    color: Material.color(Material.BlueGrey)

    id: rootWindow    
    anchors.fill: parent    
    width: 300; height: 300
    
    // MediaPlayer {
    //     id: player
    //     source: "./myclip1.avi"
    //     autoPlay: true
    // }

    // VideoOutput {
    //     id: videoOutput
    //     source: player
    //     anchors.fill: parent
    // }
}