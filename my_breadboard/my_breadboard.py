from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, cast

from viam.components.board import Board
from viam.module.types import Reconfigurable
from viam.resource.types import Model, ModelFamily
from viam.resource.base import ResourceBase

class MyBreadboard(Board, Reconfigurable):

    # Here is where we define our new model's colon-delimited-triplet (acme:demo:mybase)
    # acme = namespace, demo = family, mybase = model name.
    MODEL: ClassVar[Model] = Model(ModelFamily("acme", "demo"), "mybreadboard")

    # Constructor
    @classmethod
    def new_breadboard(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        base = cls(config.name)
        base.reconfigure(config, dependencies)
        return base

    # Validates JSON Configuration
    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        # Validate configuration
        return ["Verified"]

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        # reconfigure component
        pass
    
    


        