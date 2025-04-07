class DivarFaz1:

    users = []
    titles = []

    def __init__(self, user):
        self.user = user

    def register(self):

        if self.user in DivarFaz1.users:
            print(f"this user : {self.user} alredy is exsist ")
        else:
            DivarFaz1.users.append(self.user)
            print(f"\033[92mregistered successfully  whit\033[0m {self.user}")

    def add_advertise(self, title):
        self.title = title
        if self.user not in DivarFaz1.users:
            print("first reigesr user name so post advertise")
        else:
            if title in DivarFaz1.titles:

                print("\033[92mthis is advertis is alredy poseted\033[0m")
            else:
                DivarFaz1.titles.append(title)
                print(f"This {self.title}posted successful")


u1 = DivarFaz1("reza")
u2 = DivarFaz1("ali")
u3 = DivarFaz1("reza")
u1.register()
u1.add_advertise("mobile")
print("=" * 40)
u2.register()
u2.add_advertise("software")
u2.add_advertise("software")
print("=" * 40)

u3.register()
