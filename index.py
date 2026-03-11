from time import sleep
from playsound3 import playsound
import re

lyrics = """   Let it Happen.
[1] 3...
[1] 2...
[1] 1...
Made By inflames

I cannot vanish
You will not scared me
try to get through it
Try to push through it
(0.08) You were not thinking that i will not do it
They be loving someone and i'm another story
Take the next ticket
(0.08) Get the next train
Why would I do it?
Anyone'd think that
-
Let it happen
"""


def writeline(text):
  if not text.strip():
    print()
    return
  
  match1 = re.match(r'^\[(\d+)\]\s*(.*)', text)  # For [x], sleep x second and write all line
  match2 = re.match(r'^\((\d+\.?\d*)\)\s*(.*)', text)  # For (x), write a char and sleep x second
  if match1:
    sleep(int(match1.group(1)))
    print(match1.group(2))
  elif match2:
    for letter in match2.group(2):
      print(letter, end="", flush=True)
      sleep(float(match2.group(1)))
    print()
  else:
    for letter in text:
      print(letter, end="", flush=True)
      sleep(0.1)
    print()


playsound('letithappen.m4a', block=False)

for line in lyrics.splitlines():
  # print(line)
  writeline(line)