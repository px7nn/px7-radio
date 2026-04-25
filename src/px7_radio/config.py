#FOR DEVELOPMENT
HIDE_ERR = True

API_URL = "https://de1.api.radio-browser.info/json/stations/search"

DEFAULT_PLAYER_VOLUME = 70
DEFAULT_TIMEOUT = 5
DEFAULT_RADIO_SEARCH_LIMIT = 10
DEFAULT_YT_SEARCH_LIMIT = 5

# For yt search
YDL_OPTIONS = {
    'format': 'bestaudio[ext=m4a]/bestaudio',
    'noplaylist':True,
    'no_warnings': True,
    'quiet': True,
    'skip_download': True,
    'ignoreerrors': True,
    "extract_flat": True,
    'js_runtimes': {"node": {}},
    "socket_timeout": 5,
    "retries": 0,
    "fragment_retries": 0
} 

DEFAULT_QUERY_POSTFIX = " original audio song"