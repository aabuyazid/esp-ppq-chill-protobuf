# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Dl

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SequenceType(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SequenceType()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSequenceType(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # SequenceType
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SequenceType
    def ElemType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from FlatBuffers.Dl.TypeInfo import TypeInfo
            obj = TypeInfo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def SequenceTypeStart(builder):
    builder.StartObject(1)

def Start(builder):
    SequenceTypeStart(builder)

def SequenceTypeAddElemType(builder, elemType):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(elemType), 0)

def AddElemType(builder, elemType):
    SequenceTypeAddElemType(builder, elemType)

def SequenceTypeEnd(builder):
    return builder.EndObject()

def End(builder):
    return SequenceTypeEnd(builder)
