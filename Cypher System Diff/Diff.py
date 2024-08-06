import difflib
from pathlib import Path

'''
'''

print("")
print("Starting working of DIFF file")
print("")

first_file_lines = Path('CSRD_stare.txt').read_text(encoding="UTF-8").splitlines()
second_file_lines = Path('CSRD_nowe.txt').read_text(encoding="UTF-8").splitlines()

html_diff = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines)
Path('diff.html').write_text(html_diff, encoding="UTF-8")

html_diff = difflib.HtmlDiff().make_file(second_file_lines, first_file_lines)
Path('diff2.html').write_text(html_diff, encoding="UTF-8")

'''
with open("CSRD_stare.txt", "r", encoding="UTF-8") as f1:
    data1 = f1.read_text().splitlines()

with open("CSRD_nowe.txt", "r", encoding="UTF-8") as f2:
    data2 = f2.read_text().splitlines()

myHTML = difflib.HtmlDiff().make_file(data1, data2)

with open("CSRD_comp.html", "w", encoding="UTF-8") as ff:
    ff.write(myHTML)
'''

print("")
print("Finished working on DIFF file")
print("")

