
from util import js_repr

def make_comparator(is_strict, is_equal):
  def f(a, b, cmp_value):
    if is_strict:
      if (a[-1:] == "n") != (b[-1:] == "n"):
        return not is_equal
    return (cmp_value == 0) == is_equal
  return f

op_list = [
  ("==",  make_comparator(False, True),  "equals"),
  ("!=",  make_comparator(False, False), "does-not-equals"),
  ("===", make_comparator(True, True),   "strict-equals"),
  ("!==", make_comparator(True, False),  "strict-does-not-equals"),
]

# This is the hex representation of Number.MAX_VALUE.
max_value = "0xfffffffffffff8" + "0" * 242 + "n"
max_value_plus_one = "0xfffffffffffff8" + "0" * 241 + "1n"
max_value_minus_one = "0xfffffffffffff7" + "f" * 242 + "n"

# This is the hex representation of Number.MAX_SAFE_INTEGER.
max_safe_integer_digits = "0x1fffffffffffff"
max_safe_integer_base_10 = "9007199254740991"

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
    (max_value, "Number.MAX_VALUE", 0),
    (max_value_plus_one, "Number.MAX_VALUE", 1),
  ]),
  ("bigint-and-non-finite.js", [
    ("0n", "Infinity", -1),
    ("1n", "Infinity", -1),
    ("-1n", "Infinity", -1),
    ("0n", "-Infinity", 1),
    ("1n", "-Infinity", 1),
    ("-1n", "-Infinity", 1),
    ("0n", "NaN", None),
    ("1n", "NaN", None),
    ("-1n", "NaN", None),
  ]),
  ("bigint-and-boolean.js", [
    ("-1n", 'false', 1),
    ("-1n", 'true', 1),
    ("0n", 'false', 0),
    ("0n", 'true', 1),
    ("1n", 'false', 1),
    ("1n", 'true', 0),
    ("2n", 'false', 1),
    ("2n", 'true', 1),
  ]),
  ("bigint-and-string.js", [
    ("0n", '""', 0),
    ("0n", '"-0"', 0),
    ("0n", '"0"', 0),
    ("0n", '"-1"', 1),
    ("0n", '"1"', 1),
    ("0n", '"foo"', 1),
    ("1n", '""', 1),
    ("1n", '"-0"', 1),
    ("1n", '"0"', 1),
    ("1n", '"-1"', 1),
    ("1n", '"1"', 0),
    ("1n", '"foo"', 1),
    ("-1n", '"-"', 1),
    ("-1n", '"-0"', 1),
    ("-1n", '"-1"', 0),
    ("-1n", '"-foo"', 1),
    (max_safe_integer_base_10 + "01n", '"' + max_safe_integer_base_10 + '01"', 0),
    (max_safe_integer_base_10 + "02n", '"' + max_safe_integer_base_10 + '01"', 1),
  ]),
  ("bigint-and-object.js", [
    ("0n", "Object(0n)", 0),
    ("0n", "Object(1n)", 1),
    ("1n", "Object(0n)", 1),
    ("1n", "Object(1n)", 0),
    ("2n", "Object(0n)", 1),
    ("2n", "Object(1n)", 1),
    ("2n", "Object(2n)", 0),
    ("0n", "{}", 1),
    ("0n", "{valueOf: function() { return 0n; }}", 0),
    ("0n", "{valueOf: function() { return 1n; }}", 1),
    ("0n", '{toString: function() { return "0"; }}', 0),
    ("0n", '{toString: function() { return "1"; }}', 1),
    (max_safe_integer_base_10 + "01n", "{valueOf: function() { return " + max_safe_integer_base_10 + "01n; }}", 0),
    (max_safe_integer_base_10 + "01n", "{valueOf: function() { return " + max_safe_integer_base_10 + "02n; }}", 1),
    (max_safe_integer_base_10 + "01n", '{toString: function() { return "' + max_safe_integer_base_10 + '01"; }}', 0),
    (max_safe_integer_base_10 + "01n", '{toString: function() { return "' + max_safe_integer_base_10 + '02"; }}', 1),
  ]),
  ("bigint-and-incomparable-primitive.js", [
    ("0n", "undefined", 1),
    ("1n", "undefined", 1),
    ("0n", "null", 1),
    ("1n", "null", 1),
    ("0n", 'Symbol("1")', 1),
    ("1n", 'Symbol("1")', 1),
  ]),
  ("bigint-and-bigint.js", [
    ("0n", "0n", 0),
    ("1n", "1n", 0),
    ("-1n", "-1n", 0),
    ("0n", "-0n", 0),
    ("0n", "1n", -1),
    ("0n", "-1n", 1),
    ("1n", "-1n", 1),
    (max_safe_integer_digits + "01n", max_safe_integer_digits + "01n", 0),
    (max_safe_integer_digits + "01n", max_safe_integer_digits + "02n", -1),
    ("-" + max_safe_integer_digits + "01n", "-" + max_safe_integer_digits + "01n", 0),
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
          f.write(generateCase(a, op_str, b, result_for(op_lambda, a, b, cmp_value)))
          if a != b:
            f.write(generateCase(b, op_str, a, result_for(op_lambda, a, b, cmp_value)))

def result_for(op_lambda, a, b, cmp_value):
  return ["false", "true"][op_lambda(a, b, cmp_value)]

def generateCase(a, op, b, result):
  expression = a + " " + op + " " + b
  expression_repr = js_repr(expression);
  if len(a) + len(b) < 80:
    return "assert.sameValue({}, {}, {});\n".format(expression, result, expression_repr)
  else:
    return "assert.sameValue(\n  {},\n  {},\n  {});\n".format(expression, result, expression_repr)

if __name__ == "__main__":
  main()
