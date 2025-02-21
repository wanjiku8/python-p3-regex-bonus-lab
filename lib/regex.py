import re

my_pattern = r""
my_regex = re.compile(r"It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.")
# my_regex = re.compile(my_pattern)


def match_string(text):
    pattern = r"It's such a lovely day today\."
    return re.fullmatch(pattern, text)

def match_alternate_string(text):
    pattern = r"(Hello, world!|Python is fun!|Regex is powerful.)"
    return re.fullmatch(pattern, text)

def find_matching_strings(text_list):
    pattern = r"(Hello, world!|Python is fun!|Regex is powerful.)"
    return re.findall(pattern, " ".join(text_list))
