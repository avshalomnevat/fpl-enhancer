# This model is released under the MIT License.
# https://opensource.org/licenses/MIT
# Copyright © 2024 Avshalom Nevat

# THINGS I KNOW BEFORE STARTING (NOT MUCH):
# This model calculates the strength of a football team based on various attributes (DON'T KNOW WHAT THEY ARE OR HOW DO I USE THEM TO GET ANY OUTPUT).
# The strength is divided into two categories: offensive and defensive, and further divided into home and away performance.
# The result is a dictionary with the following structure: team_strength = {'Offence': {'Home': 0, 'Away': 0}, 'Defence': {'Home': 0, 'Away': 0}}

# Step 1: Gather data
import soccerdata as sd
from pathlib import Path

# Here is the data that will (maybe) suit me.
wanted_data = sd.FBref(leagues=['ENG-Premier League'], seasons=['1819', '20-21', '2122', '2223'], data_dir=Path('data/ENG-Premier-League/1819_2021_2122_2223'))

print(wanted_data.read_team_match_stats().sort_values('xG', ascending=False).head(10))
