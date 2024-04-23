n = int(input())

spisok = ["/" * n for e in range(n)]

# print(spisok)

for str_index, stroka in enumerate(spisok):
    for smb_index, symbol in enumerate(stroka):
        if str_index == smb_index:
            stroka = list(stroka)
            stroka[smb_index] = "\\"
            stroka = "".join(stroka)
            print(stroka)                       

         

        
    


