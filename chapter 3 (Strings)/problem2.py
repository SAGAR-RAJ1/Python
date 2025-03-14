
# 2. Write a program to fill in a letter template given below with name and date.
# letter =
# Dear <|Name |>,
# You are selected!
# <|Date|>
# III

Letter = "Dear Harry, this python course is nice. Thanks!"

letter = '''Dear <|Name|>,
You are selected!
<|Date|>
IIT'''
print(letter.replace("<|Name|>","Harry").replace("<|Date|>","24 September 2050"))