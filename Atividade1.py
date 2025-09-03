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
