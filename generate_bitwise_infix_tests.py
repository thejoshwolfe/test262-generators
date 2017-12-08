
from util import js_repr, hex_bigint, zfill_bin_bigint

op_list = [
  ("&", lambda a, b: a & b, "bitwise-and"),
  ("|", lambda a, b: a | b, "bitwise-or"),
  ("^", lambda a, b: a ^ b, "bitwise-xor"),
]

# This is the hex representation of Number.MAX_VALUE.
max_value = "0xfffffffffffff8" + "0" * 242 + "n"
max_value_plus_one = "0xfffffffffffff8" + "0" * 241 + "1n"
max_value_minus_one = "0xfffffffffffff7" + "f" * 242 + "n"

# This is the hex representation of Number.MAX_SAFE_INTEGER.
max_safe_integer_digits = "0x1fffffffffffff"
max_safe_integer_base_10 = "9007199254740991"

case_groups = [
  ("bigint.js", [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 2),
    (2, 3),
    (0xffffffff, 0),
    (0xffffffff, 0xffffffff),
    (0xffffffffffffffff, 0x0),
    (0xffffffffffffffff, 0xffffffff),
    (0xffffffffffffffff, 0xffffffffffffffff),
    (0xbf2ed51ff75d380fd3be813ec6185780, 0x4aabef2324cedff5387f1f65),
    (0, -1),
    (0, -2),
    (1, -2),
    (2, -2),
    (2, -3),
    (-1, -2),
    (-2, -2),
    (-2, -3),
    (0xffffffff, -1),
    (0xffffffffffffffff, -1),
    (0xbf2ed51ff75d380fd3be813ec6185780, -0x4aabef2324cedff5387f1f65),
    (-0xbf2ed51ff75d380fd3be813ec6185780, 0x4aabef2324cedff5387f1f65),
    (-0xbf2ed51ff75d380fd3be813ec6185780, -0x4aabef2324cedff5387f1f65),
    (-0xffffffff, 0),
    (-0xffffffffffffffff, 0x10000000000000000),
    (-0xffffffffffffffffffffffff, 0x10000000000000000),
  ]),
  ("bigint-non-primitive.js", [
    ("Object(0b101n)", "0b011n", None),
    ("Object(0b101n)", "Object(0b011n)", None),
    "\nfunction err() {\n  throw new Test262Error();\n}\n",
    ("{[Symbol.toPrimitive]: function() { return 0b101n; }, valueOf: err, toString: err}", "0b011n", "primitive from @@toPrimitive"),
    ("{valueOf: function() { return 0b101n; }, toString: err}", "0b011n", "primitive from {}.valueOf"),
    ("{toString: function() { return 0b101n; }}", "0b011n", "primitive from {}.toString"),
  ]),
]

def main():
  for (op_str, op_lambda, op_name) in op_list:
    for (group_name, case_list) in case_groups:
      file_name = "test/language/expressions/{}/{}".format(op_name, group_name)
      with open(file_name) as f:
        contents = f.read()
      header = contents[:contents.index("---*/\n\n") + len("---*/\n\n")]

      with open(file_name, "w") as f:
        f.write(header)
        for case_item in case_list:
          if type(case_item) == str:
            f.write(case_item + "\n")
          elif len(case_item) == 2:
            (a, b) = case_item
            f.write(generateCase(a, op_str, b, op_lambda))
            if a != b:
              f.write(generateCase(b, op_str, a, op_lambda))
          else:
            (a, b, message) = case_item
            result = zfill_bin_bigint(op_lambda(5, 3), 3)
            f.write(generateNonPrimitiveCase(a, op_str, b, result, message))
            if a.replace("0b101n", "0b011n") != b.replace("0b101n", "0b011n"):
              f.write(generateNonPrimitiveCase(b, op_str, a, result, message))

def generateCase(a, op_str, b, op_lambda):
  result = op_lambda(a, b)
  if 0 <= a < 16 and 0 <= b < 16:
    a_str = zfill_bin_bigint(a, 2)
    b_str = zfill_bin_bigint(b, 2)
    result_str = zfill_bin_bigint(result, 2)
  else:
    a_str = hex_bigint(a)
    b_str = hex_bigint(b)
    result_str = hex_bigint(result)
  expression = a_str + " " + op_str + " " + b_str
  expression_repr = js_repr(expression + " === " + result_str);
  line = "assert.sameValue({}, {}, {});\n".format(expression, result_str, expression_repr)
  if len(a_str) + len(b_str) < 35:
    return line
  return "assert.sameValue(\n  {}, {},\n  {});\n".format(expression, result_str, expression_repr)

def generateNonPrimitiveCase(a, op_str, b, result, message):
  expression = a + " " + op_str + " " + b
  if message != None:
    return "assert.sameValue(\n  {}, {},\n  {});\n".format(expression, result, js_repr(message))
  else:
    expression_repr = js_repr(expression + " === " + result);
    return "assert.sameValue({}, {}, {});\n".format(expression, result, expression_repr)

if __name__ == "__main__":
  main()

