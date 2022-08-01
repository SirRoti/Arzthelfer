import nextcord
from nextcord.ext import commands

import json

from colorama import Fore
import datetime

class presence(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            with open("", "r") as data_file:
                data = json.load(data_file)

            presence_text = data["texts"]["presence"]

            await self.client.change_presence(activity=nextcord.Game(presence_text))
        except Exception as error:
            print(f"{Fore.RESET}[{datetime.datetime.now().strftime('%H:%M:%S')}] [{Fore.RED}ERROR{Fore.RESET}] Event {Fore.CYAN}presence{Fore.RESET} konnte nicht ausgeführt werden >> {Fore.CYAN}{error}{Fore.LIGHTBLACK_EX}")
            
def setup(client):
    client.add_cog(presence(client))
