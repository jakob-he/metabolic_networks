
%initCobraToolbox()
%global CBTDIR

%model = readCbModel([CBTDIR filesep 'test' filesep 'models' filesep 'Ecoli_central_network.mat']);


model.rxns
printRxnFormula(model);



%[{'Reaction ID', 'Lower Bound', 'Upper Bound'};...
%model.rxns, num2cell(model.lb), num2cell(model.ub)]

%Rxns,initConcentrations,initBiomass,timeStep,nSteps,plotRxns,exclUptakeRxns)