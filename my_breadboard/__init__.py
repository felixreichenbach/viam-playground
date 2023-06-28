"""
This file registers the MyBreadboard model with the Python SDK.
"""

from viam.components.board import *
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .my_breadboard import MyBreadboard

Registry.register_resource_creator(Board.SUBTYPE, MyBreadboard.MODEL, ResourceCreatorRegistration(MyBreadboard.new_base, MyBreadboard.validate_config))