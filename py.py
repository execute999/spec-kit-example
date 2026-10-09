
codes = ["dsa", "abc" , "qet", "abc dsad"]
codes = [code.replace(" ", "") for code in codes]



'''

old code:

codes = ["dsa", "abc" , "qet", "abc dsad"]

for code in codes : 
    if " " in code :
        assert(False)


prompt:

/speckit-specify modify py.py file to remove spaces for each element in the 'codes' list instead of theow an assert.

'''