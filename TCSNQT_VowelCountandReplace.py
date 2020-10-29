
def checkNumeric(text):
  numtext = "0123456789"

  for num in numtext:
    if num in text:
      return True

  return False

def vowelCount(text):
  vowel_dict = {}
  vowel_dict['a'] = 0
  vowel_dict['e'] = 0
  vowel_dict['i'] = 0
  vowel_dict['o'] = 0
  vowel_dict['u'] = 0

  flag = False;

  for c in text:
    if c in vowel_dict:
      vowel_dict[c] += 1
      flag = True

  return flag, vowel_dict
    



if __name__ == "__main__":
  text = input()

  # if it is blank:
  # print Invalid input 
  text = text.strip()
  
  if len(text) < 1:
    print("INVALID INPUT")
  elif checkNumeric(text):
    # if it contains any numeric value 
    # print 0 
    print("0")
  else:
    flag, vowel_dict = vowelCount(text)

    if flag:
      # now print the count of vowels
      for item in vowel_dict:
        print(item, ":", vowel_dict[item])
      # print the message without vowel
      for c in 'aeiou':
        text = text.replace(c, '')

      print(text)
    else:
        # if it contains no vowel 
        # print 0 

      print("0")

  


  

  




