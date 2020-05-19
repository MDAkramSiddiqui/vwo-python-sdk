# Copyright 2019-2020 Wingify Software Pvt. Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
import json
from vwo.services.segmentor.segment_evaluator import SegmentEvaluator

with open("tests/data/segmentor_test_cases.json") as json_file:
    segmentor_test_cases = json.load(json_file)


class TestContainsOperand(unittest.TestCase):
    def setUp(self):
        self.segment_evaluator = SegmentEvaluator()
        self.test_cases = segmentor_test_cases.get("contains_operand")

    def test_incorrect_key(self):
        test_case = self.test_cases.get("incorrect_key")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_incorrect_key_case(self):
        test_case = self.test_cases.get("incorrect_key_case")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_single_char(self):
        test_case = self.test_cases.get("single_char")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_case_mismatch(self):
        test_case = self.test_cases.get("case_mismatch")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_char_data_type(self):
        test_case = self.test_cases.get("char_data_type")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_prefix_match(self):
        test_case = self.test_cases.get("prefix_match")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_boolean_data_type(self):
        test_case = self.test_cases.get("boolean_data_type")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_part_of_text(self):
        test_case = self.test_cases.get("part_of_text")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_null_value_provided(self):
        test_case = self.test_cases.get("null_value_provided")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_upper_case(self):
        test_case = self.test_cases.get("upper_case")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_no_value_provided(self):
        test_case = self.test_cases.get("no_value_provided")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_suffix_match(self):
        test_case = self.test_cases.get("suffix_match")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_boolean_data_type2(self):
        test_case = self.test_cases.get("boolean_data_type2")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_float_data_type(self):
        test_case = self.test_cases.get("float_data_type")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_numeric_data_type_mismatch(self):
        test_case = self.test_cases.get("numeric_data_type_mismatch")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_contains_match(self):
        test_case = self.test_cases.get("contains_match")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_char_data_type_case_mismatch2(self):
        test_case = self.test_cases.get("char_data_type_case_mismatch2")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_special_characters(self):
        test_case = self.test_cases.get("special_characters")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_stringified_float(self):
        test_case = self.test_cases.get("stringified_float")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_char_data_type_case_mismatch(self):
        test_case = self.test_cases.get("char_data_type_case_mismatch")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_boolean_data_type_mismatch2(self):
        test_case = self.test_cases.get("boolean_data_type_mismatch2")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_numeric_data_type_mismatch2(self):
        test_case = self.test_cases.get("numeric_data_type_mismatch2")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_spaces(self):
        test_case = self.test_cases.get("spaces")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_mismatch(self):
        test_case = self.test_cases.get("mismatch")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_exact_match(self):
        test_case = self.test_cases.get("exact_match")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_numeric_data_type(self):
        test_case = self.test_cases.get("numeric_data_type")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_boolean_data_type_mismatch(self):
        test_case = self.test_cases.get("boolean_data_type_mismatch")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_missingkey_value(self):
        test_case = self.test_cases.get("missingkey_value")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_case_mismatch2(self):
        test_case = self.test_cases.get("case_mismatch2")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )

    def test_contains_operand_falsy_with_special_character(self):
        test_case = self.test_cases.get("contains_operand_falsy_with_special_character")
        self.assertIs(
            self.segment_evaluator.evaluate(test_case.get("dsl"), test_case.get("custom_variables")),
            test_case.get("expectation"),
        )
