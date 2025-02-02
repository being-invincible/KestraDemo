import os
from dotenv import load_dotenv, dotenv_values 
from kestra import Kestra
load_dotenv() 

# accessing and printing value
print(os.getenv("PLACES_API"))