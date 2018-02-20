import logging
import datetime


class LoggingExceptionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_exception(self, request, exception):
        logger = logging.getLogger('ws_logger')
        logger.setLevel(logging.ERROR)
        logname = 'ws_logging/%s.log' % str(datetime.datetime.now().date())
        filehandler = logging.FileHandler(filename=logname, encoding="utf-8")
        fmter = logging.Formatter(fmt="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")
        filehandler.setFormatter(fmter)
        logger.addHandler(filehandler)
        logger.error('URL[%s] ' % request.get_full_path() + str(exception))

    def __call__(self, request):
        response = self.get_response(request)
        return response
