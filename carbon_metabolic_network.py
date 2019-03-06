#!usr/bin/python3

import cobra
import cobra.test
from cobra.flux_analysis import flux_variability_analysis

def build_model():
    # create empty model
    model = cobra.Model('carbon')

    # create metabolites
    metabolite_A = cobra.Metabolite('A', compartment = 'c')
    metabolite_B = cobra.Metabolite('B', compartment = 'c')
    metabolite_C = cobra.Metabolite('C', compartment = 'c')
    metabolite_D = cobra.Metabolite('D', compartment = 'c')
    metabolite_E = cobra.Metabolite('E', compartment = 'c')
    metabolite_F = cobra.Metabolite('F', compartment = 'c')
    metabolite_G = cobra.Metabolite('G', compartment = 'c')
    metabolite_H = cobra.Metabolite('H', compartment = 'c')
    metabolite_D_ext = cobra.Metabolite('D_ext', compartment = 'e')
    metabolite_E_ext = cobra.Metabolite('E_ext', compartment = 'e')
    metabolite_F_ext = cobra.Metabolite('F_ext', compartment = 'e')
    metabolite_H_ext = cobra.Metabolite('H_ext', compartment = 'e')
    atp = cobra.Metabolite('ATP', compartment = 'c')
    nadh = cobra.Metabolite('NADH', compartment = 'c')
    oxigen = cobra.Metabolite('O2', compartment = 'c')
    oxigen_ext = cobra.Metabolite('O2_ext', compartment = 'e')
    carbon_1 = cobra.Metabolite('carbon_1', compartment = 'e')
    carbon_2 = cobra.Metabolite('carbon_2', compartment = 'e')
    biomass = cobra.Metabolite('biomass', compartment = 'c')

    # build reactions
    T_c_1 = cobra.Reaction('Tc1')
    T_c_1.add_metabolites({
        carbon_1: -1.0,
        metabolite_A: 1.0
    })
    T_c_1.lower_bound = 0.
    T_c_1.upper_bound = 10.5

    T_c_2 = cobra.Reaction('Tc2')
    T_c_2.add_metabolites({
        carbon_2: -1.0,
        metabolite_A: 1.0
    })
    T_c_2.lower_bound = 0.
    T_c_2.upper_bound = 10.5

    T_f = cobra.Reaction('Tf')
    T_f.add_metabolites({
        metabolite_F_ext: -1.0,
        metabolite_F: 1.0,
    })
    T_f.lower_bound = 0.
    T_f.upper_bound = 5.

    T_h = cobra.Reaction('Th')
    T_h.add_metabolites({
        metabolite_H_ext: -1.0,
        metabolite_H: 1.0,
    })
    T_h.lower_bound = 0.
    T_h.upper_bound = 5.

    T_o2 = cobra.Reaction('To2')
    T_o2.add_metabolites({
        oxigen_ext: -1.0,
        oxigen: 1.0,
    })
    T_o2.lower_bound = 0.
    T_o2.upper_bound = 15.

    T_d = cobra.Reaction('Td')
    T_d.add_metabolites({
        metabolite_D: -1.0,
        metabolite_D_ext: 1.0,
    })
    T_d.lower_bound = 0.
    T_d.upper_bound = 1000.

    T_e = cobra.Reaction('Te')
    T_e.add_metabolites({
        metabolite_E: -1.0,
        metabolite_E_ext: 1.0,
    })
    T_e.lower_bound = 0.
    T_e.upper_bound = 12.

    r_1 = cobra.Reaction('R_1')
    r_1.add_metabolites({
        metabolite_A: -1.0,
        atp: -1.0,
        metabolite_B: 1.0
    })
    r_1.lower_bound = 0.
    r_1.upper_bound = 12.

    r_2 = cobra.Reaction('R_2')
    r_2.add_metabolites({
        metabolite_C: 1.0,
        atp: 2.0,
        nadh: 2.0,
        metabolite_B: -1.0
    })
    r_2.lower_bound = -1000.
    r_2.upper_bound = 1000.

    r_3 = cobra.Reaction('R_3')
    r_3.add_metabolites({
        metabolite_F: 1.0,
        metabolite_B: -1.0
    })
    r_3.lower_bound = 0.
    r_3.upper_bound = 1000.

    r_4 = cobra.Reaction('R_4',)
    r_4.add_metabolites({
        metabolite_G: 1.0,
        metabolite_C: -1.0
    })
    r_4.lower_bound = 0.
    r_4.upper_bound = 1000.

    r_5_a = cobra.Reaction('R_5_a')
    r_5_a.add_metabolites({
        metabolite_C: 0.8,
        nadh: 2.0,
        metabolite_G: -1.0
    })
    r_5_a.lower_bound = 0.
    r_5_a.upper_bound = 1000.

    r_5_b = cobra.Reaction('R_5_b')
    r_5_b.add_metabolites({
        metabolite_C: 0.8,
        nadh: 2.0,
        metabolite_G: -1.0
    })
    r_5_b.lower_bound = 0.
    r_5_b.upper_bound = 1000.

    r_6 = cobra.Reaction('R_6')
    r_6.add_metabolites({
        metabolite_C: -1.0,
        atp: 2.0,
        metabolite_D: 3.0
    })
    r_6.lower_bound = 0.
    r_6.upper_bound = 1000.

    r_7 = cobra.Reaction('R_7')
    r_7.add_metabolites({
        metabolite_C: -1.0,
        nadh: -4.0,
        metabolite_E: 1.0
    })
    r_7.lower_bound = 0.
    r_7.upper_bound = 1000.

    r_8 = cobra.Reaction('R_8')
    r_8.add_metabolites({
        metabolite_G: -1.0,
        atp: -1.0,
        nadh: -2.0,
        metabolite_H: 1.0
    })
    r_8.lower_bound = -1000.
    r_8.upper_bound = 1000.

    r_res = cobra.Reaction('R_res')
    r_res.add_metabolites({
        oxigen: -1.0,
        nadh: -1.0,
        atp: 1.0
    })
    r_res.lower_bound = 0.
    r_res.upper_bound = 1000.

    biomass_reaction = cobra.Reaction('Growth')
    biomass_reaction.add_metabolites({
        metabolite_C: -1.0,
        metabolite_F: -1.0,
        metabolite_H: -1.0,
        atp: -10.0,
        biomass: 1.0,
    })
    biomass_reaction.lower_bound = 0.
    biomass_reaction.upper_bound = 1000.


    # pass reactions+metabolites to the model
    reactions = [T_c_1, T_c_2, T_f, T_h, T_o2, T_d, T_e, r_1, r_2,
                 r_3, r_4, r_5_a, r_5_b, r_6, r_7, r_8, r_res, biomass_reaction]
    model.add_reactions(reactions)

    #add boundary reactions
    model.add_boundary(model.metabolites.carbon_1, type="exchange", ub=10.5)
    model.add_boundary(model.metabolites.carbon_2, type="exchange", ub=10.5)
    model.add_boundary(model.metabolites.H_ext, type="exchange", ub=5)
    model.add_boundary(model.metabolites.F_ext, type="exchange", ub=5)
    model.add_boundary(model.metabolites.O2_ext, type="exchange", ub=15)
    model.add_boundary(model.metabolites.E_ext, type="demand", ub=12)
    model.add_boundary(model.metabolites.D_ext, type="demand", ub=12)
    model.add_boundary(model.metabolites.biomass, type="demand")

    # set biomass production as objective
    model.objective = 'Growth'

    return model


def main():
    print('================ SUBTASK 1: Building the Model ================')
    model = build_model()
    print("Reactions")
    print("---------")
    for x in model.reactions:
        print(f"{x.id}:{x.reaction}")

    print("")
    print("Metabolites")
    print("-----------")
    for x in model.metabolites:
        print(x.id)

    print('\n================ SUBTASK 2: Computing the maximum flow through the growth reaction ================\n')
    solution = model.optimize()
    print(model.summary())

    print('\n================ SUBTASK 3: FVA ================\n')
    fva = flux_variability_analysis(model)
    print(fva)

    print('\n================ SUBTASK 4: Find essential reactions ================\n')
    #Knock out each reaction. If the objective value is 0, the reaction is essential.
    for reaction in model.reactions:
        with model as model:
            reaction.knock_out()
            model.optimize()
            if round(model.objective.value,6) == 0:
                print(f"{reaction.id} blocked, new growth rate {round(model.objective.value,6)} -------> ESSENTIAL")
            else:
                print(f"{reaction.id} blocked, new growth rate {round(model.objective.value,6)}")


if __name__ == "__main__":
    main()
