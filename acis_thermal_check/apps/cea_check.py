#!/usr/bin/env python

"""
========================
cea_check
========================

This code generates backstop load review outputs for checking the HRC
CEA temperature 1DPAMZT.  It also generates CEA model validation
plots comparing predicted values to telemetry for the previous three
weeks.
"""

# Matplotlib setup
# Use Agg backend for command-line (non-interactive) operation
import matplotlib
matplotlib.use('Agg')

import sys
from acis_thermal_check import \
    ACISThermalCheck, \
    get_options


class CEACheck(ACISThermalCheck):
    def __init__(self):
        valid_limits = {'2CEAHVPT': [(1, 2.0), (50, 1.0), (99, 2.0)],
                        'PITCH': [(1, 3.0), (99, 3.0)],
                        'TSCPOS': [(1, 2.5), (99, 2.5)]
                        }
        hist_limit = [20.0]
        limits_map = {}
        super(CEACheck, self).__init__("2ceahvpt", "cea", valid_limits,
                                       hist_limit, limits_map=limits_map)

    def _calc_model_supp(self, model, state_times, states, ephem, state0):
        """
        Update to initialize the cea0 pseudo-node. If 1dpamzt
        has an initial value (T_cea) - which it does at
        prediction time (gets it from state0), then T_cea0 
        is set to that.  If we are running the validation,
        T_cea is set to None so we use the dvals in model.comp

        NOTE: If you change the name of the dpa0 pseudo node you
              have to edit the new name into the if statement
              below.
        """
        if 'cea0' in model.comp:
            if state0 is None:
                T_cea0 = model.comp["2ceahvpt"].dvals
            else:
                T_cea0 = state0["2ceahvpt"]
            model.comp['cea0'].set_data(T_cea0, model.times)


def main():
    args = get_options()
    cea_check = CEACheck()
    try:
        cea_check.run(args)
    except Exception as msg:
        if args.traceback:
            raise
        else:
            print("ERROR:", msg)
            sys.exit(1)


if __name__ == '__main__':
    main()