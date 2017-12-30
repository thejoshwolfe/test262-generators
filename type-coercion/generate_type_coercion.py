#!/usr/bin/env python
# Copyright (C) 2017 Josh Wolfe. All rights reserved.
# This code is governed by the BSD license found in the LICENSE file.

import os
import sys

from type_coercion import generate_tests

output_path = "test"

def main():

    generate_tests(
        path_prefix="language/expressions/exponentiation/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-exp-operator-runtime-semantics-evaluation",
            "description": "exponentiation operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) ** 1n, 2n, %(message)s);',
                   'assert.sameValue(1n **   %(value)s  , 1n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) ** 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n **   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/multiplication/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-multiplicative-operators-runtime-semantics-evaluation",
            "description": "multiplication operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) * 2n, 4n, %(message)s);',
                   'assert.sameValue(2n *   %(value)s  , 4n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) * 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n *   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/division/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-multiplicative-operators-runtime-semantics-evaluation",
            "description": "division operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) / 2n, 1n, %(message)s);',
                   'assert.sameValue(2n /   %(value)s  , 1n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) / 1n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n /   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/modulus/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-multiplicative-operators-runtime-semantics-evaluation",
            "description": "modulus operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) %% 2n, 0n, %(message)s);',
                   'assert.sameValue(2n %%   %(value)s  , 0n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) %% 1n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n %%   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/addition/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-addition-operator-plus-runtime-semantics-evaluation",
            "description": "addition operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) + 1n, 3n, %(message)s);',
                   'assert.sameValue(1n +   %(value)s  , 3n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) + 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n +   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/subtraction/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-subtraction-operator-minus-runtime-semantics-evaluation",
            "description": "subtraction operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) - 1n, 1n, %(message)s);',
                   'assert.sameValue(3n -   %(value)s  , 1n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) - 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n -   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/left-shift/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-left-shift-operator-runtime-semantics-evaluation",
            "description": "left-shift operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) << 1n, 4n, %(message)s);',
                   'assert.sameValue(1n <<   %(value)s  , 4n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) << 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n <<   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/right-shift/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-signed-right-shift-operator-runtime-semantics-evaluation",
            "description": "right-shift operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) >> 1n, 1n, %(message)s);',
                   'assert.sameValue(4n >>   %(value)s  , 1n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) >> 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n >>   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/unsigned-right-shift/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-unsigned-right-shift-operator-runtime-semantics-evaluation",
            "description": "unsigned-right-shift operator ToNumeric with BigInt operands",
            "info": "After ToNumeric type coercion, unsigned-right-shift always throws for BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.throws(TypeError, function() { ((%(value)s)) >>> 0n; }, %(message)s);',
                   'assert.throws(TypeError, function() { 0n >>>   %(value)s  ; }, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) >>> 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n >>>   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/bitwise-and/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-binary-bitwise-operators-runtime-semantics-evaluation",
            "description": "bitwise-and operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) & 3n, 2n, %(message)s);',
                   'assert.sameValue(3n &   %(value)s  , 2n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) & 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n &   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/bitwise-or/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-binary-bitwise-operators-runtime-semantics-evaluation",
            "description": "bitwise-or operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) | 1n, 3n, %(message)s);',
                   'assert.sameValue(1n |   %(value)s  , 3n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) | 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n |   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="language/expressions/bitwise-xor/bigint",
        conversion="ToNumeric-BigInt",
        frontmatter={
            "esid": "sec-binary-bitwise-operators-runtime-semantics-evaluation",
            "description": "bitwise-xor operator ToNumeric with BigInt operands",
            "features": ["BigInt"],
        },
        templates={
            '2n': ('assert.sameValue(((%(value)s)) ^ 3n, 1n, %(message)s);',
                   'assert.sameValue(3n ^   %(value)s  , 1n, %(message)s);'),
            "throws": ('assert.throws(%(error)s, function() { ((%(value)s)) ^ 0n; }, %(message)s);',
                       'assert.throws(%(error)s, function() { 0n ^   %(value)s  ; }, %(message)s);'),
        },
    )

    generate_tests(
        path_prefix="built-ins/BigInt/asIntN/bits-toindex",
        conversion="ToIndex",
        frontmatter={
            "esid": "pending",
            "description": "BigInt.asIntN type coercion for bits parameter",
            "info": """
                BigInt.asIntN ( bits, bigint )

                1. Let bits be ? ToIndex(bits).
            """,
            "features": ["BigInt"],
        },
        templates={
            '0': 'assert.sameValue(BigInt.asIntN(%(value)s, 1n), 0n, %(message)s);',
            '1': 'assert.sameValue(BigInt.asIntN(%(value)s, 1n), -1n, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { BigInt.asIntN(%(value)s, 0n); }, %(message)s);',
        },
        nominal_value_cases=[
            (3, 'assert.sameValue(BigInt.asIntN(%(value)s, 10n), 2n, %(message)s);'),
        ],
    )

    generate_tests(
        path_prefix="built-ins/BigInt/asUintN/bits-toindex",
        conversion="ToIndex",
        frontmatter={
            "esid": "pending",
            "description": "BigInt.asUintN type coercion for bits parameter",
            "info": """
                BigInt.asUintN ( bits, bigint )

                1. Let bits be ? ToIndex(bits).
            """,
            "features": ["BigInt"],
        },
        templates={
            '0': 'assert.sameValue(BigInt.asUintN(%(value)s, 1n), 0n, %(message)s);',
            '1': 'assert.sameValue(BigInt.asUintN(%(value)s, 1n), 1n, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { BigInt.asUintN(%(value)s, 0n); }, %(message)s);',
        },
        nominal_value_cases=[
            (3, 'assert.sameValue(BigInt.asUintN(%(value)s, 10n), 2n, %(message)s);'),
        ],
    )

    generate_tests(
        path_prefix="built-ins/BigInt/asIntN/bigint-tobigint",
        conversion="ToBigInt",
        frontmatter={
            "esid": "pending",
            "description": "BigInt.asIntN type coercion for bigint parameter",
            "info": """
                BigInt.asIntN ( bits, bigint )

                2. Let bigint ? ToBigInt(bigint).
            """,
            "features": ["BigInt"],
        },
        templates={
            '0n': 'assert.sameValue(BigInt.asIntN(2, %(value)s), 0n, %(message)s);',
            '1n': 'assert.sameValue(BigInt.asIntN(2, %(value)s), 1n, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { BigInt.asIntN(0, %(value)s); }, %(message)s);',
        },
        nominal_value_cases=[
            (10, 'assert.sameValue(BigInt.asIntN(3, %(value)s), 2n, %(message)s);'),
            (12345678901234567890003, 'assert.sameValue(BigInt.asIntN(4, %(value)s), 3n, %(message)s);'),
        ],
    )

    generate_tests(
        path_prefix="built-ins/BigInt/asUintN/bigint-tobigint",
        conversion="ToBigInt",
        frontmatter={
            "esid": "pending",
            "description": "BigInt.asUintN type coercion for bigint parameter",
            "info": """
                BigInt.asUintN ( bits, bigint )

                2. Let bigint ? ToBigInt(bigint).
            """,
            "features": ["BigInt"],
        },
        templates={
            '0n': 'assert.sameValue(BigInt.asUintN(2, %(value)s), 0n, %(message)s);',
            '1n': 'assert.sameValue(BigInt.asUintN(2, %(value)s), 1n, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { BigInt.asUintN(0, %(value)s); }, %(message)s);',
        },
        nominal_value_cases=[
            (10, 'assert.sameValue(BigInt.asUintN(3, %(value)s), 2n, %(message)s);'),
            (12345678901234567890003, 'assert.sameValue(BigInt.asUintN(4, %(value)s), 3n, %(message)s);'),
        ],
    )

    generate_tests(
        copyright_holder="Igalia, S.L",
        path_prefix="built-ins/DataView/prototype/getBigInt64/to-boolean-littleendian",
        conversion="ToBoolean",
        frontmatter={
            "esid": "sec-dataview.prototype.getbigint64",
            "description": "Boolean littleEndian argument coerced in ToBoolean",
            "info": """
                DataView.prototype.getBigInt64 ( byteOffset [ , littleEndian ] )

                1. Let v be the this value.
                2. If littleEndian is not present, let littleEndian be undefined.
                3. Return ? GetViewValue(v, byteOffset, littleEndian, "Int64").

                24.3.1.1 GetViewValue ( view, requestIndex, isLittleEndian, type )

                ...
                5. Set isLittleEndian to ToBoolean(isLittleEndian).
                ...
                12. Let bufferIndex be getIndex + viewOffset.
                13. Return GetValueFromBuffer(buffer, bufferIndex, type, false,
                "Unordered", isLittleEndian).

                24.1.1.6 GetValueFromBuffer ( arrayBuffer, byteIndex, type,
                isTypedArray, order [ , isLittleEndian ] )

                ...
                9. Return RawBytesToNumber(type, rawValue, isLittleEndian).

                24.1.1.5 RawBytesToNumber( type, rawBytes, isLittleEndian )

                ...
                2. If isLittleEndian is false, reverse the order of the elements of rawBytes.
                ...
            """,
            "features": ["DataView", "ArrayBuffer", "DataView.prototype.setUint8", "BigInt"],
        },
        preamble=(
            'var buffer = new ArrayBuffer(8);\n'
            'var sample = new DataView(buffer, 0);\n'
            'sample.setUint8(7, 0xff);\n'
            'assert.sameValue(sample.getBigInt64(0), 0xffn, "no argument");\n'
        ),
        templates={
            'false': 'assert.sameValue(sample.getBigInt64(0, %(value)s), 0xffn, %(message)s);',
            'true': 'assert.sameValue(sample.getBigInt64(0, %(value)s), -0x100000000000000n, %(message)s);',
        },
    )

    generate_tests(
        copyright_holder="Igalia, S.L",
        path_prefix="built-ins/DataView/prototype/getBigInt64/toindex-byteoffset",
        conversion="ToIndex",
        frontmatter={
            "esid": "sec-dataview.prototype.getbigint64",
            "description": "ToIndex conversions on byteOffset",
            "info": """
                DataView.prototype.getBigInt64 ( byteOffset [ , littleEndian ] )

                1. Let v be the this value.
                2. If littleEndian is not present, let littleEndian be undefined.
                3. Return ? GetViewValue(v, byteOffset, littleEndian, "Int64").

                24.3.1.1 GetViewValue ( view, requestIndex, isLittleEndian, type )

                ...
                4. Let getIndex be ? ToIndex(requestIndex).
                ...
            """,
            "features": ["DataView", "ArrayBuffer", "DataView.prototype.setUint8", "BigInt"],
        },
        preamble=(
            'var buffer = new ArrayBuffer(12);\n'
            'var sample = new DataView(buffer, 0);\n'
            'sample.setUint8(0, 0x27);\n'
            'sample.setUint8(1, 0x02);\n'
            'sample.setUint8(2, 0x06);\n'
            'sample.setUint8(3, 0x02);\n'
            'sample.setUint8(4, 0x80);\n'
            'sample.setUint8(5, 0x00);\n'
            'sample.setUint8(6, 0x80);\n'
            'sample.setUint8(7, 0x01);\n'
            'sample.setUint8(8, 0x7f);\n'
            'sample.setUint8(9, 0x00);\n'
            'sample.setUint8(10, 0x01);\n'
            'sample.setUint8(11, 0x02);\n'
        ),
        templates={
            '0': 'assert.sameValue(sample.getBigInt64(%(value)s), 0x2702060280008001n, %(message)s);',
            '1': 'assert.sameValue(sample.getBigInt64(%(value)s), 0x20602800080017fn, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { sample.getBigInt64(%(value)s); }, %(message)s);',
        },
        nominal_value_cases=[
            (2, 'assert.sameValue(sample.getBigInt64(%(value)s), 0x602800080017F00n, %(message)s);'),
            (3, 'assert.sameValue(sample.getBigInt64(%(value)s), 0x2800080017F0001n, %(message)s);'),
        ],
    )

    generate_tests(
        copyright_holder="Igalia, S.L",
        path_prefix="built-ins/DataView/prototype/getBigUint64/to-boolean-littleendian",
        conversion="ToBoolean",
        frontmatter={
            "esid": "sec-dataview.prototype.getbiguint64",
            "description": "Boolean littleEndian argument coerced in ToBoolean",
            "features": ["DataView", "ArrayBuffer", "DataView.prototype.setUint8", "BigInt"],
        },
        preamble=(
            'var buffer = new ArrayBuffer(8);\n'
            'var sample = new DataView(buffer, 0);\n'
            'sample.setUint8(7, 0xff);\n'
            'assert.sameValue(sample.getBigUint64(0), 0xffn, "no argument");\n'
        ),
        templates={
            'false': 'assert.sameValue(sample.getBigUint64(0, %(value)s), 0xffn, %(message)s);',
            'true': 'assert.sameValue(sample.getBigUint64(0, %(value)s), 0xff00000000000000n, %(message)s);',
        },
    )

    generate_tests(
        copyright_holder="Igalia, S.L",
        path_prefix="built-ins/DataView/prototype/getBigUint64/toindex-byteoffset",
        conversion="ToIndex",
        frontmatter={
            "esid": "sec-dataview.prototype.getbiguint64",
            "description": "ToIndex conversions on byteOffset",
            "features": ["DataView", "ArrayBuffer", "DataView.prototype.setUint8", "BigInt"],
        },
        preamble=(
            'var buffer = new ArrayBuffer(12);\n'
            'var sample = new DataView(buffer, 0);\n'
            'sample.setUint8(0, 0x27);\n'
            'sample.setUint8(1, 0x02);\n'
            'sample.setUint8(2, 0x06);\n'
            'sample.setUint8(3, 0x02);\n'
            'sample.setUint8(4, 0x80);\n'
            'sample.setUint8(5, 0x00);\n'
            'sample.setUint8(6, 0x80);\n'
            'sample.setUint8(7, 0x01);\n'
            'sample.setUint8(8, 0x7f);\n'
            'sample.setUint8(9, 0x00);\n'
            'sample.setUint8(10, 0x01);\n'
            'sample.setUint8(11, 0x02);\n'
        ),
        templates={
            '0': 'assert.sameValue(sample.getBigUint64(%(value)s), 0x2702060280008001n, %(message)s);',
            '1': 'assert.sameValue(sample.getBigUint64(%(value)s), 0x20602800080017fn, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { sample.getBigUint64(%(value)s); }, %(message)s);',
        },
        nominal_value_cases=[
            (2, 'assert.sameValue(sample.getBigUint64(%(value)s), 0x602800080017F00n, %(message)s);'),
            (3, 'assert.sameValue(sample.getBigUint64(%(value)s), 0x2800080017F0001n, %(message)s);'),
        ],
    )

    generate_tests(
        path_prefix="built-ins/String/prototype/indexOf/position-tointeger",
        conversion="ToInteger",
        frontmatter={
            "esid": "sec-string.prototype.indexof",
            "description": "String.prototype.indexOf type coercion for position parameter",
            "info": """
                String.prototype.indexOf ( searchString [ , position ] )

                4. Let pos be ? ToInteger(position).
            """,
        },
        templates={
            '0': 'assert.sameValue("aaaa".indexOf("aa", %(value)s), 0, %(message)s);',
            '1': 'assert.sameValue("aaaa".indexOf("aa", %(value)s), 1, %(message)s);',
            'Infinity': 'assert.sameValue("aaaa".indexOf("aa", %(value)s), -1, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { "".indexOf("", %(value)s); }, %(message)s);',
        },
        nominal_value_cases=[
            (2, 'assert.sameValue("aaaa".indexOf("aa", %(value)s), 2, %(message)s);'),
        ],
    )

    generate_tests(
        path_prefix="built-ins/String/prototype/indexOf/searchstring-tostring",
        conversion="ToString",
        frontmatter={
            "esid": "sec-string.prototype.indexof",
            "description": "String.prototype.indexOf type coercion for searchString parameter",
            "info": """
                String.prototype.indexOf ( searchString [ , position ] )

                3. Let searchStr be ? ToString(searchString).
            """,
        },
        templates={
            '': 'assert.sameValue("foo".indexOf(%(value)s), 0, %(message)s);',
            str: 'assert.sameValue("__%(expected_string_contents)s__".indexOf(%(value)s), 2, %(message)s);',
            "throws": 'assert.throws(%(error)s, function() { "".indexOf(%(value)s); }, %(message)s);',
        },
    )

if __name__ == "__main__":
    main()
