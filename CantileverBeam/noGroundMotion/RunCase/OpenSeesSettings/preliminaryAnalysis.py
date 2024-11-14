from dependencies  import *
def runGravity(self):
	
	if config.ApplyGravity=='yes':

		res=['disp','vel','accel','incrDisp','reaction','pressure','unbalancedLoad','mass']

		os.system('rm -rf SeesoutGrav')
		os.system('mkdir SeesoutGrav')
		os.system('touch SeesoutGrav.pvd')
		recorder('PVD', 'SeesoutGrav', '-precision', 4, '-dT', 0.1, *res)
		IDloadTag = 400			# load tag
		dt = 0.001			# time step for input ground motion
		
		maxNumIter = 10

		Tol=1e-3
		
		ops.timeSeries('Constant', 1, '-factor',1)

		ops.pattern('Plain', 1, 1)
		
		FX=self.config.g[0]
		FY=self.config.g[1]
		FZ=self.config.g[2]   
		for node_num in range(0,len(self.nodeList)):
			NM=ops.nodeMass(self.nodeList[node_num], 1)	
			if self.config.SeesModelType=="solid":
				ops.load(self.nodeList[node_num], NM*FX, NM*FY, NM*FZ)
			else:
				ops.load(self.nodeList[node_num], NM*FX, NM*FY, NM*FZ, 0.0, 0., 0.0) 
	
	if config.runPrelim=='Yes':
		ops.constraints('Transformation')
		ops.numberer('Plain')
		ops.system('BandGeneral')
		ops.test('EnergyIncr', Tol, maxNumIter)
		ops.algorithm('ModifiedNewton')
		NewmarkGamma = 0.5
		NewmarkBeta = 0.25
		ops.integrator('Newmark', NewmarkGamma, NewmarkBeta)
		ops.analysis('VariableTransient')
		DtAnalysis = 0.01
		TmaxAnalysis = 100
		Nsteps =  int(TmaxAnalysis/ DtAnalysis)

		ops.algorithm('KrylovNewton')

		ok = ops.analyze(Nsteps, DtAnalysis,DtAnalysis/10,DtAnalysis,100)	
		ops.loadConst('-time',0)  
		
		for node_num in range(0,len(self.nodeList)):
			ops.setNodeVel(self.nodeList[node_num], 1, 0.0, '-commit')
			ops.setNodeVel(self.nodeList[node_num], 2, 0.0, '-commit')
			ops.setNodeVel(self.nodeList[node_num], 3, 0.0, '-commit')
			# ops.setNodeAccel(self.nodeList[node_num], 1, 0.0, '-commit')
			# ops.setNodeAccel(self.nodeList[node_num], 2, 0.0, '-commit')
			# ops.setNodeAccel(self.nodeList[node_num], 3, 0.0, '-commit')

	nope=1
def runPreliminaryAnalysis(self):
	res=['disp','vel','accel','incrDisp','reaction','pressure','unbalancedLoad','mass']
	
	
	os.system('rm -rf SeesoutPrelim')
	os.system('mkdir SeesoutPrelim')
	os.system('touch SeesoutPrelim.pvd')
	ops.recorder('PVD', 'SeesoutPrelim', '-precision', 4, '-dT', 0.01, *res)
	Tol=1e-3
	maxNumIter = 10
	#ops.pattern('UniformExcitation', IDloadTag, GMdirection, '-accel', 2)
	ops.constraints('Transformation')
	ops.numberer('Plain')
	ops.system('BandGeneral')
	ops.test('EnergyIncr', Tol, maxNumIter)
	ops.algorithm('ModifiedNewton')
	NewmarkGamma = 0.5
	NewmarkBeta = 0.25
	ops.integrator('Newmark', NewmarkGamma, NewmarkBeta)
	ops.analysis('VariableTransient')
	DtAnalysis = 0.001
	TmaxAnalysis = 10
	Nsteps =  int(TmaxAnalysis/ DtAnalysis)
	ok=1
	# for i in test:
	ops.algorithm('KrylovNewton')
	
	# ok = ops.analyze(Nsteps, DtAnalysis,DtAnalysis/10,DtAnalysis,1)
	
	# ops.wipeAnalysis
	ops.database('File',"SeesCheckpoints/checkpoint")
	ops.save(0)
	nope=1
