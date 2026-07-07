import logging 

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(lineno)s - %(message)s")

logging.info("Mensagem de info")
