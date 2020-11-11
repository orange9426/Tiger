from env.tiger.tiger import Tiger


def init_env(env_name):
    if env_name == 'Tiger':
        return Tiger()
    else:
        raise ValueError('Unknown environment: %s' % env_name)
