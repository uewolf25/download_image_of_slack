#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

#　環境変数をセット
LT = os.environ.get("LEGACY_TOKEN")
CI = os.environ.get("CHANNEL_ID")