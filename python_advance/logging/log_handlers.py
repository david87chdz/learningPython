import logging

logger = logging.getLogger(__name__)
# Definimos el nivel mínimo
logger.setLevel(logging.DEBUG)

# Para coger la consola
handler_consola = logging.StreamHandler()
# Damos el formato
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler_consola.setFormatter(formato_logs)
logger.addHandler(handler_consola)

#Para añadir el log de archivo
handler_archivo = logging.FileHandler("archivo.log")
handler_archivo.setLevel(logging.ERROR)
handler_archivo.setFormatter(formato_logs)
logger.addHandler(handler_archivo)

logger.info("registro informativo")
