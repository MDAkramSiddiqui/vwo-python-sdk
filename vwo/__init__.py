# flake8: noqa

"""
VWO Python SDK for server-side

The MIT License (MIT)

Copyright (c) 2019 Wingify Software Pvt. Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, includi    ng without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, sub    ject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMEN    T. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WI    TH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author: VWO
Email: dev@wingify.com / integration@vwo.com
Github - https://github.com/wingify/vwo-python-sdk
"""

from .vwo import VWO
from .settings_file_util import get as get_settings_file
from .user_profile import UserProfileService

from .import logger
import logging