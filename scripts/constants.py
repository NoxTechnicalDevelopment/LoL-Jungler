import os

# LANE
SELECTED_LANE = 'mid'

# PATHS
LEAGUE_DIR = 'C:/Riot Games/League of Legends'
LEAGUE_PATH = LEAGUE_DIR + '/LeagueClient'
LOCKFILE_PATH = LEAGUE_DIR + "/lockfile"
LEAGUE_GAME_CONFIG_PATH = LEAGUE_DIR + '/Config/game.cfg'
LOCAL_GAME_CONFIG_PATH = os.path.dirname(os.getcwd()) + '/resources/game.cfg'
LEVELED_ACCOUNTS_PATH = os.path.dirname(os.getcwd()) + '/resources/leveled.acc'
ACCOUNTS_PATH = os.path.dirname(os.getcwd()) + '/resources/accounts.acc'

# LCU API INFO
LCU_HOST = '127.0.0.1'
LCU_USERNAME = 'riot'
DEFAULT_PROTOCOL = 'https'

# WINDOW NAMES
RIOT_CLIENT_WINNAME = "Riot Client Main"
LEAGUE_CLIENT_WINNAME = "League of Legends"
LEAGUE_GAME_CLIENT_WINNAME = "League of Legends (TM) Client"

# PROCESS NAMES
PROCESS_NAMES = ["LeagueClient.exe", "League of Legends.exe"]

# COMMANDS
KILL_LEAGUE_CLIENT = 'TASKKILL /F /IM LeagueClient.exe'
KILL_LEAGUE = 'TASKKILL /F /IM "League of Legends.exe"'
KILL_RIOT_CLIENT = 'TASKKILL /F /IM RiotClientUx.exe'

# GAME DATA
ACCOUNT_MAX_LEVEL = 30
BEGINNER_BOTS_GAME_LOBBY_ID = 840
INTERMEDIATE_BOTS_GAME_LOBBY_ID = 850
GAME_LOBBY_ID = BEGINNER_BOTS_GAME_LOBBY_ID
EARLY_GAME_END_TIME = 600
STARTER_ITEMS_TO_BUY = 4
ITEMS_TO_BUY = 6
CHAMPS = [21, 18, 22, 67] # normal
JUNGCHAMPS = [122, 86, 14, 875] # jungle
ASK_4_MID_DIALOG = [
    "mid :)",
    "mid",
    "mid por flavor",
    "bienvenidos, mid"
]

ASK_4_JUNG_DIALOG = [
    "jung :)",
    "jung",
    "jung por flavor",
    "bienvenidos, jung"
]

# GAME BUTTON RATIOS
GAME_ALL_ITEMS_RATIO = (0.4019, 0.2349)
GAME_BUY_STARTER_ITEM_RATIO = (0.2490, 0.3903)  # Based on the default shop open position on the all items tab
GAME_BUY_EPIC_ITEM_RATIO = (0.2519, 0.5923)  # Based on the default shop open position on the all items tab
GAME_BUY_LEGENDARY_ITEM_RATIO = (0.2875, 0.7571)
GAME_BUY_ITEM_RATIO_INCREASE = (.0366, 0)
GAME_BUY_PURCHASE_RATIO = (0.7644, 0.7877)  # Based on the default shop open position
GAME_MINI_MAP_UNDER_TURRET = (0.8760, 0.8846)
GAME_MINI_MAP_CENTER_MID = (0.9042, 0.8710)
GAME_MINI_MAP_ENEMY_NEXUS = (0.9628, 0.7852)
GAME_ULT_RATIO = (0.7298, 0.2689)
GAME_AFK_OK_RATIO = (0.4981, 0.4647)
GAME_CENTER_OF_SCREEN = (0.5, 0.5)
GAME_JUNGLE_CAMP_GROMP = (0.8348, 0.8521)
GAME_JUNGLE_CAMP_BLUEBUFF = (0.8603, 0.8632)
GAME_JUNGLE_CAMP_MURKWOLF = (0.8543, 0.8827)
GAME_JUNGLE_CAMP_RAPTORS = (0.9124, 0.9126)
GAME_JUNGLE_CAMP_REDBUFF = (0.9012, 0.9207)
GAME_JUNGLE_CAMP_KRUGS = (0.9100, 0.9389)


# CLIENT BUTTON RATIOS - ideally these would be unnecessary but idk the endpoints to clear rewards post game
POST_GAME_OK_RATIO = (0.4996, 0.9397)
POST_GAME_SELECT_CHAMP_RATIO = (0.4977, 0.5333)
POPUP_SEND_EMAIL_X_RATIO = (0.6960, 0.1238)
# CLIENT_RECONNECT_BUTTON = (0.4116, 0.4985)

# RANDOM
MAX_ERRORS = 5