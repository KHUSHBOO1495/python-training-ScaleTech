import logging

# logging.basicConfig(level=logging.INFO)

# logging.debug("Debug message")
# logging.info("Application started")
# logging.warning("Low memory")
# logging.error("Unable to open file")
# logging.critical("System failure")



# logging.basicConfig(
#     filename="app.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.info("Application started")

# try:
#     number = 10
#     divisor = 0

#     result = number / divisor

# except Exception:
#     logging.exception("Calculation failed")

# logging.info("Application finished")



# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )

# logger = logging.getLogger(__name__)

# logger.debug("Debugging application")
# logger.info("Application started")
# logger.warning("This is a warning")
# logger.error("Something went wrong")
# logger.critical("Critical problem")



logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def calculate(a, b):
    logger.info("Starting calculation")

    try:
        result = a / b
        logger.info("Calculation successful")
        return result

    except Exception:
        logger.exception("Calculation failed")


logger.info("Program started")

calculate(10, 2)
calculate(10, 0)

logger.info("Program finished")
