class DivarFaz1:

    users = []

    def __init__(self, user):
        self.user = user

    def register(self):

        if self.user in DivarFaz1.users:
            print(f"this user : {self.user} alredy is exsist ")
        else:
            DivarFaz1.users.append(self.user)
            print(f"register  successfull whit {self.user}")


u1 = DivarFaz1("reza")
u2 = DivarFaz1("ali")
u3 = DivarFaz1("reza")
u1.register()
u2.register()
u3.register()
