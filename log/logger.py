import logging
import logging.handlers
import os


LOG_DIR = 'log'

my_dir = os.path.dirname(__file__)


def init_logger(env_name, solver_name):
    """Init one logging object for each run."""
    my_logger = logging.getLogger(env_name + ':' + solver_name)

    # default log format has time, module name, and message
    my_format = "%(asctime)s - %(name)s - %(message)s"

    # set handler
    log_file = env_name + '.log'
    log_path = os.path.join(my_dir, '..', LOG_DIR, log_file)
    my_handler = logging.handlers.RotatingFileHandler(
        filename=log_path,
        maxBytes=10000000,
        backupCount=4)

    # set the format
    my_handler.setFormatter(logging.Formatter(my_format))

    # set default log level
    my_logger.setLevel(logging.DEBUG)

    # add a handler to the logger
    my_logger.addHandler(my_handler)


def result_logging(result, args):
    """Write the running result to the log."""
    logger = logging.getLogger(args['env'] + ':' + args['solver'])

    # Log the results for different solvers
    if args['solver'] == 'POMCP':
        logger.info('epochs: ' + str(args['n_epochs']) + '\t' +
                    'simulations: ' + str(args['n_sims']) + '\t' +
                    'uct_c: ' + str(args['uct_coefficient']) + '\t' +
                    'ave undiscounted return: ' + str(result.undiscounted_return.mean) +
                    ' +- ' + str(result.undiscounted_return.std_err()) + '\t' +
                    'ave discounted return: ' + str(result.discounted_return.mean) +
                    ' +- ' + str(result.discounted_return.std_err()) + '\t' +
                    'ave time/epoch: ' + str(result.time.mean))
