from typing import ClassVar, Mapping, Sequence

from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.resource.types import Model, ModelFamily
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase

from .api import Foo


class MyFoo(Foo, Reconfigurable):
    """ This is the specific implementation of MyFoo (defined in api.py).
    
    It inherits from Foo, as well conforms to the ``Reconfigurable`` protocol, which signifies that this component can be reconfigured.
    It also specifies a function ``Foo.new``. which conforms to the ``resource.types.ResourceCreator``type, which is required for all models.
    """

    MODEL: ClassVar[Model] = Model(ModelFamily("acme", "demo"), "foo")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        foo = cls(config.name)
        return foo

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        # Custom validation can be done by specifiying a validate function like this one. Validate functions
        # can raise errors that will be returned to the parent through gRPC. Validate functions can
        # also return a sequence of strings representing the implicit dependencies of the resource.
        if "invalid" in config.attributes.fields:
            raise Exception(
                f"'invalid' attribute not allowed for model {cls.SUBTYPE}:{cls.MODEL}")
        arg1 = 'config.attributes.fields["arg1"].string_value'
        if arg1 == "":
            raise Exception(
                "A arg1 attribute is required for Gizmo component.")
        

    async def set_state(self, state: bool) -> bool:
        self.state = state.state
        return self.my_state


    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        pass
        #self.my_arg = config.attributes.fields["arg1"].string_value

