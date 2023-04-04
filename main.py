from controllers.ViewController import ViewController
from fileControllers.CSVConroller.CSVController import CSVController
from core.Note import Note
from view.View import View

ViewController(View, Note, CSVController('./archive/1.csv')).run()
