class Notification:

    def get_notification(self):
        pass

class  Instagram(Notification):

    def get_notification(self):
        print("notification from instagram")

class Facebook(Notification):

    def get_notification(self):
        print("notification from facebook")

Instagram=Instagram()
Instagram.get_notification()

Facebook=Facebook()
Facebook.get_notification()



