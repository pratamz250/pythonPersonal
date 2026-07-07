import logging

logging.basicConfig(
        level=logging.INFO, 
        format="%(name)s - %(asctime)s - %(message)s")

import modulo_p3

logging.info("Mensagem")
print(modulo_p3.logger)
