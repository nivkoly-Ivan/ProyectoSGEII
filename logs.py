from datetime import datetime
import os
import logging

#En el requisito 006 nos piden utilizar el recurso Logging
#Basicamente nos sirve para dar formato natural y pasar datos siempre, muy parecido a lo de BancoPuertollano

class Log:

    def __init__(self):
        fecha = datetime.now().strftime("%Y%m%d")
        self.ruta = f"log/{fecha}-iniciado.txt"

        if not os.path.exists("log"):
            os.mkdir("log")

        logging.basicConfig(
            filename=self.ruta,
            level=logging.INFO,
            format="[%(asctime)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            encoding="utf-8"
        )

    def escribir(self, tipo, mensaje):
        tipo = tipo.upper()

        if tipo == "ERROR":
            logging.error(mensaje)
        elif tipo == "INFO":
            logging.info(mensaje)
        elif tipo == "INTENTO ILEGAL":
            logging.warning(f"[{tipo}] {mensaje}")
        else:
            logging.info(f"[{tipo}] {mensaje}")
