from pywinauto import Desktop, Application, ElementNotFoundError
from pywinauto.findwindows import ElementNotFoundError, enum_windows
from robot.api.deco import keyword
from robot.api import logger
from subprocess import call
# python -m robotide.__init__
# dlg.print_control_identifiers()
@keyword('Start Calc')
def startCalcDialog() -> Application():
    "This method just returns a Calculator dialog"
    app = Application(backend='uia').start('calc.exe')
    # needed since the application spaws additional processes
    # windows = Desktop(backend='uia').windows()
    # for w in windows:
    #     print(w.window_text())
    return Desktop(backend='uia').Calculator 

@keyword("Push Num Button")
def num_button_pusher(dialog: Desktop(), number:int):
    # "this methods job is to decode a number if it's more than one"
    # or to just push the regular num button
    if number>9:
        number = str(number)
        print(type(number))
        for num in number:
            try:
                btn = 'num{}Button'.format(str(num))
                dialog.child_window(auto_id=btn).invoke()

            except ElementNotFoundError as error:
                print("That element isn't found")
    else:
        try:
            btn = 'num{}Button'.format(str(number))
            dialog.child_window(auto_id=btn).invoke()

        except ElementNotFoundError as error:
            print("That element isn't found")

@keyword("Kill Calcs")
def kill_all_calcs():
    logger.info("Killing all Calculators")
    call(['TASKKILL', '/F', '/IM', "calculator.exe", "/T"])
# Calcdlg = startCalcDialog()
# num_button_pusher(Calcdlg, 5)
# num_button_pusher(Calcdlg, 100)

startCalcDialog()