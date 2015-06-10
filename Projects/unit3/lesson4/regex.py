import re

strings = (r'these', r"are", r'''all''', r"""strings""")
match_all_characters = r'.'
#DOTALL does not stop at the newline character
print re.match(r'.*', 'az09_&^%$\nfoo', re.DOTALL).group()
