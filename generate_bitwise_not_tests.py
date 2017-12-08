
from util import js_repr

op_list = [
  ("bitwise-not",),
]

# This is the hex representation of Number.MAX_VALUE.
max_value = "0xfffffffffffff8" + "0" * 242 + "n"
max_value_plus_one = "0xfffffffffffff8" + "0" * 241 + "1n"
max_value_minus_one = "0xfffffffffffff7" + "f" * 242 + "n"

# This is the hex representation of Number.MAX_SAFE_INTEGER.
max_safe_integer_digits = "0x1fffffffffffff"

case_groups = [
  ("bigint.js", [
    ("~0n", "-1n", None),
    ("~(0n)", "-1n", None),
    ("~1n", "-2n", None),
    ("~-1n", "0n", None),
    ("~(-1n)", "0n", None),
    ("~~1n", "1n", None),
    ("~0x5an", "-0x5bn", None),
    ("~-0x5an", "0x59n", None),
    ("~0xffn", "-0x100n", None),
    ("~-0xffn", "0xfen", None),
    ("~0xffffn", "-0x10000n", None),
    ("~-0xffffn", "0xfffen", None),
    ("~0xffffffffn", "-0x100000000n", None),
    ("~-0xffffffffn", "0xfffffffen", None),
    ("~0xffffffffffffffffn", "-0x10000000000000000n", None),
    ("~-0xffffffffffffffffn", "0xfffffffffffffffen", None),
    ("~0x123456789abcdef0fedcba9876543210n", "-0x123456789abcdef0fedcba9876543211n", None),
  ]),
  ("bigint-non-primitive.js", [
    ("~Object(1n)", "-2n", None),
    "\nfunction err() {\n  throw new Test262Error();\n}\n",
    ("~{[Symbol.toPrimitive]: function() { return 1n; }, valueOf: err, toString: err}", "-2n", "primitive from @@toPrimitive"),
    ("~{valueOf: function() { return 1n; }, toString: err}", "-2n", "primitive from {}.valueOf"),
    ("~{toString: function() { return 1n; }}", "-2n", "primitive from {}.toString"),
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
        for case_item in case_list:
          if type(case_item) == str:
            f.write(case_item + "\n")
          else:
            a, b, message = case_item
            f.write(generateCase(a, b, message))

def generateCase(a, b, message):
  force_line_wrap = False
  if message != None:
    message = js_repr(message)
    force_line_wrap = True
  else:
    message = js_repr(a + " === " + b)
  line = "assert.sameValue({}, {}, {});\n".format(a, b, message)
  if not force_line_wrap and len(line) < 100:
    return line
  return "assert.sameValue(\n  {}, {},\n  {});\n".format(a, b, message)

if __name__ == "__main__":
  main()



