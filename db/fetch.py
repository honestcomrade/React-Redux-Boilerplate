import pymongo
from pprint import pprint
from espnff import League
from collections import defaultdict

try:
    import simplejson as json
except:
    import json

# GLOBALS
# db stuff
db = pymongo.MongoClient().foosball
print("Connecting to DB: ",'\'',db.name,'\'')

# league info for api query
league_id = 262704
year = 2017
my_team_id = 8
this_week = 2

# END GLOBALS

# FUNCTIONS
def getMatch(week_matchups, team_id):
  for matchup in week_matchups:
    if matchup.home_team.team_id == team_id:
      match = matchup
      return match
    elif matchup.away_team.team_id == team_id:
      match = matchup
      return match
    else:
      match = "No Match Found"
  return match

# END FUNCTIONS

# SERIALIZABLE CLASSES
class TeamObj:
  def __init__(self, name, scores, wins, losses):
    self.name = name
    self.all_scores = scores
    self.wins = wins
    self.losses = losses

  def gettotal(self, scores):
    self.totalScore = 0
    for score in scores:
      self.totalScore += score
    return self.totalScore

# END SERIALIZABLE CLASSES

# get my team's overall data and write to disk
league = League(league_id, year)
teams = league.teams
my_team = next(team for team in teams if team.team_id == my_team_id)
team_obj = TeamObj(my_team.team_name, my_team.scores, my_team.wins, my_team.losses)
team_obj.gettotal(team_obj.all_scores)
with open('team.json', 'w') as f:
  json.dump(team_obj.__dict__, f)


# get my week's data and write to disk
week = league.scoreboard(week=this_week)
my_match = getMatch(week, my_team_id)
with open('week.json', 'w') as f:
  json.dump(my_match.data, f)
