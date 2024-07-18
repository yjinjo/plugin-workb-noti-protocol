import logging

from spaceone.notification.plugin.protocol.lib.server import ProtocolPluginServer

app = ProtocolPluginServer()

_LOGGER = logging.getLogger("spaceone")


@app.route("Protocol.init")
def protocol_init(params: dict) -> dict:
    """init plugin by options

    Args:
        params (ProtocolInitRequest): {
            'options': 'dict',    # Required
            'domain_id': 'str'
        }

    Returns:
        PluginResponse: {
            'metadata': 'dict'
        }
    """
    pass


@app.route("Protocol.verify")
def protocol_verify(params: dict) -> None:
    """Verifying protocol plugin

    Args:
        params (ProtocolVerifyRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'domain_id': 'str'
        }

    Returns:
        None
    """
    pass


@app.route("Notification.dispatch")
def notification_dispatch(params: dict):
    """dispatch notification

    Args:
        params (NotificationDispatchRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'channel_data': 'dict', # Required
            'message': 'dict',
            'notification_type': 'str',
        }

    Returns:
        None
    """
    pass
