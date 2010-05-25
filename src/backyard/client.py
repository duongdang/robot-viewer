#! /usr/bin/env python

# Copyright LAAS/CNRS 2009-2010
# Authors Duong Dang

import getopt,sys, warnings, imp, os

# Import the CORBA module
from omniORB import CORBA

# Import the stubs for the CosNaming and RobotViewer modules
import imp
path = imp.find_module('robotviewer')[1]
sys.path.append(path)
import RobotViewer
import CosNaming

# Initialise the ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Obtain a reference to the root naming context
obj         = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print "Failed to narrow the root naming context"
    sys.exit(1)

# Resolve the name "test.my_context/ExampleEcho.Object"
name = [CosNaming.NameComponent("test", "my_context"),
        CosNaming.NameComponent("Request", "Object")]

try:
    obj = rootContext.resolve(name)

except CosNaming.NamingContext.NotFound, ex:
    print "Name not found"
    sys.exit(1)

# Narrow the object to an RobotViewer::Request
eo = obj._narrow(RobotViewer.Request)

if eo is None:
    print "Object reference is not an Example::Echo"
    sys.exit(1)

# Invoke the echoString operation

def execute(cmd,str_args,conf):
    """
    """
    print eo.req(cmd, str_args,conf)
