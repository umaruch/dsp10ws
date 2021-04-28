from app.extensions import mpd_client


# Словарь соотношений команда-функция
routes = {
    "SET_PAUSE": mpd_client.pause,
    "SET_PLAY": mpd_client.play,
    "SET_NEXT": mpd_client.next,
    "SET_PREV": mpd_client.prev,
    "SET_REPEAT": mpd_client.repeat,
    "SET_RANDOM": mpd_client.random,
    "SET_VOLUME": None,
    "SET_TIME": None,
    "GET_STATUS": None,
    "GET_PLAYLISTS": None,
    "GET_PLAYLIST": None,
    "DELETE_PLAYLIST": None,
    "RENAME_PLAYLIST": None,
    "SWAP": None,
    "DELETE": None,
    "ADD": None,
    "BROWSE": None,
    "CHANGE_PLAYLIST": None,
    "CHANGE_SONG": None,
    "SAVE_PLAYLIST": None,
    "UPDATE": None,
    "PLAY_BROWSE": None,
    "GET_DEVICE": None,
    "REBOOT": None,
    "RENAME_DEVICE": None,
    "CHANGE_PROFILES": None,
    "GET_NETWORK": None,
    "CHANGE_NETWORK": None
}
