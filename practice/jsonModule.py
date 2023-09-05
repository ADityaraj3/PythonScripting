import json

data = '''
{
    "people": [
        {
            "name": "Aditya",
            "email": ["adityasraj123@gmail.com", "aarohesrivastava123@gmail.com"],
            "married": false
        },
        {
            "name": "Aarohee",
            "email": ["adityasraj123@gmail.com", "aarohesrivastava123@gmail.com"],
            "married": false
        }
    ]
}
'''

print(data)

pydata = json.loads(data)
print(pydata)

