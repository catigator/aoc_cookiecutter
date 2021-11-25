import logging
import sys

logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="w+",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
