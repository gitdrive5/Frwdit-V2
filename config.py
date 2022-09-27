#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "1715666"))
    API_HASH = os.environ.get("API_HASH", "8082d87f5cd157c615d5d2837af21b87")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5322382737:AAE9i-QNv5oka-BFn_VrgENJg1BSaPKGvM4") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "empty")
    OWNER_ID = os.environ.get("OWNER_ID", "5143506371")
    SESSION = os.environ.get("SESSION", "BQDCw-hYoupQiP_AwZBclYZK0O1mpzKW_dSkOI_DKorDFNA6dMbswI6PJdRCKtTpd2jRnxZ48_cTL5qy7anJOtLpBS3HiUKCb9WQEi7A1u_lyjHOJL0fHeN5pycwOePb7tqP6r6qDRjIVAIOZTlS50mIPYpkURqCgFxMekwTXxcNptQn9G2CV61mPux4T-EIssS9TFzZVVkv0OHNOreGgURDtX9ZPj7xBD6cJl1GQGnNOuxsSOpCgK6s9sz5ee14EZp1f-sgzfBpVNCzdaQkRv68b2IGQtPhSJke5Pir59a2tmADhIpaJGUUT6KKWk0UXSoeCYJ4SEbk26KDR7bySgilcdf4KQA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
