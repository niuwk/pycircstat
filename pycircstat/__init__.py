from __future__ import absolute_import
from collections import namedtuple

CI = namedtuple('confidence_interval', ['lower','upper'])

from .descriptive import *
