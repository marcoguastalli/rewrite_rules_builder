import os
import re
from pathlib import Path

from rewrite_rules_builder_constants import INPUT_FILE_NAME_WITH_PATTERNS
from rewrite_rules_builder_constants import INPUT_FILE_NAME_WITH_SUBSTITUTIONS
from rewrite_rules_builder_constants import OUTPUT_FILE_NAME_WITH_REWRITE_RULES
from rewrite_rules_builder_constants import REWRITE_RULE
from rewrite_rules_builder_constants import REWRITE_RULE_FLAGS
from python_commons import read_file_to_list_of_string
from python_commons import write_strings_to_path_file_name
from python_commons import is_blank
from python_commons import string_strip


def validate_rewrite_rule(rule):
    try:
        re.compile(rule)
        return True
    except re.error:
        return False


def generate_rewrite_rules(patterns, substitutions):
    output_array = []
    for i in range(len(patterns)):
        rule = f"{REWRITE_RULE}{string_strip(patterns[i])}$ {string_strip(substitutions[i])} {REWRITE_RULE_FLAGS}\n"
        output_array.append(rule)

    return output_array


def main(input_file_name_with_patterns: str, input_file_name_with_substitutions: str):
    patterns = []
    substitutions = []
    file_content_patterns = read_file_to_list_of_string(input_file_name_with_patterns)
    file_content_substitutions = read_file_to_list_of_string(input_file_name_with_substitutions)
    for line in file_content_patterns:
        if not is_blank(line) and line != "\n":
            patterns.append(line)
    for line in file_content_substitutions:
        if not is_blank(line) and line != "\n":
            substitutions.append(line)

    if len(patterns) != len(substitutions):
        return "Warning: The size of both arrays must be the same."

    rewrite_rules = generate_rewrite_rules(patterns, substitutions)

    invalid_rules = []
    for rule in rewrite_rules:
        if not validate_rewrite_rule(rule):
            invalid_rules.append(rule)

    if invalid_rules:
        print("Invalid rewrite rules found:")
        for rule in invalid_rules:
            print(rule)
    else:
        print("All rewrite rules are valid.")

    write_strings_to_path_file_name(rewrite_rules, OUTPUT_FILE_NAME_WITH_REWRITE_RULES)
    pass


if __name__ == "__main__":
    main(INPUT_FILE_NAME_WITH_PATTERNS, INPUT_FILE_NAME_WITH_SUBSTITUTIONS)
