class User:
    def __init__(self, name, email):
        self.name = name.title()
        self.email = email.lower()

    def __str__(self):
        return "%s <%s>" % (self.name, self.email)

    def __eq__(self, other):
        return self.email.lower() == other.email.lower()

    def is_active(self):
        return True

    def is_superuser(self):
        return False


class RegularUser(User):
    pass


class SuperUser(User):
    def is_superuser(self):
        return True


user_1 = RegularUser("нина", "nina@gmail.com")
user_2 = SuperUser("максим", "maxim.cudaew@gmail.com")
users = [user_1, user_2]

for user in users:
    print(user)
