class User:
    def __init__(self):
        self.email  = input("Enter your email: ")
        self.__password = input("Enter your password: ") # variiables de acceso, el doble piso o guion bajo.
        self.permissions = ('edit','create','update')
        self.username = None

        def setear_username(self):
            self.username = input("Add your username: ")
            print("User successfully changed")

class UserPro(User):
    def __init__(self):
        super().__init__()
        self.permissions += ('delete', 'download')

    def pay_suscription(self, amount):
        print(f"you have successfully paid your subscription {amount}")


class UserManager:
    def create_user(self,suscription):
        if suscription:
           user = UserPro()
        else:
           user= User()
        print(f"Your user has been created successfully, your permissions are: {user.permissions}")

UserManager().create_user(True)


