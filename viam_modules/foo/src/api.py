"""
This file outlines the general structure for the API around a custom, modularized component.

It defines the abstract class definition that all concrete implementations must follow,
the gRPC service that will handle calls to the component,
and the gRPC client that will be able to make calls to this component.

In this example, the ``Gizmo`` abstract class defines what functionality is required for all Gizmos. It extends ``ComponentBase``,
as all component types must. It also defines its specific ``SUBTYPE``, which is used internally to keep track of supported types.

The ``GizmoService`` implements the gRPC service for the Gizmo. This will allow other robots and clients to make requests of the Gizmo.
It extends both from ``GizmoServiceBase`` and ``ResourceRPCServiceBase``. The former is the gRPC service as defined by the proto,
and the latter is the class that all gRPC services for components must inherit from.

Finally, the ``GizmoClient`` is the gRPC client for a Gizmo. It inherits from Gizmo since it implements all the same functions. The
implementations are simply gRPC calls to some remote Gizmo.

To see how this custom modular component is registered, see the __init__.py file.
To see the custom implementation of this component, see the my_gizmo.py file.
"""


import abc
from typing import Final

from viam.components.component_base import ComponentBase
from viam.resource.types import RESOURCE_TYPE_COMPONENT, Subtype

from proto.foo_pb2 import (
    Request,
    Response
)


class Foo(ComponentBase):

    SUBTYPE: Final = Subtype("acme", RESOURCE_TYPE_COMPONENT, "foo")

    @abc.abstractproperty
    def state(self):
        pass

    @abc.abstractmethod
    async def set_state(self, request: Request) -> Response:
        pass
