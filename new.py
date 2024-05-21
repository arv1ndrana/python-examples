def parseInt(number):
    one_to_nine = ["one", "two", "three", "four",
                   "five", "six", "seven", "eight", "nine",]
    ten_to_nineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                       "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twenty_to_ninety = ["twenty", "thirty", "forty",
                        "fifty", "sixty", "seventy", "eighty", "ninety"]

    one_to_nine_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ten_to_nineteen_digits = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    twenty_to_ninety_digits = [20, 30, 40, 50, 60, 70, 80, 90]

    hundred = 100
    thousand = 1000
    million = 1000000

    number = number.replace("-", "")
    number_list = number.split()
    lst = [item for item in number_list if not item == "and"]

    print(lst)

    result = 0
    
    while lst:

        if len(lst) >= 3:
            if lst[0] in one_to_nine and lst[1] == "hundred" and lst[2] == "million":
                result += one_to_nine_digits[one_to_nine.index(lst[0])] * hundred * million
                del lst[:3]
                
            elif lst[0] in one_to_nine and lst[1] == "hundred" and lst[2] == "thousand":
                result += one_to_nine_digits[one_to_nine.index(lst[0])] * hundred * thousand
                del lst[:3]

        elif len(lst) >= 2:

            if lst[0] in one_to_nine and lst[1] == "million":
                result += one_to_nine_digits[one_to_nine.index(lst[0])] * million
                del lst[:2]

            elif lst[0] in ten_to_nineteen and lst[1] == "million":
                result += ten_to_nineteen_digits[ten_to_nineteen.index(lst[0])] * million
                del lst[:2]

            elif lst[0] in one_to_nine and lst[1] == "thousand":
                result += one_to_nine_digits[one_to_nine.index(lst[0])] * thousand
                del lst[:2]

            elif lst[0] in ten_to_nineteen and lst[1] == "thousand":
                result += ten_to_nineteen_digits[ten_to_nineteen.index(lst[0])] * thousand
                del lst[:2]

            elif lst[0] in one_to_nine and lst[1] == "hundred":
                result += one_to_nine_digits[one_to_nine.index(lst[0])] * hundred
                del lst[:2]
        else:
            if lst[0] in one_to_nine:
                result += one_to_nine_digits[one_to_nine.index(lst[0])]
                del lst[:1]
            elif lst[0] in ten_to_nineteen:
                result += ten_to_nineteen_digits[ten_to_nineteen.index(lst[0])]
                del lst[:1]

    return result
