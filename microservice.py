import pandas as pd
import random
import time
import zmq

def get_player_info():

    randNum = random.randint(0, 90)
    df = pd.read_csv("all_players.csv")

    player = df.iloc[randNum]
    playerName = player.get("Name")
    playerClub = player.get("Club")
    playerNationality = player.get("Nation")
    playerOvrRating = player.get("Overall")

    playerInfo = {
        "name": playerName,
        "club": playerClub,
        "nationality": playerNationality,
        "rating": playerOvrRating
        }

    return str(playerInfo)


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string(get_player_info())