class mobile:

    def __init__(self):
        pass

    def callings(self):
        print('Invoking Caliing function')

    def sms(self):
        print("invoking  sms method")

    def games(self):
        print("invoking games")


class realme_c10(mobile):

    def cam(self):
        print("Invoking cam method")

    def music(self):
        print("Invoking music method")

    def video_call(self):
        print("Invoking video call")

realme=realme_c10()
realme.music()
realme.video_call()
realme.cam()

