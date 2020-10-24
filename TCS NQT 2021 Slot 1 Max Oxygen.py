if __name__ == "__main__":

  oxygen = [0] * 9

  for i in range(9):
    reading = int(input())

    if reading > 0 or (reading < 100):
      oxygen[i] = reading
  # now we have reading 
  # 90, 91, 92
      # Our oxygen values are ready 
      # //0, 3, 6 - 1st trainees
      # //1, 4, 7 -  2nd trainee 
      # //2, 5, 8 - 3rd trainee 
      
  t1_avg = (oxygen[0] + oxygen[3] + oxygen[6]) // 3
  t2_avg = (oxygen[1] + oxygen[4] + oxygen[7]) // 3
  t3_avg = (oxygen[2] + oxygen[5] + oxygen[8]) // 3

  maxval = max([t1_avg, t2_avg, t3_avg])

  if maxval == t1_avg:
    print("Trainee No : 1")
  if maxval == t2_avg:
    print("Trainee No : 2")
  if maxval == t3_avg:
    print("Trainee No : 3")
  
  print("Highest Oxygen Level ", maxval)


    

    

  
