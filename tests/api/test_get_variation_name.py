# Copyright 2019-2021 Wingify Software Pvt. Ltd.
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

from __future__ import print_function
import unittest
import json
import random
import mock

import vwo
from ..data.settings_files import SETTINGS_FILES
from ..data.settings_file_and_user_expectations import USER_EXPECTATIONS

from ..config.config import TEST_LOG_LEVEL


class GetVariationNameTest(unittest.TestCase):
    def set_up(self, config_variant="AB_T_50_W_50_50"):
        self.user_id = str(random.random())
        self.settings_file = json.dumps(SETTINGS_FILES.get(config_variant))

        self.vwo = vwo.launch(self.settings_file, is_development_mode=True, log_level=TEST_LOG_LEVEL)
        self.campaign_key = config_variant
        try:
            self.goal_identifier = SETTINGS_FILES[config_variant]["campaigns"][0]["goals"][0]["identifier"]
        except Exception:
            pass

    # Test get_variation_name
    def test_get_variation_name_invalid_params(self):
        self.set_up()
        self.assertIsNone(self.vwo.get_variation_name(123, 456))

    def test_get_variation_name_with_no_campaign_key_found(self):
        self.set_up("AB_T_50_W_50_50")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertIs(self.vwo.get_variation_name("NO_SUCH_CAMPAIGN_KEY", test["user"]), None)

    def test_get_variation_name_wrong_campaign_type_passed(self):
        self.set_up("FR_T_0_W_100")
        result = self.vwo.get_variation_name("FR_T_0_W_100", "user")
        self.assertIs(result, None)

    def test_get_variation_name_against_campaign_traffic_50_and_split_50_50(self):
        self.set_up("AB_T_50_W_50_50")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertEqual(self.vwo.get_variation_name(self.campaign_key, test["user"]), test["variation"])

    def test_get_variation_name_against_campaign_traffic_100_and_split_50_50(self):
        self.set_up("AB_T_100_W_50_50")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertEqual(self.vwo.get_variation_name(self.campaign_key, test["user"]), test["variation"])

    def test_get_variation_name_against_campaign_traffic_100_and_split_20_80(self):
        self.set_up("AB_T_100_W_20_80")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertEqual(self.vwo.get_variation_name(self.campaign_key, test["user"]), test["variation"])

    def test_get_variation_name_against_campaign_traffic_20_and_split_10_90(self):
        self.set_up("AB_T_20_W_10_90")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertEqual(self.vwo.get_variation_name(self.campaign_key, test["user"]), test["variation"])

    def test_get_variation_name_against_campaign_traffic_100_and_split_0_100(self):
        self.set_up("AB_T_100_W_0_100")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertEqual(self.vwo.get_variation_name(self.campaign_key, test["user"]), test["variation"])

    def test_get_variation_name_against_campaign_traffic_100_and_split_33_x3(self):
        self.set_up("AB_T_100_W_33_33_33")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertEqual(self.vwo.get_variation_name(self.campaign_key, test["user"]), test["variation"])

    def test_get_variation_name_against_campaign_traffic_75_and_split_10_TIMES_10(self):
        self.set_up("T_75_W_10_TIMES_10")
        for test in USER_EXPECTATIONS[self.campaign_key]:
            self.assertEqual(self.vwo.get_variation_name(self.campaign_key, test["user"]), test["variation"])

    # test api raises exception
    # mock.patch referenced from https://stackoverflow.com/a/19107511
    def test_get_variation_name_raises_exception(self):
        with mock.patch("vwo.helpers.validate_util.is_valid_string", side_effect=Exception("Test")):
            self.set_up()
            self.assertIs(None, self.vwo.get_variation_name("SOME_CAMPAIGN", "USER"))

    def test_get_variation_name_with_no_custom_variables_fails(self):
        vwo_instance = vwo.launch(
            json.dumps(SETTINGS_FILES.get("T_50_W_50_50_WS")), log_level=TEST_LOG_LEVEL, is_development_mode=True
        )
        for test in USER_EXPECTATIONS.get("AB_T_50_W_50_50"):
            self.assertEquals(vwo_instance.get_variation_name("T_50_W_50_50_WS", test["user"]), None)

    def test_get_variation_name_with_no_dsl_remains_unaffected(self):
        vwo_instance = vwo.launch(
            json.dumps(SETTINGS_FILES.get("T_50_W_50_50_WS")), log_level=TEST_LOG_LEVEL, is_development_mode=True
        )
        true_custom_variables = {"a": 987.1234, "hello": "world"}
        for test in USER_EXPECTATIONS.get("AB_T_50_W_50_50"):
            self.assertEquals(
                vwo_instance.get_variation_name(
                    "T_50_W_50_50_WS", test["user"], custom_variables=true_custom_variables
                ),
                test["variation"],
            )

    def test_get_variation_name_with_presegmentation_true(self):
        vwo_instance = vwo.launch(
            json.dumps(SETTINGS_FILES.get("T_100_W_50_50_WS")), log_level=TEST_LOG_LEVEL, is_development_mode=True
        )
        true_custom_variables = {"a": 987.1234, "hello": "world"}
        for test in USER_EXPECTATIONS.get("AB_T_100_W_50_50"):
            self.assertEquals(
                vwo_instance.get_variation_name(
                    "T_100_W_50_50_WS", test["user"], custom_variables=true_custom_variables
                ),
                test["variation"],
            )

    def test_get_variation_name_with_presegmentation_false(self):
        vwo_instance = vwo.launch(
            json.dumps(SETTINGS_FILES.get("T_100_W_50_50_WS")), log_level=TEST_LOG_LEVEL, is_development_mode=True
        )
        false_custom_variables = {"a": 987123, "world": "hello"}
        for test in USER_EXPECTATIONS.get("AB_T_100_W_50_50"):
            self.assertEquals(
                vwo_instance.get_variation_name(
                    "T_100_W_50_50_WS", test["user"], custom_variables=false_custom_variables
                ),
                None,
            )

    def test_get_variation_name_against_T_100_W_33_33_33_WS_WW_None(self):
        vwo_client_instance = vwo.launch(
            json.dumps(SETTINGS_FILES.get("T_100_W_33_33_33_WS_WW")), log_level=TEST_LOG_LEVEL, is_development_mode=True
        )
        false_variation_targeting_variables = {"chrome": "true", "safari": "false", "browser": "firefox 106.69"}
        false_custom_variables = {
            "contains_vwo": "legends say that vwo is the best",
            "regex_for_no_zeros": 1223123,
            "regex_for_all_letters": "dsfASF",
            "regex_for_small_letters": "sadfksjdf",
            "regex_real_number": 12321.2242,
            "regex_for_zeros": 0,
            "is_equal_to": "!equal_to_variable",
            "contains": "contains_variable",
            "regex_for_capital_letters": "SADFLSDLF",
            "is_not_equal_to": "is_not_equal_to_variable",
            "this_is_regex": "this    is    regex",
            "starts_with": "starts_with_variable",
        }
        for test in USER_EXPECTATIONS.get("AB_T_100_W_33_33_33"):
            self.assertIs(
                vwo_client_instance.get_variation_name(
                    "T_100_W_33_33_33_WS_WW",
                    test["user"],
                    custom_variables=false_custom_variables,
                    variation_targeting_variables=false_variation_targeting_variables,
                ),
                None,
            )

    def test_get_variation_name_against_T_100_W_33_33_33_WS_WW(self):
        vwo_client_instance = vwo.launch(
            json.dumps(SETTINGS_FILES.get("T_100_W_33_33_33_WS_WW")), log_level=TEST_LOG_LEVEL, is_development_mode=True
        )
        true_variation_targeting_variables = {"chrome": "false", "safari": "true", "browser": "chrome 107.107"}
        true_custom_variables = {
            "contains_vwo": "legends say that vwo is the best",
            "regex_for_no_zeros": 1223123,
            "regex_for_all_letters": "dsfASF",
            "regex_for_small_letters": "sadfksjdf",
            "regex_real_number": 12321.2242,
            "regex_for_zeros": 0,
            "is_equal_to": "equal_to_variable",
            "contains": "contains_variable",
            "regex_for_capital_letters": "SADFLSDLF",
            "is_not_equal_to": "is_not_equal_to_variable",
            "this_is_regex": "this    is    regex",
            "starts_with": "starts_with_variable",
        }
        for test in USER_EXPECTATIONS.get("AB_T_100_W_33_33_33"):
            self.assertEquals(
                vwo_client_instance.get_variation_name(
                    "T_100_W_33_33_33_WS_WW",
                    test["user"],
                    custom_variables=true_custom_variables,
                    variation_targeting_variables=true_variation_targeting_variables,
                ),
                test["variation"],
            )
