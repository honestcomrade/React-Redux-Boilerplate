import pymongo
from pprint import pprint
from espnff import League
from collections import defaultdict

try:
    import simplejson as json
except:
    import json

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


# db stuff
db = pymongo.MongoClient().foosball
print("Connecting to DB: ",'\'',db.name,'\'')

# league info for api query
league_id = 262704
year = 2017
my_team_id = 8

# serializable classes
class TeamObj:
  def __init__(self, name, score):
    self.name = name
    self.score = score

class Week:
  def __init__(self, week, myTeam, oppTeam, myPlayers, oppPlayers):
    self.week = week
    self.myTeam = myTeam
    self.oppTeam = oppTeam
    self.myPlayers = myPlayers
    self.oppPlayers = oppPlayers

# need to refactor these assignments to functions once we are writing to disk
league = League(league_id, year)
teams = league.teams
my_team = next(team for team in teams if team.team_id == my_team_id)
team_obj = TeamObj(my_team.team_name, my_team.scores[0])

with open('team.json', 'w') as f:
  json.dump(team_obj.__dict__, f)

week_matchups = league.scoreboard(week=3)

match = getMatch(week_matchups,8)
pprint(vars(match))


# for matchup in week_matchups:




# print(week_matchups)
# week_obj = Week()


# pprint(vars(my_team))
# print(my_team)

# print(type(my_team))
# pprint(type(object))

# pickle_team = jsonpickle.encode(my_team)
# json_team = json.dumps(pickle_team, indent=4)

# team = json_team

# db.insert_many(my_team.__dict__)

# pprint(vars(my_team))
# pprint(team)

# pprint(my_team.__dict__)

# pprint(json_team)

# league = League
# json_league = jsonpickle.encode(league)
# json_object = jsonpickle.encode(league)

# print(type(json_league))

# pprint(json_league)

# restored = jsonpickle.decode(json_league)

# print(type(restored))


# pprint(vars(json_object))


# for matchup in week_matchups:
#   if matchup.home_team.team_name == my_team_name:
#     my_match_this_week = matchup
#     my_team_this_week = my_match_this_week.home_team
#   elif matchup.home_team.team_name == my_team_name:
#     my_match_this_week = matchup
#     my_team_this_week = my_match_this_week.away_team
#   else:
#     print("no match found")
#     my_match_this_week = "No Match Found"
#     my_team_this_week = "No Match Found"

# print(my_match_this_week)
# pprint(vars(my_match_this_week))

# print(my_team_this_week)
# pprint(vars(my_team_this_week))


#db writes
# db.my_team.insert_many(my_team)
# pprint("Teams: ",my_team)
# print(my_team)
# vars(my_team)
# print(type(my_team))
# attrs = vars(my_team)

# print ', '.join("%s: %s" item for item in attrs.items())
# teams_dict = defaultdict(teams)
# print(type(teams_dict))
# db.test.insert_one([teams])
# vars(league)

# requests = [insert_many({teams})]
# result = db.test.insert_many([teams])
# result.inserted_count
# db.test.bulk_write(DeleteMany({}))  # Remove all documents from the previous example.


# outputs
# print("")
# print("  ", my_team.team_name)
# print("  -------------------")

# week = 1

# for score in my_team.scores:
#   if(week < 10):
#     print("    Week ", week, " : ", score)
#   else:
#     print("    Week ", week, ": ", score)
#   week+=1
# print("  -------------------")

# totalPts = my_team.points_for

# print("Total Points:  ", totalPts)
# print("  -------------------")
# print("")

# print("      Total Mov  ")
# print("  -------------------")

# week = 1


# for mov in my_team.mov:
#   if(week < 10):
#     print("    Week ", week, " : ", mov)
#   else:
#     print("    Week ", week, ": ", mov)
#   week+=1
# print("  -------------------")
# print("")
