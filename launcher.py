#importing modules from lib to facilitate logging and running
from lib.bot import bot
from lib.bot import __init__

import logging

#pulls logs based on .\logging.conf
logger = logging.getLogger(__name__)

#set version
VERSION = "0.0.0"

#run bot
bot.run(VERSION)
