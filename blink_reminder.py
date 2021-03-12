import time
from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast("Timer Started","Remember to take regular breaks!",duration=10,icon_path="eye.ico")
while True:
    time.sleep(20*60)
    toast.show_toast("Blink Break","Look 20 ft away for 20 s!",duration=10,icon_path="eye.ico")
    time.sleep(20)
    toast.show_toast("Break Over", "Back to work!", duration=10, icon_path="eye.ico")

'''
timer = 20*60
while 1:
    print("minutes left:", timer/60)
    time.sleep(60)
    timer -= 1
    if timer == 0:
        toast.show_toast("Blink Break","Look 20 ft away for 20 s!",duration=10,icon_path="eye.ico")
        timer = 20
        while timer >= 0:
            print("seconds left:", timer)
            time.sleep(1)
            timer -= 1
        toast.show_toast("Break Over", "Back to work!", duration=10, icon_path="eye.ico")
        timer = 20*60
'''