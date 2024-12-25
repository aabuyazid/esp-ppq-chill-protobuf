# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Dl

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MapType(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MapType()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMapType(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MapType
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MapType
    def KeyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MapType
    def ValueType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from FlatBuffers.Dl.TypeInfo import TypeInfo
            obj = TypeInfo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def MapTypeStart(builder):
    builder.StartObject(2)

def Start(builder):
    MapTypeStart(builder)

def MapTypeAddKeyType(builder, keyType):
    builder.PrependInt32Slot(0, keyType, 0)

def AddKeyType(builder, keyType):
    MapTypeAddKeyType(builder, keyType)

def MapTypeAddValueType(builder, valueType):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(valueType), 0)

def AddValueType(builder, valueType):
    MapTypeAddValueType(builder, valueType)

def MapTypeEnd(builder):
    return builder.EndObject()

def End(builder):
    return MapTypeEnd(builder)

import FlatBuffers.Dl.TypeInfo
try:
    from typing import Optional
except:
    pass

class MapTypeT(object):

    # MapTypeT
    def __init__(self):
        self.keyType = 0  # type: int
        self.valueType = None  # type: Optional[FlatBuffers.Dl.TypeInfo.TypeInfoT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        mapType = MapType()
        mapType.Init(buf, pos)
        return cls.InitFromObj(mapType)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, mapType):
        x = MapTypeT()
        x._UnPack(mapType)
        return x

    # MapTypeT
    def _UnPack(self, mapType):
        if mapType is None:
            return
        self.keyType = mapType.KeyType()
        if mapType.ValueType() is not None:
            self.valueType = FlatBuffers.Dl.TypeInfo.TypeInfoT.InitFromObj(mapType.ValueType())

    # MapTypeT
    def Pack(self, builder):
        if self.valueType is not None:
            valueType = self.valueType.Pack(builder)
        MapTypeStart(builder)
        MapTypeAddKeyType(builder, self.keyType)
        if self.valueType is not None:
            MapTypeAddValueType(builder, valueType)
        mapType = MapTypeEnd(builder)
        return mapType
