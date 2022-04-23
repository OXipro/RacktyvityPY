import PySimpleGUI as sg
import rack

iprack = "192.168.111.189"
sg.theme("LightBlue5")
layout = [
    [sg.Text("Racktivity app vBETA0.1")],
    [[sg.Text("1"), sg.Button(button_text="on1"), sg.Button(button_text="off1")]],
    [[sg.Text("2"), sg.Button(button_text="on2"), sg.Button(button_text="off2")]],
    [[sg.Text("3"), sg.Button(button_text="on3"), sg.Button(button_text="off3")]],
    [[sg.Text("4"), sg.Button(button_text="on4"), sg.Button(button_text="off4")]],
    [[sg.Text("5"), sg.Button(button_text="on5"), sg.Button(button_text="off5")]],
    [[sg.Text("6"), sg.Button(button_text="on6"), sg.Button(button_text="off6")]],
    [[sg.Text("7"), sg.Button(button_text="on7"), sg.Button(button_text="off7")]],
    [[sg.Text("8"), sg.Button(button_text="on8"), sg.Button(button_text="off8")]]
]

window = sg.Window("Racktivity APP", layout, size=(300, 500))
event, values = window.read()
window.read()
#prise
if event == "on1":
    rack.prise(prise=1, status=1)
if event == "off1":
    rack.prise(prise=1, status=0)
# prise
if event == "on2":
    rack.prise(prise=2, status=1)
if event == "off2":
    rack.prise(prise=2, status=0)
# prise
if event == "on3":
    rack.prise(prise=3, status=1)
if event == "off3":
    rack.prise(prise=3, status=0)
# prise
if event == "on4":
    rack.prise(prise=4, status=1)
if event == "off4":
    rack.prise(prise=4, status=0)
# prise
if event == "on5":
    rack.prise(prise=5, status=1)
if event == "off5":
    rack.prise(prise=5, status=0)
# prise
if event == "on6":
    rack.prise(prise=6, status=1)
    window.read()
if event == "off6":
    rack.prise(prise=6, status=0)
    window.read()
# prise
if event == "on7":
    rack.prise(prise=7, status=1)
if event == "off7":
    rack.prise(prise=7, status=0)
# prise
if event == "on8":
    rack.prise(prise=8, status=1)
if event == "off8":
    rack.prise(prise=8, status=0)

