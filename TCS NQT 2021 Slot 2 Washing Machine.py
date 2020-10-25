if __name__ == "__main__":

  weight = int(input())

  if weight < 0 :
    print("INVALID INPUT")
  elif weight > 7000:
    print("OVERLOADED!!!")
  else:
    if weight < 2001:
      print("Time Estimated : 25 minutes")
    elif weight <4001:
      print("Time Estimated : 35 minutes")
    else :
      print("Time Estimated : 45 minutes")
