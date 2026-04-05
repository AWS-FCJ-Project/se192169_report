import glob
import re

BASE = r"D:\se192169_report\content\1-Worklog"

mapping = {
    "2": "Thứ hai",
    "3": "Thứ ba",
    "4": "Thứ tư",
    "5": "Thứ năm",
    "6": "Thứ sáu",
    "7": "Thứ bảy",
    "CN": "Chủ Nhật",
}

pattern = re.compile(r"\|\s*(2|3|4|5|6|7|CN)\s*\|")

def repl(match):
    key = match.group(1)
    return "| " + mapping.get(key, key) + " |"

for path in glob.glob(BASE + r"\1.*-Week*\_index.vi.md"):
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    new = pattern.sub(repl, txt)
    if new != txt:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
