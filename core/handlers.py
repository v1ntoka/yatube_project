from environs import Env


def get_environment():
    env = Env()
    env.read_env()
    ret = [env(i) for i in ['EMAIL_HOST', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD', 'EMAIL_PORT', 'EMAIL_USE_TLS']]
    return ret
