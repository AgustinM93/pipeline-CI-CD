import errno
def main():

    from os import mkdir
    try:
        
        mkdir("build")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


    f = open("build/index.html", "w")
    f.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>
    """)
    f.close()

