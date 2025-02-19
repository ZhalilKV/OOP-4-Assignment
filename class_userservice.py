from datetime import datetime


class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d")

    def get_details(self):
        return f"User ID: {self.user_id}\nName: {self.name} {self.surname}\nEmail: {self.email}\nBirthday: {self.birthday.strftime('%Y-%m-%d')}"

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age


class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):

        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):

        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):

        if user_id in cls.users:
            del cls.users[user_id]
            return True
        return False

    @classmethod
    def update_user(cls, user_id, **user_update):

        user = cls.find_user(user_id)
        if user:
            for key, value in user_update.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            return True
        return False

    @classmethod
    def get_number(cls):
        return len(cls.users)


# Example usage:
user1 = User(101010, "Zhalil", "KAchkynov", "zhalilkv@gmail.com", "200202", "2002-07-09")
user2 = User(202020, "Ayana", "Zalkarova", "ayana200309@email.com", "200303", "2003-08-20")

# Adding users
UserService.add_user(user1)
UserService.add_user(user2)

# Finding a user
found_user = UserService.find_user(101010)
if found_user:
    print(found_user.get_details())

# Updating user information
UserService.update_user(101010, name="Zhalil Updated", email="newemail@example.com")

# Getting number of users
print("Total Users:", UserService.get_number())

# Deleting a user
UserService.delete_user(202020)
print("Total Users after deletion:", UserService.get_number())