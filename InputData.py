#Question 1
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03     #annual discount rate

PSA_ON = False      # if probabilistic sensitivity analysis is on

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

# annual cost of each health state
ANNUAL_STATE_COST = [
    0,   # Well
    200, #Post Stroke
    5000,   # Stroke
    0,    # Dead
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.0,   # Well
    0.90,   # Post-Stroke
    0.8665,  #Stroke
    0.0    # Dead
    ]

# annual drug costs
ANTICOAG_COST = 2,000
NONE_COST = 0
