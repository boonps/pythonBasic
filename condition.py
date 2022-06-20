# def greeting(lang):
#     if lang == "th":
#         print("sawadee")
#     elif lang == "en":
#         print("hello")
#     elif lang == "jp":
#         print("hi!")
#     else:
#         print("bye")
#
# greeting("en")

def greet_req(eng,interview,math):
    if eng == 30 and interview > 80 and math < 50:
        return True
    else:
        return False

print(greet_req(30,81,40))