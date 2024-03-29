"""Contains functionality related to Weather"""
import logging
from enum import IntEnum
import json
from pathlib import Path
import random
import urllib.parse

import requests

from models.producer import Producer
logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is incomplete - skipping")
        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        #
        logger.debug("handling incoming weather message")
        value = message.value()
        self.temperature = value["temperature"]
        self.status = value["status"]
        logger.debug(
            "weather is now %sf and %s", self.temperature, self.status.replace("_", " ")
        )