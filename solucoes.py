def sao_anagramas(string1, string2):  
    
  s1 = string1.replace(" ", "").lower()
  s2 = string2.replace(" ", "").lower()
    
    
  return sorted(s1) == sorted(s2)



print(sao_anagramas("amor", "roma"))         
print(sao_anagramas("coração", "roca cão"))  
print(sao_anagramas("carro", "corar"))       
print(sao_anagramas("fato", "tofa"))         
print(sao_anagramas("rio", "ior"))           
print(sao_anagramas("gato", "cabra"))        
print(sao_anagramas("banana", "ananás"))     
print(sao_anagramas("pedra", "perda"))       
print(sao_anagramas("escola", "colesa"))

def cifra_de_cesar(texto, deslocamento):
  # TODO
  pass

def valida_cpf(cpf_string):
  # TODO
  pass