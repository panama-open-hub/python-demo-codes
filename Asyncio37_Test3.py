import tornado
from tornado import gen,ioloop, web
from tornado.gen import multi
from tornado.options import define, options
import logging
from datetime import datetime, date,timedelta

logging.basicConfig(filename='serverLogger.log',filemode='a',level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('tornado.access').disabled = True
define("port", default=8000, help="run on the given port", type=int)

async def bgTask():
    while True:
        try: 
           NOW = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           logging.debug(NOW)
           print(NOW)
           #await gen.sleep(3600)
           await gen.sleep(1)
        except Exception as ex:
           print(ex)
           print('exiting.')
           break 

async def runAll():
    tornado.options.parse_command_line()
    print("Listening at port 8000")
    logging.warning("Tornado server started listening")
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    await multi([bgTask()])

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class StopServer(tornado.web.RequestHandler):
    def get(self):
        tornado.ioloop.IOLoop.instance().stop()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', HomeHandler),
            (r"/stop", StopServer),
        ]
        tornado.web.Application.__init__(self, handlers)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().run_sync(runAll)