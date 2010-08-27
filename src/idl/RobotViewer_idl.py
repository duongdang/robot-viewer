# Python stubs generated by omniidl from RobotViewer.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "hpp"
#
__name__ = "hpp"
_0_hpp = omniORB.openModule("hpp", r"RobotViewer.idl")
_0_hpp__POA = omniORB.openModule("hpp__POA", r"RobotViewer.idl")


# typedef ... DoubleSeq
class DoubleSeq:
    _NP_RepositoryId = "IDL:hpp/DoubleSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_hpp.DoubleSeq = DoubleSeq
_0_hpp._d_DoubleSeq  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_double, 0)
_0_hpp._ad_DoubleSeq = (omniORB.tcInternal.tv_alias, DoubleSeq._NP_RepositoryId, "DoubleSeq", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_double, 0))
_0_hpp._tc_DoubleSeq = omniORB.tcInternal.createTypeCode(_0_hpp._ad_DoubleSeq)
omniORB.registerType(DoubleSeq._NP_RepositoryId, _0_hpp._ad_DoubleSeq, _0_hpp._tc_DoubleSeq)
del DoubleSeq

# typedef ... ElementList
class ElementList:
    _NP_RepositoryId = "IDL:hpp/ElementList:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_hpp.ElementList = ElementList
_0_hpp._d_ElementList  = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0)
_0_hpp._ad_ElementList = (omniORB.tcInternal.tv_alias, ElementList._NP_RepositoryId, "ElementList", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0_hpp._tc_ElementList = omniORB.tcInternal.createTypeCode(_0_hpp._ad_ElementList)
omniORB.registerType(ElementList._NP_RepositoryId, _0_hpp._ad_ElementList, _0_hpp._tc_ElementList)
del ElementList

# interface RobotViewer
_0_hpp._d_RobotViewer = (omniORB.tcInternal.tv_objref, "IDL:hpp/RobotViewer:1.0", "RobotViewer")
omniORB.typeMapping["IDL:hpp/RobotViewer:1.0"] = _0_hpp._d_RobotViewer
_0_hpp.RobotViewer = omniORB.newEmptyClass()
class RobotViewer :
    _NP_RepositoryId = _0_hpp._d_RobotViewer[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # exception KeyError
    _0_hpp.RobotViewer.KeyError = omniORB.newEmptyClass()
    class KeyError (CORBA.UserException):
        _NP_RepositoryId = "IDL:hpp/RobotViewer/KeyError:1.0"

        _NP_ClassName = "hpp.RobotViewer.KeyError"

        def __init__(self, reason):
            CORBA.UserException.__init__(self, reason)
            self.reason = reason
    
    _d_KeyError  = (omniORB.tcInternal.tv_except, KeyError, KeyError._NP_RepositoryId, "KeyError", "reason", (omniORB.tcInternal.tv_string,0))
    _tc_KeyError = omniORB.tcInternal.createTypeCode(_d_KeyError)
    omniORB.registerType(KeyError._NP_RepositoryId, _d_KeyError, _tc_KeyError)


_0_hpp.RobotViewer = RobotViewer
_0_hpp._tc_RobotViewer = omniORB.tcInternal.createTypeCode(_0_hpp._d_RobotViewer)
omniORB.registerType(RobotViewer._NP_RepositoryId, _0_hpp._d_RobotViewer, _0_hpp._tc_RobotViewer)

# RobotViewer operations and attributes
RobotViewer._d_createElement = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), None)
RobotViewer._d_destroyElement = (((omniORB.tcInternal.tv_string,0), ), (), {_0_hpp.RobotViewer.KeyError._NP_RepositoryId: _0_hpp.RobotViewer._d_KeyError})
RobotViewer._d_enableElement = (((omniORB.tcInternal.tv_string,0), ), (), {_0_hpp.RobotViewer.KeyError._NP_RepositoryId: _0_hpp.RobotViewer._d_KeyError})
RobotViewer._d_disableElement = (((omniORB.tcInternal.tv_string,0), ), (), {_0_hpp.RobotViewer.KeyError._NP_RepositoryId: _0_hpp.RobotViewer._d_KeyError})
RobotViewer._d_updateElementConfig = (((omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:hpp/DoubleSeq:1.0"]), (), {_0_hpp.RobotViewer.KeyError._NP_RepositoryId: _0_hpp.RobotViewer._d_KeyError})
RobotViewer._d_getElementConfig = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:hpp/DoubleSeq:1.0"], ), {_0_hpp.RobotViewer.KeyError._NP_RepositoryId: _0_hpp.RobotViewer._d_KeyError})
RobotViewer._d_listElement = ((), (omniORB.typeMapping["IDL:hpp/ElementList:1.0"], ), None)
RobotViewer._d_Ping = ((), ((omniORB.tcInternal.tv_string,0), ), None)

# RobotViewer object reference
class _objref_RobotViewer (CORBA.Object):
    _NP_RepositoryId = RobotViewer._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def createElement(self, *args):
        return _omnipy.invoke(self, "createElement", _0_hpp.RobotViewer._d_createElement, args)

    def destroyElement(self, *args):
        return _omnipy.invoke(self, "destroyElement", _0_hpp.RobotViewer._d_destroyElement, args)

    def enableElement(self, *args):
        return _omnipy.invoke(self, "enableElement", _0_hpp.RobotViewer._d_enableElement, args)

    def disableElement(self, *args):
        return _omnipy.invoke(self, "disableElement", _0_hpp.RobotViewer._d_disableElement, args)

    def updateElementConfig(self, *args):
        return _omnipy.invoke(self, "updateElementConfig", _0_hpp.RobotViewer._d_updateElementConfig, args)

    def getElementConfig(self, *args):
        return _omnipy.invoke(self, "getElementConfig", _0_hpp.RobotViewer._d_getElementConfig, args)

    def listElement(self, *args):
        return _omnipy.invoke(self, "listElement", _0_hpp.RobotViewer._d_listElement, args)

    def Ping(self, *args):
        return _omnipy.invoke(self, "Ping", _0_hpp.RobotViewer._d_Ping, args)

    __methods__ = ["createElement", "destroyElement", "enableElement", "disableElement", "updateElementConfig", "getElementConfig", "listElement", "Ping"] + CORBA.Object.__methods__

omniORB.registerObjref(RobotViewer._NP_RepositoryId, _objref_RobotViewer)
_0_hpp._objref_RobotViewer = _objref_RobotViewer
del RobotViewer, _objref_RobotViewer

# RobotViewer skeleton
__name__ = "hpp__POA"
class RobotViewer (PortableServer.Servant):
    _NP_RepositoryId = _0_hpp.RobotViewer._NP_RepositoryId


    _omni_op_d = {"createElement": _0_hpp.RobotViewer._d_createElement, "destroyElement": _0_hpp.RobotViewer._d_destroyElement, "enableElement": _0_hpp.RobotViewer._d_enableElement, "disableElement": _0_hpp.RobotViewer._d_disableElement, "updateElementConfig": _0_hpp.RobotViewer._d_updateElementConfig, "getElementConfig": _0_hpp.RobotViewer._d_getElementConfig, "listElement": _0_hpp.RobotViewer._d_listElement, "Ping": _0_hpp.RobotViewer._d_Ping}

RobotViewer._omni_skeleton = RobotViewer
_0_hpp__POA.RobotViewer = RobotViewer
omniORB.registerSkeleton(RobotViewer._NP_RepositoryId, RobotViewer)
del RobotViewer
__name__ = "hpp"

#
# End of module "hpp"
#
__name__ = "RobotViewer_idl"

_exported_modules = ( "hpp", )

# The end.
