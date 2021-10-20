# SpellNumTH.py
"""
Function: to spell number by thai language
input type: positive integers
output type: string
limitation: digits up to 10^18
"""

def SpellNumTH(number):
    # Validate input number
    status = True
    while status:
        try:
            num = str(number)
            #! starting number must not be ZERO
            if num[0] == '0':
                raise Exception("Don't enter the number starting with ZERO.")
            #! numberic is a must
            if not num.isnumeric():
                raise Exception("Please enter only positive integers.")
        except Exception as e:
            print(e)
        else:
            num_len = len(num)
            status = False

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

    # Define place value
    place_value = {
        6:'ล้าน',
        5:'แสน',
        4:'หมื่น',
        3:'พัน',
        2:'ร้อย',
        1:'สิบ'
    }

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
    word_concat = ''.join(word_mapped)
    return word_concat + 'บาท'