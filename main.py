# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import re

get_char = r"([\w )\[\]*,\(]+): ([\w\?, '.\-\"\!\[\]]*)"
get_actions = r"(\[(?:\w+| )*\](?:\.)?)"
get_pt = r"(\[[^\]]*\](\.|))"
test_str = open('script.txt', 'r').read()

matches = re.finditer(get_char, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
    actions = re.findall(get_actions,match.group(2),re.DOTALL)
    lines = re.sub(get_pt,'',match.group(2))
    lines = re.sub(r"\s\s",' ',lines)
    lines = re.sub(r"\.[^ ]",'. ',lines)
    lines = re.sub(r"^ ",'',lines)
    print("lines",lines)
    print("actions",actions)
    match.group()
