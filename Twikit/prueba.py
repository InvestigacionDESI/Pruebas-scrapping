import asyncio
from twikit import Client

USERNAME = 'Investigac128'
EMAIL = 'investigacionDESI1234'
PASSWORD = 'investigaciondesi@gmail.com'

# Initialize client
client = Client(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

asyncio.run(main())