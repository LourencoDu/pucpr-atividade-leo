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

def cifra_de_cesar(texto, deslocamento):
    resultado = ""

    for char in texto:
        if char.isalpha():  # só mexe se for letra
            base = ord('A') if char.isupper() else ord('a')
            # desloca dentro do alfabeto de 26 letras
            nova_pos = (ord(char) - base + deslocamento) % 26 + base
            resultado += chr(nova_pos)
        else:
            resultado += char  # mantém espaços, números, pontuação

    return resultado
print(cifra_de_cesar("abc", 2))  
# cde

print(cifra_de_cesar("xyz", 3))  
# abc

print(cifra_de_cesar("Ataque ao Amanhecer!", 5))  
# Fyfvzj ft Frfsmjhmjw!
