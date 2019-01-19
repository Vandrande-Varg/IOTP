import time
import json
import paho.mqtt.client as mqtt

mqtt_broker = "m2m.eclipse.org"
topic_cpu = "iotp/fanControl"
my_mqtt = None

def onMessage(client, userdata, message):
	m_decode=str(message.payload.decode("utf-8","ignore"))
	print(m_decode)
	first_arg = m_decode
	
	if((int(first_arg) != 0) and (int(first_arg) != 1)):
		print("first_arg brightness val: "+first_arg)
		f = open("brightness_variable.txt","w+")
		f.write(first_arg)
		f.close()
		print("brightness var file written")
	elif(int(first_arg) == 0) or (int(first_arg) == 1):
		print("first_arg on/off: "+first_arg)
		f = open("on_off_variable.txt","w+")
		f.write(first_arg)
		f.close()
		print("on off var file written")

def startMQTT():
	my_mqtt = mqtt.Client()
	my_mqtt.on_message = onMessage
	my_mqtt.connect(mqtt_broker, port=1883)
	my_mqtt.subscribe(topic_cpu, qos=1)
	my_mqtt.loop_start()
	print("Subscribed to topic")
	
def main():
	startMQTT()
	while True:
		time.sleep(2)

if __name__ == "__main__":
	main()
