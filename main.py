# The Vacuum's Alibi entry: one deadpan line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: the vacuum grades the missed spot 9.7 out of 10 for clean and
# refuses to clean a 9.7 -- smug about its sensors, a specific number as
# the surprise turn, and the punch ("I have standards.") sitting at the end.
import os

LINE = "My sensors rated that spot 9.7 out of 10 for clean. I do not clean 9.7s. I have standards."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"
assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
