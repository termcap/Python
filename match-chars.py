import re
print(bool(re.match('^[a-zA-Z0-9.\-_()\\\]+$', r'\2022\01\path-to_file(GRE)-v.1')))
print(bool(re.match('^[1234]+$', '123')))
