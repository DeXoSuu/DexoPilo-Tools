from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Site")

print(f"""
{white}[{red}02{white}] {red}->{white} Discord
{white}[{red}03{white}] {red}->{white} Github
""")

try:
    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Site -> {color.RESET}")
    if choice in ['2', '02']:
        site = f"https://{discord_server}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the Discord server \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()

    if choice in ['3', '03']:
        site = f"https://{github_tool}"
        webbrowser.open_new_tab(site)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Access to the site \"{color.WHITE}{site}{color.RED}\"" + color.RESET)
        Continue()
        Reset()
except Exception as e:
    Error(e)
