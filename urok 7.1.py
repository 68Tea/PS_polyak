import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs1.log",
                    filemode="w",
                    format="We have next message:%(asctime)s:%(levelname)s:%(message)s")

try:
    print(10/0)
except Exception:
    logging.exception("Expect")