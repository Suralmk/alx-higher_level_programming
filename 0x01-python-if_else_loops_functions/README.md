## 0x01-python-if_else_loops_functions
# conditional statments
# loops
# Functions 
<hr>
![code](https://github.com/Suralmk/alx-higher_level_programming/assets/104755355/4d500d89-78dc-4ae4-9846-46c0b8543dd4)
<hr>

<h3>if statment</h3>
<p>There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.</p>

<p>
x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
--------------
More
</p>

<h3>Loop</h3>
<p>The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):</p>

<p>
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
-------------
cat 3
window 6
defenestrate 12</p>
