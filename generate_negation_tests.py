
from util import js_repr

op_list = [
  ("unary-minus",),
]

# This is the hex representation of Number.MAX_VALUE.
max_value = "0xfffffffffffff8" + "0" * 242 + "n"
max_value_plus_one = "0xfffffffffffff8" + "0" * 241 + "1n"
max_value_minus_one = "0xfffffffffffff7" + "f" * 242 + "n"

# This is the hex representation of Number.MAX_SAFE_INTEGER.
max_safe_integer_digits = "0x1fffffffffffff"

case_groups = [
  ("bigint.js", [
    ("-0n", "0n", True),
    ("-(0n)", "0n", True),
    ("-1n", "1n", False),
    ("-(1n)", "-1n", True),
    ("-(1n)", "1n", False),
    ("-(-1n)", "1n", True),
    ("-(-1n)", "-1n", False),
    ("- - 1n", "1n", True),
    ("- - 1n", "-1n", False),
    ("-(" + max_safe_integer_digits + "01n)", "-" + max_safe_integer_digits + "01n", True),
    ("-(" + max_safe_integer_digits + "01n)", max_safe_integer_digits + "01n", False),
    ("-(" + max_safe_integer_digits + "01n)", "-" + max_safe_integer_digits + "00n", False),
  ]),
  ("bigint-non-primitive.js", [
    ("-Object(1n)", "-1n", True),
    ("-Object(1n)", "1n", False),
    ("-Object(1n)", "Object(-1n)", False),
    ("-Object(-1n)", "1n", True),
    ("-Object(-1n)", "-1n", False),
    ("-Object(-1n)", "Object(1n)", False),
    ("-{[Symbol.toPrimitive]: function() { return 1n; }, valueOf: function() { $ERROR(); }, toString: function() { $ERROR(); }}", "-1n", True),
    ("-{valueOf: function() { return 1n; }, toString: function() { $ERROR(); }}", "-1n", True),
    ("-{toString: function() { return 1n; }}", "-1n", True),
  ]),
]

def main():
  for (op_name,) in op_list:
    for (group_name, case_list) in case_groups:
      file_name = "test/language/expressions/{}/{}".format(op_name, group_name)
      with open(file_name) as f:
        contents = f.read()
      header = contents[:contents.index("---*/\n\n") + len("---*/\n\n")]

      with open(file_name, "w") as f:
        f.write(header)
        cases = []
        for (a, b, eq) in case_list:
          f.write(generateCase(a, b, eq))

def generateCase(a, b, eq):
  if eq:
    method = "sameValue"
    message = js_repr(a + " === " + b)
  else:
    method = "notSameValue"
    message = js_repr(a + " !== " + b)
  line = "assert.{}({}, {}, {});\n".format(method, a, b, message)
  if len(line) < 100:
    return line
  return "assert.{}(\n  {}, {},\n  {});\n".format(method, a, b, message)

if __name__ == "__main__":
  main()


