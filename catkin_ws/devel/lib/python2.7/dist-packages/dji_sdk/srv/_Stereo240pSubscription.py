# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dji_sdk/Stereo240pSubscriptionRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Stereo240pSubscriptionRequest(genpy.Message):
  _md5sum = "f676e2d64f211783ff9d6cc8a69aa395"
  _type = "dji_sdk/Stereo240pSubscriptionRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
uint8 front_right_240p
uint8 front_left_240p
uint8 down_front_240p
uint8 down_back_240p



uint8 unsubscribe_240p

"""
  __slots__ = ['front_right_240p','front_left_240p','down_front_240p','down_back_240p','unsubscribe_240p']
  _slot_types = ['uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       front_right_240p,front_left_240p,down_front_240p,down_back_240p,unsubscribe_240p

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Stereo240pSubscriptionRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.front_right_240p is None:
        self.front_right_240p = 0
      if self.front_left_240p is None:
        self.front_left_240p = 0
      if self.down_front_240p is None:
        self.down_front_240p = 0
      if self.down_back_240p is None:
        self.down_back_240p = 0
      if self.unsubscribe_240p is None:
        self.unsubscribe_240p = 0
    else:
      self.front_right_240p = 0
      self.front_left_240p = 0
      self.down_front_240p = 0
      self.down_back_240p = 0
      self.unsubscribe_240p = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_5B().pack(_x.front_right_240p, _x.front_left_240p, _x.down_front_240p, _x.down_back_240p, _x.unsubscribe_240p))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.front_right_240p, _x.front_left_240p, _x.down_front_240p, _x.down_back_240p, _x.unsubscribe_240p,) = _get_struct_5B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_5B().pack(_x.front_right_240p, _x.front_left_240p, _x.down_front_240p, _x.down_back_240p, _x.unsubscribe_240p))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.front_right_240p, _x.front_left_240p, _x.down_front_240p, _x.down_back_240p, _x.unsubscribe_240p,) = _get_struct_5B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5B = None
def _get_struct_5B():
    global _struct_5B
    if _struct_5B is None:
        _struct_5B = struct.Struct("<5B")
    return _struct_5B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dji_sdk/Stereo240pSubscriptionResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Stereo240pSubscriptionResponse(genpy.Message):
  _md5sum = "eb13ac1f1354ccecb7941ee8fa2192e8"
  _type = "dji_sdk/Stereo240pSubscriptionResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool result

"""
  __slots__ = ['result']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Stereo240pSubscriptionResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.result is None:
        self.result = False
    else:
      self.result = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.result))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.result,) = _get_struct_B().unpack(str[start:end])
      self.result = bool(self.result)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.result))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.result,) = _get_struct_B().unpack(str[start:end])
      self.result = bool(self.result)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class Stereo240pSubscription(object):
  _type          = 'dji_sdk/Stereo240pSubscription'
  _md5sum = 'c1205f3b01904555b852bb2bc5881da0'
  _request_class  = Stereo240pSubscriptionRequest
  _response_class = Stereo240pSubscriptionResponse
