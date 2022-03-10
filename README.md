# Spelling Number Project

## Description
This project is developed for learning and practicing Python.\
Developing this projects as a function for spelling number with natural language in thai language.
Moreover, this function able to play its voice.

## Prerequisites
This project is built with python3 and thier libraries as follows
- gtts
- os

## Usage
```python
# import SpellNumTH for spelling number and Playvoice for playing voice
from SpellNumTH import SpellNumTH, PlayVoice

# input number
num = 81000121.456

# get the result
result = SpellNumTH(num)

# show the result
print(result)

# play vocie
PlayVoice(result)
```

## Key Learning
- Validation of user input by try-except keyword
- Logic how to naturally spell the number in thai language
- Usage of map and lambda together
- Usage of gtts library
 

## License
[MIT](https://choosealicense.com/licenses/mit/)
