name=input("name")
date=input("date")
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
letter=letter.replace("<|Name|>",name).replace("<|Date|>",date)
print(letter)