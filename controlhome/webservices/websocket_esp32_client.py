#Web Socket client
import websocket
import odoorpc

class bd_webserver(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #Prepare the connection to the server
        odoo = odoorpc.ODOO('localhost', port=8069)
        # Login
        odoo.login('controlhomedb', 'admin', 'admin')
        item = odoo.env['controlhome.monitoring'].search([('name','=',self.name)])
        odoo.env['controlhome.monitoring'].write(item,{'state':self.value})

#id = odoo.execute('controlhome.monitoring', 'search', [('name','=','Fire')])
#item= odoo.execute('controlhome.monitoring', 'read', id, ['state'])
#print(item)
#print(module)

class esp32_ws_client(object):

    def __init__(self, ip):
        self.ip = ip
        #self.variable = variable
        #self.value = value

    def writing(self,variable,value):
        try:
            ws = websocket.WebSocket()
            ws.connect("ws://%s/ws" % self.ip) #IP of the Web socket server
            ws.send("%s,%s" %(variable, value)) #Command to send msg to ESP32

            ws.close() #Close to connection of Socket
        except:
            print("Problem with the web server")

    def reading(self):
        try:
            ws = websocket.WebSocket()
            ws.connect("ws://%s/ws" % self.ip) #IP of the Web socket server
            variable, value = ws.recv().split(",") #Command to receive msg from ESP32
            ws.close() #Close to connection of Socket
            return (variable,value)
        except:
            print("Problem with the web server")

abc = esp32_ws_client("192.168.1.142")
varia, val = abc.reading()
print(varia)
print(val)

bd_webserver("Fire","On")
#abc.writing("Fire","Off")
