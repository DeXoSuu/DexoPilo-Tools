from Config.Util import *
from Config.Config import *
try:
    import requests
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Joiner")

try:
    def joiner(token, invite):
        invite_code = invite.split("/")[-1]

        try:
            response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
            if response.status_code == 200:
                server_name = response.json().get('guild', {}).get('name')
            else:
                server_name = invite
        except:
            server_name = invite

        try:
            response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers={'Authorization': token})
                
            if response.status_code == 200:
                print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Status: {white}Joined{green} Server: {white}{server_name}{green}")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error {response.status_code}{red} Server: {white}{server_name}{red}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error{red} Server: {white}{server_name}{red}")

    Slow(discord_banner)
    token = Choice1TokenDiscord()
    invite = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Server Invitation -> {reset}")
    joiner(token, invite)
    Continue()
    Reset()
except Exception as e:
    Error(e)
