import re
def main():
    lista_ip="192.111.111.111 193.112.112.112 12.111.111.111 123.1234.111.111 666.666.666.666 999.999.999"

    # usando re.findall(), si el patron emplea un grupo, devuelve el identificador del grupo pero no toda la cadena, 
    # para devolver toda la cadena empezar el grupo con ?:
    patron="(?:\d{3}\.){3}\d{3}"
    print(re.findall(patron,lista_ip))

main()
