import logging
from dataclasses import asdict, astuple

from inventory import Inventory

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format=" %(asctime)s -  %(name)s - %(levelname)s - %(message)s",
    datefmt='%Y-%m-%d %I:%M:%S %p',
)


if __name__ == "__main__":

    invent = Inventory("Cocoa", 2, 25)
    invent.name = "Milk"

    logging.info("Started...")
    logging.info(invent)
    logging.info(asdict(invent))
    logging.info(astuple(invent))
    logging.info(invent.quantity_at_hand)
    logging.info(invent.name)
    logging.info(invent.total_cost())
    logging.info("Finished...")
