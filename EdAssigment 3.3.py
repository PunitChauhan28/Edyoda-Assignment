def string_test(str1):
    dict2={"Upper_case":0,"Lower_case":0}
    for k in str1:
        if k.isupper():
            dict2["Upper_case"]+=1
        elif k.islower():
            dict2["Lower_case"]+=1
        else:
            pass
    print("Original string",str1)
    print("upper_case:",dict2["Upper_case"])
    print("Lower_case:",dict2["Lower_case"])

string_test("heLLo")




