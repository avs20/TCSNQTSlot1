
if __name__ == "__main__":

  teams = []

  team = input()

  while team != "q":
    teams.append(team)
    team = input()

  if len(teams) < 3 or len(teams) > 12:
    print("INVALID INPUT")
  else:

    count = 0 
    pairing = []
    for i in range(0, len(teams)):
      for j in range(i+1, len(teams)):
        pair = teams[i] + "-" + teams[j]
        pairing.append(pair)
        count += 1

    print("TOTAL MATCHES : ", count)
    for pair in pairing:
      print(pair.upper())



