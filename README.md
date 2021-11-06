# SpellNumTH
SpellNumTH is a function for spelling number by thai language and playing its voice.

## Technologies
- Python 3.8
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

## License
[MIT](https://choosealicense.com/licenses/mit/)
