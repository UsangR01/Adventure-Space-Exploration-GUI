import logging
import time

logging.basicConfig(filename=f'logs/log_{time.strftime("%Y%m%d-%H%M%S")}.log', level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

def log_move(direction):
    logging.info(f'Moved {direction}')

def log_location(location):
    logging.info(f'Entered {location}')

def log_pickup(item):
    logging.info(f"You've Picked up {item}")

def log_use_up(item):
    logging.info(f"You've Used up {item}")

def log_unittest():
    logging.info(f"You've logged a unittest")

def log_drop_off(item):
    logging.info(f"You've Dropped off {item}")

def log_NegData_Check():
    logging.info(f"You've checked negotiator data")

def log_help_check():
    logging.info(f"You've Used the help button")


















# from datetime import datetime
#
# import settings
#
# formatter = logging.Formatter('%(message)s')
#
# default_logger: logging.Logger
# event_logger: logging.Logger
#
#
# def setup_logger(name, log_file, level=logging.INFO):
#     """To set up as many loggers as you want"""
#
#     handler = logging.FileHandler(log_file)
#     handler.setFormatter(formatter)
#
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     logger.addHandler(handler)
#
#     return logger
#
#
# def init_loggers():
#     global default_logger
#     default_logger = None
#     global event_logger
#     event_logger = None
#     ensure_folders_exist()
#     now = datetime.now()
#     if settings.create_logs:
#         default_logger = setup_logger("default_logger", r'logs/log_' + str(now).replace(':', '') + '.txt')
#     if settings.create_event:
#         event_logger = setup_logger("event_logger", r'events/event_' + str(now).replace(':', '') + '.txt')
#
#
# def ensure_folders_exist():
#     if not os.path.exists("events"):
#         os.makedirs("events")
#     if not os.path.exists("logs"):
#         os.makedirs("logs")
#
#
# def event(e):
#     global event_logger
#     if event_logger:
#         event_logger.info(e)
