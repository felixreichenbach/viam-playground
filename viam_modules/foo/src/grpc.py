"""
This file outlines the general structure for the gRPC client and server around a custom, modularized component.

It defines the gRPC service that will handle calls to the component,
and the gRPC client that will be able to make calls to this component.

The ``FooService`` implements the gRPC service for the Foo. This will allow other robots and clients to make requests of the Foo.
It extends both from ``GizmoServiceServicer`` and ``ResourceRPCServiceBase``. The former is the gRPC service as defined by the proto,
and the latter is the class that all gRPC services for components must inherit from.

Finally, the ``FooClient`` is the gRPC client for a Foo. It inherits from Foo since it implements all the same functions. The
implementations are simply gRPC calls to some remote Foo.

To see how this custom modular component is registered, see the __init__.py file.
To see the custom implementation of this component, see the my_foo.py file.
"""

from grpclib.client import Channel

from viam.resource.rpc_service_base import ResourceRPCServiceBase

from ..proto.foo_pb2_grpc import FooServiceServicer, FooServiceStub
from ..proto.foo_pb2 import (
    Request,
    Response
)

from .api import Foo


class FooService(FooServiceServicer, ResourceRPCServiceBase):
    """Example gRPC service for the Foo component"""

    RESOURCE_TYPE = Foo

    async def SetState(self, request: Request, context) -> Response:
        assert request is not None
        name = request.name
        foo = self.get_resource(name)
        result = await foo.set_state(request.state)
        response = Response(state=result)
        return response


class FooClient(Foo):
    """Example gRPC client for the Foo component"""

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = FooServiceStub(channel)
        super().__init__(name)

    async def set_state(self, state: bool) -> bool:
        response: Response = await self.client.SetState(Request(name=self.name, state=state))
        return response
