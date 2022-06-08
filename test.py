class PythonPlayer(object):

    def start(self,player):
        return player.firstping(self)

    def firstPong(self,player):
        return player.secondping(self)

    def secondPong(self):
        return "Success"

    class Java:
        implements = ["py4j.PongPlayer"]

# Start the JVM with "java -cp py4j.jar py4j.examples.ExampleApplication"
from py4j.java_gateway import JavaGateway, CallbackServerParameters
gateway = JavaGateway(callback_server_parameters=CallbackServerParameters())
# ping_player = gateway.jvm.py4j.examples.PingPlayer()
y=gateway.entry_point
pong_player = PythonPlayer()
print(pong_player.start(y))