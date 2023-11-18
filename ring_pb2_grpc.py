# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ring_pb2 as ring__pb2


class AlertStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Delete = channel.unary_unary(
                '/ring.Alert/Delete',
                request_serializer=ring__pb2.keyValue.SerializeToString,
                response_deserializer=ring__pb2.returnValue.FromString,
                )
        self.Add = channel.unary_unary(
                '/ring.Alert/Add',
                request_serializer=ring__pb2.keyValue.SerializeToString,
                response_deserializer=ring__pb2.returnValue.FromString,
                )


class AlertServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=ring__pb2.keyValue.FromString,
                    response_serializer=ring__pb2.returnValue.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=ring__pb2.keyValue.FromString,
                    response_serializer=ring__pb2.returnValue.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ring.Alert', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Alert(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ring.Alert/Delete',
            ring__pb2.keyValue.SerializeToString,
            ring__pb2.returnValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ring.Alert/Add',
            ring__pb2.keyValue.SerializeToString,
            ring__pb2.returnValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
