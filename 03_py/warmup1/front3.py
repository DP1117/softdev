def front3(str):
  copy = str
  if len(str) >= 3:
    copy = str[:3]
  return copy + copy + copy
