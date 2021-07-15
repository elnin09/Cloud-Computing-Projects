#delimiters delimiters = " \t,;.?!-:@[](){}_*/"
import re
text = 'The {quick},brown\nfox jum[p]s*ove!r ?the laz&y;dog.\nline-cha:n@ge'
print re.split(';|,|\*|\n|\s|\t|;|\.|\?|!|-|:|@|\[|\]|\(|\)|\{|\}|_|&',text)