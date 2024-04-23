# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re

def validate_numero_telefone(phone_number):
    pattern = '\(\d{2}\) 9\d{4}-\d{4}'
   
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
        return "Número de telefone válido."
    
    else:
       return "Número de telefone inválido."
    
phone_number = input()  
result = validate_numero_telefone(phone_number)
print(result)