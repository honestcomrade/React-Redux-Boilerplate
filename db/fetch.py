from espnff import League

league_id = 262704
year = 2017

league = League(league_id, year)

teams = league.teams

my_team = next(team for team in teams if team.team_name == 'Offensive Fowlers')

print("")
print("  ", my_team.team_name)
print("  -------------------")

i = 1

for score in my_team.scores:
  if(i < 10):
    print("    Week ", i, " : ", score)
  else:
    print("    Week ", i, ": ", score)
  i+=1
print("  -------------------")

totalPts = my_team.points_for

print("Total Points:  ", totalPts)
print("  -------------------")
print("")

print("      Total Mov  ")
print("  -------------------")

i = 1


for mov in my_team.mov:
  if(i < 10):
    print("    Week ", i, " : ", mov)
  else:
    print("    Week ", i, ": ", mov)
  i+=1
print("  -------------------")
print("")
