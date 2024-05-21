import re

phone_num_regex = re.compile(r"\+(\d\d\d)-(\d\d\d\d\d\d\d\d\d\d)")
my_number = phone_num_regex.search("My phone number is +977-9876543210.")

print(my_number.group())
print(my_number.group(1))
print(my_number.group(2))

country_code, phone_number = my_number.groups()
print(country_code, phone_number)

influencer_regex = re.compile(r"Hamza Ahmed|Mark Manson|Iman Gandzi")
influencer = influencer_regex.search(
    "The self help media is run by Mark Manson, Hamza Ahmed and Iman Gandzi on YouTube."
)
print(influencer.group())

bat_regex = re.compile(r"Bat(man|mobile|ball)")
batman = bat_regex.search("Have you seen Batman? I have to ask him to play Batball!")
print(batman.group())

business_regex = re.compile(r"Business(wo)?man")
business = business_regex.search("I am a businessman and she is a Businesswoman.")
print(business.group())

target_regex = re.compile(r"(Ta)*rget")

target = target_regex.search("Target")
print(target.group())

target = target_regex.search("TaTaTarget")
print(target.group())

target = target_regex.search("rget")
print(target.group())


target_regex = re.compile(r"(Ta)+rget")

target = target_regex.search("Target")
print(target.group())

target = target_regex.search("TaTaTarget")
print(target.group())

target = target_regex.search("rget")
print(f"Nothing: {target is None}")

ha_regex = re.compile(r"(Ha){3}")
ha = ha_regex.search("HaHaHa")
print(ha.group())

ha_regex = re.compile(r"(Ha){3,}")
ha = ha_regex.search("HaHaHaHaHaHaHa")
print(ha.group())

ha_regex = re.compile(r"(Ha){3,5}")
ha = ha_regex.search("HaHaHaHaHaHaHa")  # GREEDY
print(ha.group())

ha_regex = re.compile(r"(Ha){3,5}?")
ha = ha_regex.search("HaHaHaHaHaHaHa")  # NON-GREEDY
print(ha.group())

help_regex = re.compile(r"HELP")
print(help_regex.findall("HELP ME!! I SAID HELP MEE!!! I AM DYING! PLEASE HELP MEE!!"))

vowel_regex = re.compile(r"[aeiouAEIOU]")
print(vowel_regex.findall("A quick brown fox jumps over the lazy dog."))

vowel_regex = re.compile(r"[^aeiouAEIOU]")
print(vowel_regex.findall("A quick brown fox jumps over the lazy dog."))


whole_string_is_num = re.compile(r"^\d+$")
print(whole_string_is_num.search("1234567890"))
print(whole_string_is_num.search("12345xyz67890") is None)
print(whole_string_is_num.search("12 34567890") is None)

cream_regex = re.compile(r".cream")
cream = cream_regex.findall("I scream, You scream, We all scream for Ice-cream.")
print(cream)
