
from util import js_repr

case_template = """\
var x = %s;
assert.sameValue(%s, %s, %s);
assert.sameValue(%s, %s, %s);
"""

op_list = [
  ("++%s", lambda lo, hi: (lo, hi, hi),  "prefix-increment"),
  ("--%s", lambda lo, hi: (hi, lo, lo),  "prefix-decrement"),
  ("%s++", lambda lo, hi: (lo, lo, hi),  "postfix-increment"),
  ("%s--", lambda lo, hi: (hi, hi, lo),  "postfix-decrement"),
]

# This is the hex representation of Number.MAX_VALUE.
max_value = "0xfffffffffffff8" + "0" * 242 + "n"
max_value_plus_one = "0xfffffffffffff8" + "0" * 241 + "1n"
max_value_minus_one = "0xfffffffffffff7" + "f" * 242 + "n"

# This is the hex representation of Number.MAX_SAFE_INTEGER.
max_safe_integer_digits = "0x1fffffffffffff"

case_groups = [
  ("bigint.js", [
    ("0n", "1n", "%s", "x"),
    ("-1n", "0n", "%s", "x"),
    ("123456n", "123457n", "%s", "x"),
    ("-123457n", "-123456n", "%s", "x"),
    (max_safe_integer_digits + "00n", max_safe_integer_digits + "01n", "%s", "x"),
    ("-" + max_safe_integer_digits + "01n", "-" + max_safe_integer_digits + "00n", "%s", "x"),
    ("0n", "1n", "{y:%s}", "x.y"),
    ("0n", "1n", "{y:{z:%s}}", "x.y.z"),
    ("0n", "1n", "[%s]", "x[0]"),
    ("0n", "1n", "[null, [null, null, %s]]", "x[1][2]"),
    ("0n", "1n", "{y:[%s]}", "x.y[0]"),
    ("0n", "1n", "[{z:%s}]", "x[0].z"),
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
        cases = []
        for (lo, hi, initializer, accessor) in case_list:
          (initial_value, middle_value, final_value) = op_lambda(lo, hi)
          middle_message = "var x = %s; %s === %s" % (
            initializer % initial_value,
            op_str % accessor,
            middle_value)
          final_message = "var x = %s; %s; %s === %s" % (
            initializer % initial_value,
            op_str % accessor,
            accessor,
            final_value)
          cases.append(case_template % (initializer % initial_value,
            op_str % accessor, middle_value, js_repr(middle_message),
            accessor, final_value, js_repr(final_message)))
        f.write("\n".join(cases))

if __name__ == "__main__":
  main()

