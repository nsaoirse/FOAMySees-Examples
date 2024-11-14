import openseespy.opensees as ops
# FOAMySees GUI Generated User Loads, time written=1731571194.0793228

def applyGM(time):

    # default is to pass

    # pass

    #

    #   'time' is available for use as a variable. It is initialized by the python function wrapping this user routine. If you'd like to implement time-dependent loads,

    #   or time histories for that matter, you must input the '-startTime', time) option in the ops.timeSeries object with 'time' as the time variable

    

    

    

    ####################################################################################################################################

    IDloadTag = 400			# load tag        <-make sure you remove this via #ops.remove('loadPattern',IDloadTag) in the userLoadRemove.txt file

    TSTAG=2				# time series tag <- make sure you remove this via #ops.remove('timeSeries', TSTAG) in the userLoadRemove.txt file

    

    GMfact=1

    GMfile='./fromUser/GroundMotion.acc'

    

    # Uniform EXCITATION: acceleration input

    dt = 0.00001			# time step for input ground motion

    maxNumIter = 10

    GMdirection=1

    Tol=1e-3

    

    period=0.01

    factor=5e-4

    tStart=0.01

    tEnd=0.25

    

    #ops.timeSeries('Path', TSTAG, '-dt', dt, '-filePath', GMfile, '-factor', GMfact, '-useLast', '-startTime', time) # <--this is the python variable for time & how to use it!

    #ops.pattern('UniformExcitation', IDloadTag, GMdirection, '-accel', 2) 

    

    ####################################################################################################################################

    ### other things you could do.... additionally, you could apply nodal loads, or nodal load time histories.

    ### just make sure that whatever you apply here, that the pattern and timeSeries objects are 'removed' from the model in the userLoadRemove.txt file

    ops.timeSeries('Triangle', TSTAG, tStart, tEnd, period, '-factor', factor, '-shift', time, '-zeroShift', 0.0)

    ops.pattern('MultipleSupport', IDloadTag-1)

    

    #ops.imposedMotion(0, 1,IDloadTag)

    

    

    ops.groundMotion(IDloadTag, 'Plain', '-disp',TSTAG, '-int', 'Trapezoidal', '-fact', 1.0) 

    



def removeGM():

    # default is to pass

    # pass

    #

    #

    

    # Anything you apply you must remove, as well

    

    TSTAG=2

    ops.remove('timeSeries', TSTAG) 

    IDloadTag = 400

    ops.remove('loadPattern',IDloadTag)

    IDloadTag1 = 399

    ops.remove('loadPattern',IDloadTag1)

    

    

