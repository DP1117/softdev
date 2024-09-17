def not_string(str):
  if len(str) > 2 and str[0:3] == "not":
    return str
  return "not " + str