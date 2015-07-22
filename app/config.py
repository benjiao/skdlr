import logging


class Config(object):
    LOG_FILE = 'tmp/scheduler.log'
    LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
    LOG_LEVEL = logging.DEBUG

    DAEMON_PID_FILE = '/tmp/schedservice.pid'
    DAEMON_OUT_LOG = '/var/log/schedservice.out.log'
    DAEMON_ERR_LOG = '/var/log/schedservice.err.log'

    DATABASE_URI = 'sqlite:///db/app.db'
    TEST_DATABASE_URI = 'sqlite:///db/test.db'
