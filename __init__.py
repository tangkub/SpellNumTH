# SpellNumTH.py
"""
Function: To spell number and play its voice by thai language
input type: int or float
output type: string
limitation: 18 digits and 2 decimal places
"""

# Import module for playing voice
from gtts import gTTS
import os



# Function: number to text
def SpellNumTH(number):

    # Validate input number
    try:
        num = number
        #! numeric is a must
        if not (isinstance(num, int) or isinstance(num, float)):
            raise Exception("Please enter only number.")
        #! <= 18 digits
        if len(str(num).split(".")[0]) >= 18:
            raise Exception("Please enter the number less than 18 digits")
    except Exception as e:
        print(e)
        return None

    # Define number spelling
    spelling = {
        '0':'',
        '1':'หนึ่ง',
        '2':'สอง',
        '3':'สาม',
        '4':'สี่',
        '5':'ห้า',
        '6':'หก',
        '7':'เจ็ด',
        '8':'แปด',
        '9':'เก้า'
    }

    # Define number spelling for float number
    spelling_float = {
        '0':'ศูนย์',
        '1':'หนึ่ง',
        '2':'สอง',
        '3':'สาม',
        '4':'สี่',
        '5':'ห้า',
        '6':'หก',
        '7':'เจ็ด',
        '8':'แปด',
        '9':'เก้า'
    }

    # Define place value
    place_value = {
        6:'ล้าน',
        5:'แสน',
        4:'หมื่น',
        3:'พัน',
        2:'ร้อย',
        1:'สิบ'
    }

    # Split float number
    float_state = False
    if isinstance(num, float):
        float_state = True
        num = round(num, 2)
        num = str(num)
        num_float = num.split(".")[1] # get float number
        num = num.split(".")[0] # get integer number

        # find number spelling for float number
        num_float_spell = ['จุด']
        for i in num_float:
            num_float_spell.append(spelling_float[i])

    num = str(num)
    num_len = len(num)

    # Find place value and number of each digit
    num_place_value = []
    num_spell = []
    for i in range(num_len, 0, -1):
        # create list of number spelling
        num_spell.append(spelling[num[i-1]])
        # create list of place value
        if i-1 == 0:
            num_place_value.append('')
        else:
            if (i-1)%6 == 0:
                num_place_value.append(place_value[6])
            elif (i-1)%6 == 5:
                num_place_value.append(place_value[5])
            elif (i-1)%6 == 4:
                num_place_value.append(place_value[4])
            elif (i-1)%6 == 3:
                num_place_value.append(place_value[3])
            elif (i-1)%6 == 2:
                num_place_value.append(place_value[2])
            elif (i-1)%6 == 1:
                num_place_value.append(place_value[1])
            else:
                print('something wrong')

    # Remove place value by number spelling is none
    num_place_value.reverse()
    for i in range(num_len):
        # case: less than 1 million
        if i < 6 and num_spell[i] == '':
            num_place_value[i] = ''
        # case: more than 1 million and less than 1 trillion
        if i > 6 and i < 12 and num_spell[i] == '':
            num_place_value[i] = ''
        # case: more than 1 trillion
        if i > 12 and num_spell[i] == '':
            num_place_value[i] = ''
    num_place_value.reverse()
    num_spell.reverse()

    # Modify specific number
    for n in range(2, num_len+1, 6):
        # case: 2nd digit has number and ending with '1'
        if num_spell[-n] != spelling['0'] and  num_spell[-n+1] == spelling['1']:
            num_spell[-n+1] = 'เอ็ด'
        # case: '1' at ten
        if num_spell[-n] == spelling['1']:
            num_spell[-n] = ''
        # case: '2' at ten
        if num_spell[-n] == spelling['2']:
            num_spell[-n] = 'ยี่'

    # Final result
    word_mapped = list(map(lambda x,y: x+y, num_spell, num_place_value))
    if float_state:
        word_mapped.extend(num_float_spell)
    word_concat = ''.join(word_mapped)
    return word_concat + 'บาท'



# Function: text to speech
def PlayVoice(text, language='th'):
    text = text
    language = language
    voice = gTTS(text=text, lang=language, slow=False)
    voice.save('voice.mp3')
    os.system("start voice.mp3")