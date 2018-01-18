
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
  ("bigint-and-number.js", [
    ('1n', '1'),
    ('Object(1n)', '1'),
    ('1n', 'Object(1)'),
    ('Object(1n)', 'Object(1)'),
    ('1n', 'NaN'),
    ('1n', 'Infinity'),
    ('1n', 'true'),
    ('1n', '"1"', "string"),
    ('1n', 'null'),
    ('1n', 'undefined'),
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
        for case_item in case_list:
          if len(case_item) == 3:
            if op_str == "+":
              # + operator with string operands isn't what we're testing here
              continue
            case_item = case_item[:-1]
          (a, b) = case_item
          f.write(generateCase(a, op_str, b))
          f.write(generateCase(b, op_str, a))

      print(file_name)

def generateCase(a, op_str, b):
  if a.startswith('{'): a = '(' + a + ')'
  expression = a + ' ' + op_str + ' ' + b
  message = js_repr(expression + " throws TypeError");
  return 'assert.throws(TypeError, function() { %s; }, %s);\n' % (expression, message)

if __name__ == "__main__":
  main()

