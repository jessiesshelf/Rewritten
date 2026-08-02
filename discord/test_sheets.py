import gspread

gs = gspread.service_account(r'D:\Coders\rewritten\rewritten-504216-8ed7e75237c4.json')
sheet = gs.open("Rewritten Fichas").worksheet("Miller")
print(sheet.get("I8:I13"))