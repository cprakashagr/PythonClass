

'''
Notes:
uses a '\' to indicate the special forms or to indicate special characters without invoking their meaning.

Python's raw string pattern --> is prefixed with 'r'. Ex: ---r"\n"---  for string match for \n. ---"\n"---
for string match for new line.

RE Syntax.

com  = re.compile('re literals');
result = com.find('bigstring');
# finds from the beginning only till the first match

result = com.search('bigstring');
# finds from anywhere in the string till the first match


-->>    result.group();     # matching string
        result.start();     # start index
        result.end();       # end index
        result.span();      # start and the end indices

result = com.findall('bigstring');
# finds all the occurances and returns a list of all the matching strings.

result = com.finditer('bigstring');
# finds all the occurances and returns an object as an iterator.

result = com.find('bigstring');


'''

import re


def main():
    p = re.compile('ab')
    print(p.match(''))
    pass

if __name__ == "__main__":
    main()
