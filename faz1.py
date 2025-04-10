class DivarFaz1:

    users = []
    titles = []
    lst_user = {}

    def __init__(self, user):
        self.user = user

    def register(self):

        if self.user in DivarFaz1.users:
            print(f"this user : {self.user} already is exsist ")
        else:
            DivarFaz1.users.append(self.user)
            print(f"\033[92mregistered successfully  with\033[0m {self.user}")

    def add_advertise(self, title):

        if self.user not in DivarFaz1.users:
            print("first reigesr user name so post advertise")
        else:
            if title in DivarFaz1.titles:

                print("\033[92mthis is advertis is alredy poseted\033[0m")
            else:
                DivarFaz1.titles.append(title)
                DivarFaz1.lst_user[title] = self.user

                print(f"This {title}posted successful")

    def rem_advertise(self, title):
        if self.user not in DivarFaz1.users:
            print(f"{self.user}not in rigester")
        else:
            if title not in DivarFaz1.titles:
                print(f"{title} not exsist")
            elif title in DivarFaz1.titles and DivarFaz1.lst_user[title] == self.user:
                print(f"Removed {title} by {self.user}")
                del DivarFaz1.lst_user[title]
                DivarFaz1.titles.remove(title)
            else:
                print(
                    f"User '{self.user}' is not the owner of '{title}' and cannot remove it."
                )

    @classmethod
    def list_my_advertises(cls, username):
        if username not in cls.users:
            print("invalid user ")
            return
        user_ads = [
            title for title in cls.titles if cls.lst_user.get(title) == username
        ]
        if user_ads:
            print(f'\033[92m{" \/\/\/".join(user_ads)}\033[0m')
        else:
            print("no advertisement found ")

    # FAZ 2 =========================================================================
    @classmethod
    def add_favorit(cls, username, title):
        if username not in cls.users:
            print("you dont rigeste")
        else:
            if title not in cls.titles:
                print("title not already")


u1 = DivarFaz1("reza")
u2 = DivarFaz1("ali")
u3 = DivarFaz1("reza")
# ===============================================================
u1.register()
u1.add_advertise("mobile")
# ===============================================================
print("=" * 40)
u2.register()
u2.add_advertise("book")
u2.add_advertise("software")
u2.add_advertise("comod")
# ===============================================================
print("=" * 40)
u3.register()
print("=" * 40)
u2.rem_advertise("mobile")
u2.rem_advertise("book")
# ================================================================
DivarFaz1.list_my_advertises("ali")
