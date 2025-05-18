midiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
midiccionario["Portugal"]="Lisboa"
print(midiccionario["Francia"])
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))


mitupla1=["China","Japon"]
midiccionario1={mitupla1[0]:"Beijing",mitupla1[1]:"Tokio"}
print(midiccionario1)
print(midiccionario1["China"])
print(len(midiccionario1))