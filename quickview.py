#! /usr/bin/env python

# Copyright LAAS/CNRS 2009-2012
# Authors Duong Dang


import getopt,sys, warnings
from getopt import getopt
from application import Application

#########################################################
################   MAIN PROGRAM    ######################
#########################################################

def usage():
    print """
Usage ./quickview [options]

Options:

-w, --wrl      : load a wrl file
-s, --simplify : simplify display (only draw a skeleton)
-m, --measure  : measure startup time
--standalone   : standalone mode 
"""

def main():
    debug=False
    mst=False
    smp=False
    VRMLmesh=None
    standalone=False
    try:
        opts,args=getopt(sys.argv[1:],
                         "l:w:sdmho:v", ["load=","wrl=","simplify","debug","help", "measure-time","output=","standalone"])
    except Exception, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    sequenceFile = None
    verbose = False
    for o, a in opts:
        
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
 
        elif o in ("-d", "--debug"):
            debug=True 
        
        elif o in ("-s", "--simplify"):
            smp=True

        elif o in ("-m", "--measure-time"):
            mst=True

        elif o in ("-o", "--output"):
            output = a

        elif o in ("-l", "--load"):
            sequenceFile=a        


        elif o in ("-w", "--wrl"):
            VRMLmesh=a

        elif o in ("--standalone"):
            standalone=True
        else:
            assert False, "unhandled option"
            
    
    app=Application(debug)
    if sequenceFile:
        app.basename=sequenceFile    
    app.VRMLfile=VRMLmesh
    app.measureTime=mst
    app.simplify=smp
    app.init()

    if not standalone:
        try:

            ##################################
            #      omniORB
            ##################################
            from omniORB import CORBA, PortableServer

            # Import the stubs for the Naming service
            import CosNaming

            # Import the stubs and skeletons
            import RoboViewer, RoboViewer__POA

            # Define an implementation of the Echo interface
            class Request_i (RoboViewer__POA.Request):
                def req(self, mesg):
                    print "request %s:", mesg
                    return app.execute(mesg)

            # Initialise the ORB
            orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

            # Find the root POA
            poa = orb.resolve_initial_references("RootPOA")

            # Create an instance of Request_i
            ri = Request_i()

            # Create an object reference, and implicitly activate the object
            ro = ri._this()

            # Obtain a reference to the root naming context
            obj         = orb.resolve_initial_references("NameService")
            rootContext = obj._narrow(CosNaming.NamingContext)

            if rootContext is None:
                print "Failed to narrow the root naming context"
                sys.exit(1)

            # Bind a context named "test.my_context" to the root context
            name = [CosNaming.NameComponent("test", "my_context")]

            try:
                testContext = rootContext.bind_new_context(name)
                print "New test context bound"

            except CosNaming.NamingContext.AlreadyBound, ex:
                print "Test context already exists"
                obj = rootContext.resolve(name)
                testContext = obj._narrow(CosNaming.NamingContext)
                if testContext is None:
                    print "test.mycontext exists but is not a NamingContext"
                    sys.exit(1)

            # Bind the Echo object to the test context
            name = [CosNaming.NameComponent("Request", "Object")]

            try:
                testContext.bind(name, ro)
                print "New Request object bound"

            except CosNaming.NamingContext.AlreadyBound:
                testContext.rebind(name, ro)
                print "Request binding already existed -- rebound"

                # Note that is should be sufficient to just call rebind() without
                # calling bind() first. Some Naming service implementations
                # incorrectly raise NotFound if rebind() is called for an unknown
                # name, so we use the two-stage approach above

            # Activate the POA
            poaManager = poa._get_the_POAManager()
            poaManager.activate()

            # Everything is running now, but if this thread drops out of the end
            # of the file, the process will exit. orb.run() just blocks until the
            # ORB is shut down


        except Exception,error:
            warnings.warn("%s.\n Starting in standalone mode"%error)


    ##################################
    
    app.run()
if __name__=="__main__": 
    main()

