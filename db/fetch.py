import pymongo
from pymongo import InsertOne, DeleteOne, ReplaceOne, DeleteMany
from pprint import pprint
from espnff import League
from collections import defaultdict


# db definition
db = pymongo.MongoClient().foosball
# db = pymongo.MongoClient().bulk_example

print("Connecting to DB: ",'\'',db.name,'\'')

# league info for api query
league_id = 262704
year = 2017
my_team_name = "Offensive Fowlers"

league = League(league_id, year)

teams = league.teams

my_team = next(team for team in teams if team.team_name == my_team_name)

week_matchups = league.scoreboard(week=2)

for matchup in week_matchups:
  if matchup.home_team.team_name == my_team_name:
    my_match_this_week = matchup
    my_team_this_week = my_match_this_week.home_team
  elif matchup.home_team.team_name == my_team_name:
    my_match_this_week = matchup
    my_team_this_week = my_match_this_week.away_team

print(my_match_this_week)
pprint(vars(my_match_this_week))

print(my_team_this_week)
pprint(vars(my_team_this_week))


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
