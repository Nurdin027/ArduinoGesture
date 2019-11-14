from serial import Serial
import pyautogui

Arduino_Serial = Serial('com5',9600)
 
while 1:
    incoming_data = str (Arduino_Serial.readline())
    print (incoming_data)
     

    if 'next' in incoming_data:
        pyautogui.hotkey('pgdn')
        
    if 'prev' in incoming_data:
        pyautogui.hotkey('pgup')

    incoming_data = "";