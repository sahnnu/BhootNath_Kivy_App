# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Label
from kivy.app import App
import datetime
from datetime import date
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import json,requests


'''from kivy.uix.popup import Popup
from kivy.garden.MessageBox import MessageBox'''
DOMAIN = 'http://3.16.36.128/'
API_TOKEN = 'api/token/'
GAME_DATA = 'game/gamedata/'
uname = None
password = ''
access_s = ''
singleDigitNumber = 0
slot_num = 0
digit_num1 = 0
digit_num3 = 0


class FIrstLabel(Label):
    pass


class SlotButton(Button):
    pass


class Date(Button):
    pass


class SlotButtons(Button):
    pass


class AnswerInput(BoxLayout):
    pass


class LotteryNumber(Button):
    pass


class textinp(TextInput):
    pass


class ClassScreen1(Screen):
    pass


class ClassScreen2(Screen):
    pass


class loginButton(Button):
    pass


# Screen Managers and Screens

# sm = ScreenManager()
class SigninWindow(BoxLayout):
    SM = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inject(self, value, object):  # Screen Manager Object is injected
        if value == 'sm':
            global SM
            SM = object

    class PasswordtextInput(TextInput):
        def SigninFunc(self):
            global password
            password =self.text




    class SigninButton(Button):
        def gotoscreen2(self, *args):
            global uname, password
            uname = "admin"
            headers = {
                'Content-type': 'application/json'
            }

            data = '{"username": "admin", "password": "' + password + '"}'
            response = requests.post(DOMAIN + API_TOKEN, headers=headers, data=data)
            password = ''
            global SM, access_s
            if response.status_code == 200:
                SM.current = 's2'

                access_json = response.json()
                access_s = access_json["access"]


class BhootnathApp(App):
    def Displaysum(self, *args):
        try:
            if len(self.inputField.text) <= 3:

                inputNumber = int(self.inputField.text)
                global digit_num3, digit_num1
                digit_num3 = inputNumber
                if inputNumber == 000:
                    self.lotteryResult.text = "0"
                else:
                    rev = 0
                    while inputNumber > 0:
                        dig = inputNumber % 10
                        rev = rev + dig
                        inputNumber = inputNumber // 10
                        singleNumber = rev % 10
                        digit_num1 = singleNumber
                        self.lotteryResult.text = str(singleNumber)
            else:
                self.lotteryResult.text = "Enter three digit Integer"
        except:
            self.lotteryResult.text = "Provide Integer Input"

    def CurrentSlot(self, *args):
        currenttime = datetime.datetime.now().hour
        #currenttime = 13
        currentday =  datetime.datetime.now().strftime("%A")
        #currentday = 'Sunday'

        slotdict={}
        slotlist=[]
        opentime =0
        closetime =0
        slotover =0

        if currentday == 'Sunday':
            slotdict = {0: 'slot1', 1: 'slot2', 2: 'slot3', 3: 'slot4', 4: 'slot-over'}
            slotlist = [11,12,14,16]
            opentime = 7
            closetime =16
            slotover =4

        else:
             slotdict = {0: 'slot1', 1: 'slot2', 2: 'slot3', 3: 'slot4', 4: 'slot5', 5: 'slot6', 6: 'slot7', 7: 'slot8',
                    8: 'Slot-over'}

             slotlist = [9,11, 13, 15, 16, 18, 19, 20, 23]
             opentime = 7
             closetime = 23
             slotover = 8



        lowerbound = 7
        upperbound = 11
        i =0
        #currenttime = 1 Edit this for testing in different hours of time
        print(currenttime)
        while i < len(slotlist):

            if lowerbound <= currenttime <= upperbound:
                self.mainbutton.text = slotdict[i]
                global slot_num
                slot_num = i
                print(slot_num)
                break
            elif closetime < currenttime or currenttime < opentime:
                self.mainbutton.text = slotdict[slotover]
                break

            #if i < len(slotlist): #To avoid out of range
            print(i)
            lowerbound = slotlist[i]  # 11
            upperbound = slotlist[i + 1]  # 12
            i += 1

    def build(self):
        self.rlayout = RelativeLayout()
        self.sm = ScreenManager()
        self.screen1 = ClassScreen1(name="s1")
        self.screen2 = ClassScreen2(name="s2")
        self.sm.add_widget(self.screen1)
        self.sm.add_widget(self.screen2)
        self.sm.current = 's1'
        self.rlayout = RelativeLayout()
        SWindow = SigninWindow()
        SWindow.inject('sm', self.sm)
        self.rlayout.add_widget(SWindow)
        self.screen1.add_widget(self.rlayout)
        layout = FloatLayout(size=(300, 300))
        firstlabel = FIrstLabel()
        dropdown2 = DropDown()
        datebutton = Date()
        self.inputField = textinp()
        print(self.inputField.text)
        submitButton = AnswerInput()
        self.lotteryResult = LotteryNumber()
        self.lotteryResult.on_press = self.Displaysum
        self.mainbutton = SlotButton()
        self.mainbutton.on_press = self.CurrentSlot
        datebutton.text = 'Date:' + date.today().strftime("%d-%b-%Y")
        self.screen2.add_widget(layout)
        layout.add_widget(self.mainbutton)
        layout.add_widget(firstlabel)
        layout.add_widget(datebutton)
        layout.add_widget(self.inputField)
        layout.add_widget(submitButton)
        layout.add_widget(self.lotteryResult)  # runTouchApp(self.sm)
        return self.sm

    class Submit(Button):
        def last_submit(self, *args):
            global access_s, SM

            header_access = "Bearer " + access_s

            headers = {
                'Content-Type': 'application/json',
                'Authorization': header_access
            }
            global digit_num3, digit_num1, slot_num
            submitdict = {
                "digit3": digit_num3,
                "digit1": digit_num1,
                "slot": slot_num+1,
                "rider_id": 2
            }
            data_str = json.dumps(submitdict)

            response = requests.post(DOMAIN + GAME_DATA, headers=headers,data=data_str)

            if response.status_code == 201:
                SM.current = 's1'
                print(response.json())
            else:
                print(response.json())
                pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    BApp = BhootnathApp()
    BApp.run()
