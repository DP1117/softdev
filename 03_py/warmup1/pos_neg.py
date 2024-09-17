def pos_neg(a, b, negative):
  return (negative and a < 0 and b < 0) or (not negative and a < 0 and b > 0) or (not negative and b < 0 and a > 0)