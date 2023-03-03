"""El modulo crea una carpeta y adentro de esta carpeta crea un archivo"""
import errno
import os


def main():
    """Funcion main, crea una carpeta y un archivo index.html"""
    try:
        os.mkdir("build")
        with open("build/index.html", "w", encoding="utf8") as folder:
            folder.write("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport"
            content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            </head>
            <body>
            </body>
            </html>
            """)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
