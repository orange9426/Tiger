from solver.pomcp.pomcp import POMCP


def init_solver(solver_name, args):
    if solver_name == 'POMCP':
        return POMCP(args)
