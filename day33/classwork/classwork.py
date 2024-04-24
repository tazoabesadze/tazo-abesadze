# def to_weird_case(words):
#     words = words.split(" ")
    
#     res_list = []
    
#     for word in words:
#         modified_str = ""
        
#         for i in range(len(word)):
#             if i %2 == 0:
#                 modified_str += word[i].upper()
#             else:
#                 modified_str += word[i].lower()
        
#         res_list.append(modified_str)
        
#     return " ".join(res_list)



# def camel_case(str):
#     res_list = []
    
#     str = str.split(" ")
    
#     for word in str:
#         res_list.append(word.capitalize())
        
#     return "".join(res_list)



# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         is_valid = True
        
#         numbers = "0123456789"
        
#         for i in pin:
#             if i not in numbers:
#                 is_valid = False
                
#         return is_valid
#     return False