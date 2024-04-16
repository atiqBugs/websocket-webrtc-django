

# Create your models here.
async def connect(self, scope):
    """
    Connect to a audio chat room group

    Args:
        scope: The scope of the connection

    Returns:
        None
    """
    self.room_name = scope["url_route"]["kwargs"]["room_name"]
    self.room_group_name = f"audio_{self.room_name}"

    await self.channel_layer.group_add(self.room_group_name, self.channel_name)
    await self.accept()


async def disconnect(self, close_code):
    """
    Disconnect from a audio chat room group

    Args:
        close_code: The close code of the connection

    Returns:
        None
    """
    await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    