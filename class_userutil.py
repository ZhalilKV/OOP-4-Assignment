import random
import string
import re
from datetime import datetime


class UserUtil:
    @staticmethod
    def generate_user_id():
        """Generates a unique 9-digit user ID with the first two digits from the current year."""
        year_prefix = datetime.today().year % 100  # Get last two digits of the year
        random_digits = ''.join(random.choices(string.digits, k=7))  # Generate 7 random digits
        return int(f"{year_prefix}{random_digits}")

    @staticmethod
    def generate_password():
        """Generates a strong password with at least 1 uppercase, 1 lowercase, 1 digit, and 1 special character."""
        length = 8
        upper = random.choice(string.ascii_uppercase)
        lower = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")

        remaining = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?", k=length - 4))
        password = ''.join(random.sample(upper + lower + digit + special + remaining, length))

        return password

    @staticmethod
    def is_strong_password(password):
        """Checks if a given password is at least 8 characters long and includes uppercase, lowercase, numbers, and special characters."""
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password):
            return False
        return True

    @staticmethod
    def generate_email(name, surname, domain):
        """Generates an email address in the format name.surname@domain.com."""
        return f"{name.lower()}.{surname.lower()}@{domain.lower()}"

    @staticmethod
    def validate_email(email):
        """Validates email format (must be in 'name.surname@domain.com' format)."""
        pattern = r"^[a-zA-Z]+[.][a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$"
        return bool(re.match(pattern, email))


# Example Usage:
print("Generated User ID:", UserUtil.generate_user_id())
print("Generated Password:", UserUtil.generate_password())
print("Password Strength Check:", UserUtil.is_strong_password("Abc@1234"))  # Should return True
print("Generated Email:", UserUtil.generate_email("John", "Doe", "example.com"))
print("Email Validation:", UserUtil.validate_email("john.doe@example.com"))  # Should return True