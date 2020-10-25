if __name__ == "__main__":

  parent = input()
  isParent = input()

  if isParent == "Y":
    child = input()
    children = child.split(",")

    total_members = len(children)+ 1;

    print("TOTAL MEMBERS:", total_members)
    print("COMMISION DETAILS")
    print(parent, ":", 500 , "INR")
    for c in children:
      print(c, ":", 250, "INR")

  else:
    print("TOTAL MEMBERS:1")
    print("COMMISION DETAILS")
    print(parent, ":", 250 , "INR")
    
