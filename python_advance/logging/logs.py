import logging
#Level le indica el primer nivel en este caso DEBUG
#Filename le indica el archivo a crear
#Filemode le indicamos que lo sobreescriba (lo podemos omitir)
logging.basicConfig(level=logging.DEBUG, filename="ejemplo_logs.log", filemode="w")

logging.debug("Log de debugging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

