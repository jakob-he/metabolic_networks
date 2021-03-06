initCobraToolbox(false)
R1 = '39.43 ac + 35 o2 -> x';
R2 = '9.46 glcxt + 12.92 o2 -> x';
R3 = '9.84 glcxt + 12.73 o2 -> x';
R4 = '-19.23 glcxt -> 12.12 ac + x';


reactionIdentifiers = {'V1','V2','V3','V4'};
reactionNames = reactionIdentifiers;
reactionFormulas = {R1,R2,R3,R4};

revFlagList = [0,0,0,0];
upperBoundList = [1000,1000,1000,1000];
initConcentrations = [10.8 0.4 0.21];
initBiomass = 0.001;
timeStep = 0.001;
nSteps = 10000;
plotRxns = {'EX_ac[c]' 'EX_o2[c]' 'EX_glcxt[c]'};
exclUptakeRxns = {};

model1 = createModel(reactionIdentifiers,reactionNames,reactionFormulas,revFlagList, [0,0,0,0], upperBoundList);


model1 = addDemandReaction(model1, {'x[c]'});
model1 = addExchangeRxn(model1, {'ac[c]','o2[c]','glcxt[c]'},[-1000,-1000,-1000],[1000,1000,1000]);
model1 = changeObjective(model1,{'V1','V2','V3','V4'});


model1.rxns

substrateRxns = {'EX_ac[c]' 'EX_o2[c]' 'EX_glcxt[c]'};


[concentrationMatrix,excRxnNames,timeVec,biomassVec] = dynamicFBA(model1,substrateRxns,initConcentrations,initBiomass,timeStep,nSteps,plotRxns,exclUptakeRxns);