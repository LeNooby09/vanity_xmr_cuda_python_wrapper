base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def sanitize_input():
  raw_input = input("Enter a pattern: ")
  if len(raw_input) > 95:
      print("Pattern is too long. Please enter a pattern of 95 characters or less.")
      return False
  elif len(raw_input) < 1:
      print("Pattern is too short. Please enter a pattern of 1 character or more.")
      return False
  else:
      for char in raw_input:
          if char not in base58:
              print("Pattern contains invalid characters. Please enter a pattern containing only base58 characters.")
              return False
          else :
              return raw_input

def pattern_match(pattern = sanitize_input()):

  print("Avaliable patterns:\n'?': any character\n'...xxx': any character until end of string, then match 'xxx' at the end\n")
