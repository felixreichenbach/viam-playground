"""
This file registers the Foo subtype with the Viam Registry, as well as the specific MyFoo model.
"""

from viam.components.motor import *  # noqa: F403 Need to import motor so the component registers itself
from viam.resource.registry import Registry, ResourceCreatorRegistration, ResourceRegistration

from .api import Foo
from .grpc import FooClient, FooService
from .my_foo import MyFoo

Registry.register_subtype(ResourceRegistration(Foo, FooService, lambda name, channel: FooClient(name, channel)))

Registry.register_resource_creator(Foo.SUBTYPE, Foo.MODEL, ResourceCreatorRegistration(MyFoo.new, MyFoo.validate_config))