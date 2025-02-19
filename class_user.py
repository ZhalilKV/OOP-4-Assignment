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


# Example usage:
user = User(101010, "Zhalil", "Kachkynov", "zhalilkv@gmail.com", "200202", "2002-07-09")
print(user.get_details())
print("Age:", user.get_age())


def get_age(self):
    today = datetime.today()
    age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
    return age