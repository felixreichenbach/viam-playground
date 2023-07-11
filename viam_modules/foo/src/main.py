import asyncio

from viam.module.module import Module

from ..src import Foo, MyFoo


async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered. For an example, see the `src.__init__.py` file.
    """

    module = Module.from_args()
    module.add_model_from_registry(Foo.SUBTYPE, MyFoo.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
