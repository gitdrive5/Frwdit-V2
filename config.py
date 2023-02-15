#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "1945966"))
    API_HASH = os.environ.get("API_HASH", "6b73197f50512e26f5ebd42e73c3315f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5322382737:AAGWqY21L-mw_hPIbUF8sze_HrT9wEdDtGw") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "empty")
    OWNER_ID = os.environ.get("OWNER_ID", "5143506371")
    SESSION = os.environ.get("SESSION", "BQALRelShO-7i9naPF65FN1RAx2DCoeMzmxR7QbIebKOUkDGIvzDX6wrNFAWZO-zpRluvv6laft_pC8nBew4skx_Ddvx3J76tP5wUzFIgKyvl9HxtiN608kz0JGX5fK1MjBIxrhioxsxY-dAso6xmeTQBMK12eeJgZVnPnwkGwFYmFTlsUeAEPGc-t1nr_yyLkBvrg466gikBcid3uwlJMvxmCkLM19XGYv-fmnBXmDE9TH3w6CD_MTlkbwdfTtrMcF6Kdnf3vo_c2L7bkDGuN0NNhYoZRL7WIAfXXv46qPk98qoBmSXd7n9xoLQdSn0swDfsV0Ro94jX2yZp5S8f8i3AAAAAWuYknoA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
