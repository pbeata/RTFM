"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class edmOUT(object):
    __slots__ = ["tempSlope"]

    def __init__(self):
        self.tempSlope = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(edmOUT._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">d", self.tempSlope))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != edmOUT._get_packed_fingerprint():
            raise ValueError("Decode error")
        return edmOUT._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = edmOUT()
        self.tempSlope = struct.unpack(">d", buf.read(8))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if edmOUT in parents: return 0
        tmphash = (0xd13f6704302b9464) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if edmOUT._packed_fingerprint is None:
            edmOUT._packed_fingerprint = struct.pack(">Q", edmOUT._get_hash_recursive([]))
        return edmOUT._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

