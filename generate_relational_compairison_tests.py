
from util import js_repr

op_list = [
  ("<",  lambda a, b: a < b,  "less-than"),
  ("<=", lambda a, b: a <= b, "less-than-or-equal"),
  (">",  lambda a, b: a > b,  "greater-than"),
  (">=", lambda a, b: a >= b, "greater-than-or-equal"),
]

# This is the hex representation of Number.MAX_VALUE.
max_value_plus_one = "0xfffffffffffff8" + "0" * 241 + "1n"
max_value_minus_one = "0xfffffffffffff7" + "f" * 242 + "n"

# This is the hex representation of Number.MAX_SAFE_INTEGER.
max_safe_integer_digits = "0x1fffffffffffff"

case_groups = [
  ("bigint-and-number.js", [
    ("0n", "0", 0),
    ("0n", "-0", 0),
    ("0n", "0.000000000001", -1),
    ("0n", "1", -1),
    ("1n", "0", 1),
    ("1n", "0.999999999999", 1),
    ("1n", "1", 0),
    ("0n", "Number.MIN_VALUE", -1),
    ("0n", "-Number.MIN_VALUE", 1),
    ("-10n", "Number.MIN_VALUE", -1),
  ]),
  ("bigint-and-number-extremes.js", [
    ("1n", "Number.MAX_VALUE", -1),
    ("1n", "-Number.MAX_VALUE", 1),
    (max_value_minus_one, "Number.MAX_VALUE", -1),
    (max_value_plus_one, "Number.MAX_VALUE", 1),
  ]),
  ("bigint-and-non-finite.js", [
    ("1n", "Infinity", -1),
    ("-1n", "Infinity", -1),
    ("1n", "-Infinity", 1),
    ("-1n", "-Infinity", 1),
    ("0n", "NaN", None),
  ]),
  ("bigint-and-bigint.js", [
    ("0n", "0n", 0),
    ("1n", "1n", 0),
    ("-1n", "-1n", 0),
    ("0n", "-0n", 0),
    ("0n", "1n", -1),
    ("0n", "-1n", 1),
    ("1n", "-1n", 1),
    (max_safe_integer_digits + "01n", max_safe_integer_digits + "02n", -1),
    ("-" + max_safe_integer_digits + "01n", "-" + max_safe_integer_digits + "02n", 1),
    ("0x10000000000000000n", "0n", 1),
    ("0x10000000000000000n", "1n", 1),
    ("0x10000000000000000n", "-1n", 1),
    ("0x10000000000000001n", "0n", 1),
    ("-0x10000000000000000n", "0n", -1),
    ("-0x10000000000000000n", "1n", -1),
    ("-0x10000000000000000n", "-1n", -1),
    ("-0x10000000000000001n", "0n", -1),
    ("0x10000000000000000n", "0x100000000n", 1),
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
        for (a, b, cmp_value) in case_list:
          f.write(generateCase(a, op_str, b, result_for(op_lambda, cmp_value, 0)))
          if a != b:
            f.write(generateCase(b, op_str, a, result_for(op_lambda, 0, cmp_value)))

def result_for(op_lambda, a, b):
  if a == None or b == None: return "false"
  return ["false", "true"][op_lambda(a, b)]

def generateCase(a, op, b, result):
  expression = a + " " + op + " " + b
  expression_repr = js_repr(expression)
  if len(a) + len(b) < 80:
    return "assert.sameValue({}, {}, {});\n".format(expression, result, expression_repr)
  else:
    return "assert.sameValue(\n  {},\n  {},\n  {});\n".format(expression, result, expression_repr)

if __name__ == "__main__":
  main()
