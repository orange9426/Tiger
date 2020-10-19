from log import logger
from util.console import console
from util.divider import print_divider
from statistic.results import Results
from statistic.record_history import RecordHistory
import logging
import time
import tqdm


module = 'RUN'


def _play_game(env, solver, args):
    """Plays a game with policies solved by the solver."""
    solver.reset_for_epoch()

    history = solver.solve_game(env)

    return history


def run(env, solver, args):
    """Run multiple epochs as an experiment."""
    # Save all results in the experiment
    results = Results()

    print_divider('large')

    # Run for multiple epochs
    for epoch in tqdm.tqdm(range(args['n_epochs'])):
        # Show epochs progress
        print_divider('medium')
        console(2, module, "Epoch: " + str(epoch))

        epoch_start = time.time()

        # Play a game with policies solved by the solver
        history = _play_game(env, solver, args)

        # Record the results
        results.time.add(time.time() - epoch_start)
        results.update_reward_results(
            history.undiscounted_return(),
            history.discounted_return(args['discount'])
        )

        print_divider('medium')

    # Show the results
    results.show(args['n_epochs'])

    # Write the results to the log
    logger.result_logging(results, args)
