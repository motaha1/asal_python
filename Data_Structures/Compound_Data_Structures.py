x = {
    'hello':{
        1:'no'
,        2:'yes'
    } , 

    'welcome':{
        1:'no',
        2:'yes'
    }
}

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}


print(elements.get('hydrogen').get('number'))
print(elements["hydrogen"]["number"])