# import necessary library
from constants import ACCOUNTS_PATH, LEVELED_ACCOUNTS_PATH
import os

# db request username where level < 30
def get_username():
    with open(ACCOUNTS_PATH, 'r') as f:
        first_line = f.readline().strip()
        username = first_line.split(':')[0]
    return username

# db request password where username == username
def get_password():
    with open(ACCOUNTS_PATH, 'r') as f:
        first_line = f.readline().strip()
        password = first_line.split(':')[1]
    return password

# db set level to 30 where username == username
def set_account_as_leveled():
    with open(ACCOUNTS_PATH, 'r') as read_obj:
        lines = read_obj.readlines()
    with open(ACCOUNTS_PATH, 'w') as write_obj:
        write_obj.writelines(lines[1:])
    with open(LEVELED_ACCOUNTS_PATH, 'a') as leveled_obj:
        leveled_obj.write(lines[0])

# log output
username = get_username()
password = get_password()
print(f"Username: {username}, Password: {password}")
