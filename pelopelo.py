import converter

p = input("'.'に当てはめたい文字列を入力:")
h = input("'-'に当てはめたい文字列を入力:")
s = input("区切り文字を入力:")

context = input(p + h + p + h +"語に変換したい文字列を入力(日本語可):")
result = converter.convert(context)
print(result.replace(".",p).replace("-",h).replace(" ",s))