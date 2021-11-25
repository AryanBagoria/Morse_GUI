from guizero import App, Text, TextBox, PushButton
import RPi.GPIO as GPIO
import time

PIN = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

letters = {
      'A': '.-', 
      'B': '-...', 
      'C': '-.-.', 
      'D': '-..', 
      'E': '.', 
      'F': '..-.', 
      'G': '--.', 
      'H': '....', 
      'I': '..', 
      'J': '.---', 
      'K': '-.-', 
      'L': '.-..', 
      'M': '--', 
      'N': '-.', 
      'O': '---', 
      'P': '.--.', 
      'Q': '--.-', 
      'R': '.-.', 
      'S': '...', 
      'T': '-', 
      'U': '..-', 
      'V': '...-', 
      'W': '.--', 
      'X': '-..-', 
      'Y': '-.--', 
      'Z': '--..', 
      '1': '.----', 
      '2': '..---', 
      '3': '...--', 
      '4': '....-', 
      '5': '.....', 
      '6': '-....', 
      '7': '--...', 
      '8': '---..', 
      '9': '----.', 
      '0': '-----', 
      ' ': '/'
          }

def led_control(time_sleep):
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(time_sleep)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.5)

def led_blink():
    appMessage.value = inputText.value
    if len(appMessage.value) > 12:
        appMessage.value = "Cannot enter more than 12 characters"
    else:
        appMessage.value = appMessage.value 
        word = inputText.value
        word = word.upper ()
        for letter in word:
                time.sleep(2)
                morseCodeLetter = letters[letter]
                for codes in morseCodeLetter:
                    if codes ==  "_":
                        led_control(0.5)
                    elif codes == ".":
                        led_control (0.2)
                    elif codes == "/":
                        time.sleep(1)

app = App(title = "Morse Code")
appMessage = Text(app,text = "Enter text to get morse code signal" ,size = 15, color="BLACK")
inputText = TextBox(app, width=20)
ledBlink = PushButton(app, command=led_blink, text ="BLINK LED" ,width = 20)
app.display()

GPIO.cleanup()
