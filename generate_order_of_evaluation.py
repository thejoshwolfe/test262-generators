
from util import js_repr, hex_bigint, zfill_bin_bigint

op_list = [
  ('**', "exponentiation"),
  ('*', "multiplication"),
  ('/', "division"),
  ('%', "modulus"),
  ('+', "addition"),
  ('-', "subtraction"),
  ('<<', "left-shift"),
  ('>>', "right-shift"),
  ('>>>', "unsigned-right-shift"),
  ('&', "bitwise-and"),
  ('|', "bitwise-or"),
  ('^', "bitwise-xor"),
]

case_groups = [
  ("order-of-evaluation.js", [
    ("*", "MyError", "err", 1, "?GetValue(lhs) throws."),
    ("*", ["err"], "MyError", 2, "?GetValue(rhs) throws."),
    ("*", ["MyError"], ["err"], 3, "?ToPrimive(lhs) throws."),
    ("*", ["1"], ["MyError"], 4, "?ToPrimive(rhs) throws."),
    ("-", ["Symbol"], ["err"], 3, "?ToNumeric(lhs) throws."),
    ("+", ["Symbol"], ["MyError"], 4, "?ToPrimive(rhs) is called before ?ToNumeric(lhs)."),
    ("*", ["1"], ["Symbol"], 4, "GetValue(lhs) throws."),
  ]),
]

def main():
  for (op_str, op_name) in op_list:
    for (group_name, case_list) in case_groups:
      file_name = "test/language/expressions/{}/{}".format(op_name, group_name)
      with open(file_name) as f:
        contents = f.read()
      header = contents[:contents.index('---*/\n\n') + len('---*/\n\n')]

      with open(file_name, "w") as f:
        f.write(header)
        f.write("function MyError() {}\n")
        f.write("var trace;\n")
        for case_item in case_list:
          f.write(generateCase(op_str, *case_item))

      print(file_name)

case_template = '''
// %(message)s
trace = "";
assert.throws(%(error)s, function() {
  (function() {
    trace += "1";
    %(lhs_value)s
  })() %(op)s (function() {
    trace += "2";
    %(rhs_value)s
  })();
}, "%(message)s");
assert.sameValue(trace, "%(trace)s", "%(message)s");
'''

value_template = '''\
    return {
      valueOf: function() {
        trace += "%(3_or_4)s";
        %(value)s
      }
    };
'''.strip()

def generateCase(op_str, filter_code, lhs, rhs, trace_count, message):
  if filter_code == "+":
    if op_str != "+": return ""
  elif filter_code == "-":
    if op_str == "+": return ""
  else:
    assert filter_code == "*"
  lhs_template = "%(value)s"
  if type(lhs) == list:
    [lhs] = lhs
    lhs_template = value_template
  rhs_template = "%(value)s"
  if type(rhs) == list:
    [rhs] = rhs
    rhs_template = value_template

  error = ["TypeError"]
  def valueFor(token):
    if token == "err": return 'throw new Test262Error("should not be evaluated");'
    if token == "1": return 'return 1;'
    if token == "Symbol": return 'return Symbol("1");'
    if token == "MyError":
      error[0] = "MyError"
      return 'throw new MyError();'
    assert False

  return case_template % {
    "message": message,
    "op": op_str,
    "trace": "1234"[:trace_count],
    "lhs_value": lhs_template % {
      "value": valueFor(lhs),
      "3_or_4": "3",
    },
    "rhs_value": rhs_template % {
      "value": valueFor(rhs),
      "3_or_4": "4",
    },
    "error": error[0],
  }

if __name__ == "__main__":
  main()


