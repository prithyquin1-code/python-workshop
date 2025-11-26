class Application:

    def __init__(self,application_name,category,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.category=category
        self.company=company
        self.app_size=app_size
        self.no_of_users=no_of_users
        self.ratings=ratings

    def signup(self):
        print(f"signup done,{self.application_name}")

    def login(self):
        print(f"welcome to {self.application_name}")

    def logout(self):
        print("thank you for using")

    def info(self):
        print(f"welcome to {self.category} "
              f" belongs to {self.company},{self.app_size},{self.no_of_users},{self.ratings}")

app1=Application("Instagram", "social media","meta",42.47,1000,4.4)
app2=Application("linkdn","social media","meta",43,98,7)
app3=Application("youtube","socila media","meta",47.67,456,6)
app1.signup()
app1.login()
app1.logout()

app2.signup()
app2.login()
app2.logout()

app3.signup()
app3.login()
app3.logout()

app1.info()
app2.info()
app3.info()