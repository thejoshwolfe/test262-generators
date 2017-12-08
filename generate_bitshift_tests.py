
from util import (
  js_repr,
  hex_bigint,
  bin_bigint,
)

def left_shift(a, b):
  if b < 0:
    return a >> -b
  return a << b
def right_shift(a, b):
  if b < 0:
    return a << -b
  return a >> b

op_list = [
  ("<<", True, "left-shift"),
  (">>", False, "right-shift"),
  (">>>", None, "unsigned-right-shift"),
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
    (5, 1),
    (5, 2),
    (5, 3),
    (5, -1),
    (5, -2),
    (5, -3),
    (0, 128),
    (0, -128),
    (0x246, 0),
    (0x246, 127),
    (0x246, 128),
    (0x246, 129),
    (0x246, -128),
    (0x123456789abcdef0fedcba9876543212345678, 64),
    (0x123456789abcdef0fedcba9876543212345678, 32),
    (0x123456789abcdef0fedcba9876543212345678, 16),
    (0x123456789abcdef0fedcba9876543212345678, 0),
    (0x123456789abcdef0fedcba9876543212345678, -16),
    (0x123456789abcdef0fedcba9876543212345678, -32),
    (0x123456789abcdef0fedcba9876543212345678, -64),
    (0x123456789abcdef0fedcba9876543212345678, -127),
    (0x123456789abcdef0fedcba9876543212345678, -128),
    (0x123456789abcdef0fedcba9876543212345678, -129),
    (-5, 1),
    (-5, 2),
    (-5, 3),
    (-5, -1),
    (-5, -2),
    (-5, -3),
    (-1, 128),
    (-1, 0),
    (-1, -128),
    (-0x246, 0),
    (-0x246, 127),
    (-0x246, 128),
    (-0x246, 129),
    (-0x246, -128),
    (-0x123456789abcdef0fedcba9876543212345678, 64),
    (-0x123456789abcdef0fedcba9876543212345678, 32),
    (-0x123456789abcdef0fedcba9876543212345678, 16),
    (-0x123456789abcdef0fedcba9876543212345678, 0),
    (-0x123456789abcdef0fedcba9876543212345678, -16),
    (-0x123456789abcdef0fedcba9876543212345678, -32),
    (-0x123456789abcdef0fedcba9876543212345678, -64),
    (-0x123456789abcdef0fedcba9876543212345678, -127),
    (-0x123456789abcdef0fedcba9876543212345678, -128),
    (-0x123456789abcdef0fedcba9876543212345678, -129),
  ]),
  ("bigint-non-primitive.js", [
    ("Object(0b101n)", "1n", None),
    ("Object(0b101n)", "Object(1n)", None),
    "\nfunction err() {\n  throw new Test262Error();\n}\n",
    ("{[Symbol.toPrimitive]: function() { return 0b101n; }, valueOf: err, toString: err}", "1n", "primitive from @@toPrimitive"),
    ("{valueOf: function() { return 0b101n; }, toString: err}", "1n", "primitive from {}.valueOf"),
    ("{toString: function() { return 0b101n; }}", "1n", "primitive from {}.toString"),
    ("0b101n", "{[Symbol.toPrimitive]: function() { return 1n; }, valueOf: err, toString: err}", "primitive from @@toPrimitive"),
    ("0b101n", "{valueOf: function() { return 1n; }, toString: err}", "primitive from {}.valueOf"),
    ("0b101n", "{toString: function() { return 1n; }}", "primitive from {}.toString"),
    ("{valueOf: function() { return 0b101n; }}", "{valueOf: function() { return 1n; }}", "primitive from {}.valueOf"),
  ]),
]

def main():
  for (op_str, is_left, op_name) in op_list:
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
            f.write(generateCase(a, op_str, b, is_left))
          else:
            (a, b, message) = case_item
            f.write(generateNonPrimitiveCase(a, op_str, b, is_left, message))

def pedantic_left_shift(a, b):
  python_result = a << b
  ecma_result = a * (2**b)
  if python_result != ecma_result:
    raise Exception("python and ecma disagree")
  return python_result
def pedantic_right_shift(a, b):
  python_result = a >> b
  ecma_result = (a - (a % (2**b))) / (2**b)
  if python_result != ecma_result:
    raise Exception("python and ecma disagree")
  return python_result

def generateCase(a, op_str, b, is_left):
  if is_left == True:
    if b >= 0:
      result = pedantic_left_shift(a, b)
    else:
      result = pedantic_right_shift(a, -b)
  elif is_left == False:
    b = -b
    if b >= 0:
      result = pedantic_right_shift(a, b)
    else:
      result = pedantic_left_shift(a, -b)
  else:
    expression = "{}n {} {}n".format(str(a), op_str, str(b))
    expression_repr = js_repr("bigint {} bigint throws a TypeError".format(op_str))
    return "assert.throws(TypeError, function() { %s; }, %s);\n" % (expression, expression_repr)

  a_str = bin_bigint(a)
  b_str = str(b) + "n"
  result_str = bin_bigint(result)
  expression = a_str + " " + op_str + " " + b_str
  expression_repr = js_repr(expression + " === " + result_str);
  line = "assert.sameValue({}, {}, {});\n".format(expression, result_str, expression_repr)
  if len(a_str) + len(b_str) < 35:
    return line
  return "assert.sameValue(\n  {}, {},\n  {});\n".format(expression, result_str, expression_repr)

def generateNonPrimitiveCase(a_str, op_str, b_str, is_left, message):
  expression = a_str + " " + op_str + " " + b_str
  if is_left == True:
    result = bin_bigint(5 << 1)
  elif is_left == False:
    result = bin_bigint(5 >> 1)
  else:
    expression = "{} {} {}".format(a_str, op_str, b_str)
    if message != None:
      expression_repr = js_repr("bigint >>> bigint throws a TypeError for {}".format(message))
    else:
      expression_repr = js_repr("bigint >>> bigint throws a TypeError for {}".format(expression))
    if expression[:1] == "{":
      expression = "({})".format(expression)
    return "assert.throws(TypeError,\n  function() { %s; },\n  %s);\n" % (expression, expression_repr)

  if message != None:
    return "assert.sameValue(\n  {}, {},\n  {});\n".format(expression, result, js_repr(message))
  else:
    expression_repr = js_repr(expression + " === " + result);
    return "assert.sameValue({}, {}, {});\n".format(expression, result, expression_repr)

if __name__ == "__main__":
  main()

