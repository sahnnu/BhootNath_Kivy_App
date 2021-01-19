# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Label
from kivy.app import App
import datetime,time
from datetime import date
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import json,requests


from kivy.uix.popup import Popup

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
            else:
                self.text ='Login Failed !!!'



class BhootnathApp(App):
    def Displaysum(self, *args):
        try:

            List_input = [128, 290, 100, 579, 335, 137, 380, 678, 344, 146, 470, 119, 399, 236, 489, 155, 588, 245, 560,
                          777, 227, 129, 246, 200, 589, 336, 138, 345, 679, 499, 147, 390, 110, 666, 136, 480, 228, 688,
                          237, 570, 444, 255, 120, 247, 300, 670, 355, 139, 256, 689, 445, 148, 346, 166, 599, 157, 490,
                          229, 779, 238, 580, 111, 337, 130, 248, 400, 680, 338, 149, 257, 789, 446, 158, 347, 112, 455,
                          167, 356, 220, 699, 239, 590, 888, 266, 140, 258, 500, 690, 339, 159, \
                          267, 780, 366, 168, 348, 113, 447, 230, 357, 122, 799, 249, 456, 555, 177, 123, 259, 600, 457,
                          448, 150, 268, 790, \
                          466, 169, 349, 114, 556, 178, 358, 277, 880, 240, 367, 222, 330, 124, 278, 700, 467, 223, 160,
                          340, 890, 377, 179, \
                          359, 115, 449, 250, 368, 133, 557, 269, 458, 999, 188, 125, 279, 800, 468, 288, 134, 350, 567,
                          440, 170, 369, 116, \
                          477, 189, 378, 224, 558, 260, 459, 666, 233, 126, 289, 900, 478, 225, 135, 360, 568, 388, 180,
                          379, 117, 559, 270, 450, 144, 577, 234, 469, 333, 199, 127, 235, 550, 569, \
                          299, 136, 370, 578, 334, 145, 389, 118, 488, 190, 460, 226, 668, 280, 479, 000, 244, 669, 778,
                          788, 770, \
                          889, 899, 566, 990, 667, 677]

            inputNumber = int(str(self.inputField.text))


            flag = False
            for i in List_input:

                if inputNumber == i:
                    flag = True
                    break


            global digit_num3, digit_num1
            digit_num3 = inputNumber
            rev = 0
            if flag :
                if inputNumber == 0:
                    self.lotteryResult.text = str(inputNumber)
                    digit_num1 = 0
                else:
                    while inputNumber > 0:

                        dig = inputNumber % 10
                        rev = rev + dig
                        inputNumber = inputNumber // 10
                        singleNumber = rev % 10
                        print(singleNumber,inputNumber)
                        digit_num1 = singleNumber
                        self.lotteryResult.text = str(singleNumber)

            else:

                self.lotteryResult.text = "Please enter a valid lottery number"


        except:
            self.lotteryResult.text = "Please enter a valid number"

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

            '''1st GAME ? 09:40 AM
                2nd GAME ? 11:55 AM
                3rd GAME ? 01:20 PM
                4th GAME ? 02:55 PM
                5th GAME ? 04:20 PM
                6th GAME ? 05:55 PM
                7  th GAME ? 07:20 PM
                8th GAME ? 08:55 PM'''

        else:
             slotdict = {0: 'slot1', 1: 'slot2', 2: 'slot3', 3: 'slot4', 4: 'slot5', 5: 'slot6', 6: 'slot7', 7: 'slot8',
                    8: 'Slot-over'}

             slotlist = [11, 12, 13, 15, 16.5, 18.5, 19.5,22,23]
             opentime = 7
             closetime = 23
             slotover = 8



        lowerbound = 7
        upperbound = 11
        i =0
       # currenttime = 21# Edit this for testing in different hours of time

        while i < len(slotlist):

            if lowerbound <= currenttime <= upperbound:
                self.mainbutton.text = slotdict[i]
                global slot_num
                slot_num = i

                break
            elif  currenttime >closetime  or currenttime < opentime:
                self.mainbutton.text = slotdict[slotover]
                slot_num = 8
                break

            #if i < len(slotlist): #To avoid out of range

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
            global access_s, SM,digit_num3, digit_num1, slot_num
            print(slot_num)
            if  slot_num > 7:
                self.text='Time Over !!! to Show Result '

                #exit()

            else:

                header_access = "Bearer " + access_s

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': header_access
                }

                submitdict = {
                    "digit3": digit_num3,
                    "digit1": digit_num1,
                    "slot": slot_num+1,
                    "rider_id": 2
                }
                data_str = json.dumps(submitdict)

                response = requests.post(DOMAIN + GAME_DATA, headers=headers,data=data_str)

                if response.status_code == 201:
                    self.text = 'YaaaY!!! Result Published...Check the Portal'
                    print(response.json())


                    SM.current = 's1'
                else:
                    print(response.json())
                    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    BApp = BhootnathApp()
    BApp.run()
