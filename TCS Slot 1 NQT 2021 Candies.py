if __name__ == "__main__":

  custOrder = int(input())


  if custOrder < 0 or custOrder > 10:
    print("Invalid Input")
    print("Number of Candies in Jar : 10")
  else:
    print("Number of candies sold : ",custOrder)
    leftCandies = 10 - custOrder

    if leftCandies <= 5:
      print("Number of Candies in Jar : 10")
    else:
      print("Number of Candies in Jar : ", leftCandies)
