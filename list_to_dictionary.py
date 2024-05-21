def list_to_dictionary(key_list, value_list):
   dictionary = {}
   if len(key_list) == len(value_list):
      for key,value in zip(key_list,value_list):
         dictionary.update({key:value})
      return dictionary
   else:
      return "Please provide equal keys and value to be put in the dictionary"

key_list = ["Apple","Banana","Mango"]
value_list = ["A","B","M"] 

result = list_to_dictionary(key_list, value_list)
print(result)
