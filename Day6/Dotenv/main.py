'''

`dotenv` in Python is used to manage environment variables,
providing a way to store configuration details and sensitive information outside of your code.
This separation enhances security, flexibility, and compatibility across different environments.
By using a `.env` file, you can easily configure your application without modifying the source code,
making it a practical tool for deployment, especially in containerized environments like Docker.

To Install : pip install python-dotenv

'''


import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()  # It loads the env file

# load_dotenv(override = True) # It allows to override the secret keys

# We can access individual keys from env with os.getenv("secret variable name")

print(f'Secret key : {os.getenv("MY_SECRET_KEY")}')
print(f'Host and Port : {os.getenv("COMBINED")}')
print(f'MAIL : {os.getenv("MAIL")}')

# Fetching all env values in the form of dictionary

config = dotenv_values("/home/veda/PycharmProjects/pythonLearninga/Day6/Dotenv/.env")
print(f'\nType of config : {type(config)}')

print(f'\nConfiguration keys : {config.keys()}')
print(f'\nConfiguration values : {config.values()}')
print(f'\nSecret key : {config["MY_SECRET_KEY"]}')

config = {
    **dotenv_values("/home/veda/PycharmProjects/pythonLearninga/Day6/Dotenv/.env.secret"),
    **dotenv_values("/home/veda/PycharmProjects/pythonLearninga/Day6/Dotenv/.env.shared"),
    # **os.environ
    }

print(f'\n {config}')