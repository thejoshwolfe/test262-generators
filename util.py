
def js_repr(string):
  string = string.replace("\\", "\\\\")
  string = string.replace("\n", "\\n")
  if '"' in string and "'" not in string:
    return "'" + string + "'"
  else:
    string = string.replace("\"", "\\\"")
    return "\"" + string + "\""

def hex_bigint(n):
  if -10 < n < 10: return str(n) + "n"
  s = hex(n)
  if s[-1] == "L":
    s = s[:-1]
  return s + "n"

def bin_bigint(n):
  if n < 0 or n > 256: return hex_bigint(n)
  if n <= 1: return str(n) + "n"
  return bin(n) + "n"

def zfill_bin_bigint(n, bits):
  if n < 0: raise ValueError
  return "0b" + bin(n)[2:].zfill(bits) + "n"
