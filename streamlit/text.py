import os
from dotenv import load_dotenv

load_dotenv()

portfastapi = os.getenv('PORTFastapi')
str=portfastapi+"hi"
print (str)
print(type(portfastapi))
