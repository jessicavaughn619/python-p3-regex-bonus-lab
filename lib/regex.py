import re

my_pattern = r"[A-Z][A-z]*'*[a-z]\s[a-z' ]*today*.*"
my_regex = re.compile(my_pattern)

