"""MongoDB collections."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
from .database import get_mongodb


db = get_mongodb()
questions_collection = db['questions']
