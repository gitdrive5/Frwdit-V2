#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "21879629"))
    API_HASH = os.environ.get("API_HASH", "dcb6bfd6d51a8ff5f6aadb01b9fdd11b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5322382737:AAE9i-QNv5oka-BFn_VrgENJg1BSaPKGvM4") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "empty")
    OWNER_ID = os.environ.get("OWNER_ID", "5143506371")
    SESSION = os.environ.get("SESSION", "AQCBewPXye6HuBJVfJUuCNI5TEm4__5ngD-Fqm7u8Uieo2TgQ5V0mN9w89EVcltdXlFSjthCieu8-ys3bjLvoo6rP5yXDIZGjmEtoot-73I7MinAEiz_t1HrqsEHIq8GNbqr5mZfP86urVGcKjPGH74OWl0500C-hPgvJnERfRYdwyWlO0NcLS230pL_5eWAUN8GIkQKKNmPleWSIkoK81iUrEpZ-fpB3ubcTsSOhWQdbsaer7vBbfmpDvUyvvAbryvZrgtQLso-SdqgrTuPiMTpa5hQcjHFjZZejiJHRGzVgSG-K_3n3_QO_DNVJf8SMolcHpBAFcwE9kJr5kQ78eMaAAAAATKTrcMA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
