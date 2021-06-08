![Tec de Monterrey](../../images/logotecmty.png)
# Hello Name
Básico-Hello Name

Modifica el programa que se encuentra en la carpeta `src` que se llama `main.py` y que contiene el siguiente código:

```python
def main():
  name = input("Enter your name: ")
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

El programa debe pedirle su nombre al usuario, y a continuación saludarlo,
imprimiendo el mensaje: `Hello <name>!`. Por ejemplo, si el usuario teclea
como nombre `Diego`, el programa debe imprimir:

```plaintext
Hello Diego!
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Agrega una nueva línea abajo del comentario con el código para imprimir
`Hello <name>!` y ejecuta el programa.


**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
