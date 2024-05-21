def generate_hashtag(s):
    s_list = s.split()
    s_list_capitalized = [string.title() for string in s_list]
    final_result = "".join(s_list_capitalized)
    final_result_length = len(final_result)

    return "#" + final_result if final_result_length > 0 and final_result_length < (140 + 1) else False

foo = "Hi! My name is Slim Shady"
one = ""
another_one = "asldf ldajsdklf ksdfkl asdfhl asdjfk fh askdfhkjhsdkfkasdjfkldlj ldjfklasdj flasdjfsjf lsdfj ldjf ldjf lfkaf ldjf lkasdjflk sjdfkl sjdklf asdjf ldjfkl djfl ajsdfl jsdlkfj sdklfj sdf ladjfdj fksdjf kasdjf asdkfjklasdfhasdjfhasdkfhasdkfj ksadjfklf ljd fkajsdfuisdfuasdfiuasdhyfiuasdiufhasduifashfjkasdfjkdfjhasdjkfhafjhasdfasdjfkhsadjkfhajksdfhasdjkfhasdjkfhajsdkfhasdjkfhsdjkfhasd"



print(generate_hashtag(foo))
print(generate_hashtag(oe))
print(generate_hashtag(another_one))
