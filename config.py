# adapt the following variables to your needs
talkgroups = [3179400, 3187028] # Talkgroups to monitor, seperated by commas
callsigns = ['WA1ABC','W1AW'] # Callsigns to monitor, seperated by commas
noisy_calls = ["L1DHAM", "N0CALL", "N0C4LL"] # Noisy calls signs that will be ignored
min_duration = 0 # Min. duration of a QSO to qualify for a push notification
min_silence = 300 # Min. time in seconds after the last QSO before a new push notification will be send
verbose = True # Enable extra messages (console only)
emit_sound = True
open_webbrowser = True
url_to_open = "https://brandmeister.network/?page=lh&jsonquery=%7B%22condition%22%3A%22OR%22%2C%22rules%22%3A%5B%7B%22id%22%3A%22DestinationID%22%2C%22field%22%3A%22DestinationID%22%2C%22type%22%3A%22integer%22%2C%22input%22%3A%22text%22%2C%22operator%22%3A%22equal%22%2C%22value%22%3A%223179400%22%7D%2C%7B%22id%22%3A%22DestinationID%22%2C%22field%22%3A%22DestinationID%22%2C%22type%22%3A%22integer%22%2C%22input%22%3A%22text%22%2C%22operator%22%3A%22equal%22%2C%22value%22%3A%223187028%22%7D%5D%7D" # PUT YOUR URL IN HERE!!!!!

# Pushover configuration
pushover = False # Enable or disable notifications via Pushover
pushover_token = "1234567890" # Your Pushover API token
pushover_user = "abcdefghijklm" # Your Pushover user key

# Telegram configuration
telegram = False # Enable or disable notifications via Telegram
telegram_api_id = "1234567"
telegram_api_hash = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
telegram_username = "foo_bot"
phone = "+491234567890"

# DAPNet configuration
dapnet = False # Enable or disable notifications via dapnet
dapnet_user = "mycall"
dapnet_pass = "xxxxxxxxxxxxxxxxxxxx"
dapnet_url = 'http://www.hampager.de:8080/calls'
dapnet_callsigns = ["MYCALL"]
dapnet_txgroup = "dl-all"

# Discord Configuration
discord = False
discord_wh_url = 'DISCORD_WEBHOOK_HERE'
