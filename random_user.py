from users import Users
from datetime import datetime
import random
import string

countries = ["USA", "UK", "Canada", "Australia", "Germany", "France", "Japan", "China", "India",
             "Brazil", "Mexico", "Italy", "Spain", "South Korea", "Russia", "Netherlands", "Turkey", "Indonesia", "Saudi Arabia", "UAE", "Afghanistan"]


countries = ["Indonesia", "Singapore", "Taiwan", "Palestine"]
def generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_data():
    name = generate_random_string()
    username = generate_random_string()
    email = generate_random_string() + "@example.com"
    password = generate_random_string()
    bio = generate_random_string()
    createdAt = datetime.now()
    country = random.choice(countries)  
    age = random.randint(10, 75) 
    return name, username, email, password, bio, createdAt, country, age

def main():
    name, username, email, password, bio, createdAt, country, age = generate_random_data()
    Users.add_single_user(name, username, email, password, bio, createdAt, country, age)

if __name__ == "__main__":
    for _ in range(6000):
        main()
