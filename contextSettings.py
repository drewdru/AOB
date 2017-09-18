from PyQt5.QtCore import QDir 

from AOI.controllers.mainController import MainController
from AOI.controllers.noiseGeneratorController import NoiseGeneratorController
from AOI.controllers.colorCorrectorController import ColorCorrectorController
from AOI.controllers.filtersController import FiltersController
from AOI.controllers.binarizeController import BinarizeController
from AOI.controllers.morphologyController import MorphologyController
from AOI.controllers.segmentationController import SegmentationController

def setAOIContext(context):
    aoiDir = '{}/AOI'.format(QDir.currentPath())

    # add controllers
    mainController = MainController(aoiDir)
    context.setContextProperty('PyConsole', mainController)
    context.setContextProperty('mainController', mainController)

    colorCorrectorController = ColorCorrectorController(aoiDir)
    context.setContextProperty('colorCorrectorController', colorCorrectorController)

    noiseGeneratorController = NoiseGeneratorController(aoiDir)
    context.setContextProperty('noiseGeneratorController', noiseGeneratorController)

    filtersController = FiltersController(aoiDir)
    context.setContextProperty('filtersController', filtersController)

    binarizeController = BinarizeController(aoiDir)
    context.setContextProperty('binarizeController', binarizeController)

    morphologyController = MorphologyController(aoiDir)
    context.setContextProperty('morphologyController', morphologyController)

    segmentationController = SegmentationController(aoiDir)
    context.setContextProperty('segmentationController', segmentationController)

    # add paths
    aoiDir = 'file:///{}'.format(aoiDir)
    context.setContextProperty('aoiDir', aoiDir)
    context.setContextProperty('appDir', aoiDir)

    aobDir = 'file:///{}'.format(QDir.currentPath())
    context.setContextProperty('aobDir', aobDir)

    return context
