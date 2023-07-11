# gRPC / ProtoBuf Guide

Official Python documentation: https://grpc.io/docs/languages/python/basics/


## Approach

1. create proto file
2. generate apis
3. create api.py (abstract api definitions)


## Useful Commands

Show help:

python3 -m grpc.tools.protoc -h


Generate API definitions:

python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. foo.proto



