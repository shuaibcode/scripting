#Connecting to multiple devices.



import netmiko

from netmiko import ConnectHandler



#password = getpass()
Router1 = {
	"device_type": "cisco_ios",
	"ip":"192.168.1.18",
        "username":"admin",
        "password":"admin",
        "secret":"admin",                       
}
                        
Router2 = {
	"device_type": "cisco_ios",
        "ip":"192.168.1.17",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}

Router3 = {
	"device_type": "cisco_ios",
	"ip":"192.168.1.15",
        "username":"admin",
        "password":"admin",
        "secret":"admin",                       
}
                        
Router4 = {
	"device_type": "cisco_ios",
        "ip":"192.168.1.20",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}

Router5 = {
	"device_type": "cisco_ios",
	"ip":"192.168.1.21",
        "username":"admin",
        "password":"admin",
        "secret":"admin",                       
}
                        
Router6 = {
	"device_type": "cisco_ios",
        "ip":"192.168.1.19",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}

                        
Router7 = {
	"device_type": "cisco_ios",
        "ip":"192.168.1.16",
   	"username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}
  
print("********************TOTAL Devices SSH  throgh PYTHON SCRIPT************************")
print('##############################******###############')
print("Connecting to device :Router1,Router2,Router3,Router4,Router5 and Router6 and Router7")
  
device_list = [Router1,Router2,Router3,Router4,Router5,Router6,Router7]
 
for device in device_list:
        net_connect = ConnectHandler(**device)
        print(net_connect.find_prompt())
net_connect.disconnect()
print("configration of ospf from the follwing devices:R-2,R-6,R-7")

devices=[Router2,Router6,Router7]
verbose = True
for device in devices:

        print('##############################******########################################')
        print('')
        print(" Connecting to Device:R-2,R-6,R-7 " + device["ip"])
        net_connect = ConnectHandler(**device)
        prompter = net_connect.find_prompt()
        if '>' in prompter:
                net_connect.enable()
        output = net_connect.send_command('show run | sec ospf')
        ospf_commands = ['router ospf 100', 'net 0.0.0.0 255.255.255.255 area 0']
        if not 'router ospf' in output:
                print('OSPF is not enabled on device: ' + device["ip"])
                answer = input('Would you like you enable default OSPF settings on: ' + device ["ip"]+ ' <y/n> ')
                if answer == 'y':
                        output = net_connect.send_config_set(ospf_commands)
                        print(output)
                        print('OSPF is now configured!')   
                else:
                        print('No OSPF configurations have been made!')
        else:
           print("OSPF is already configured on device: " + device["ip"])

net_connect.disconnect()
print('')
        
  
print('##############################******########################################')
  
print("")
  
print(" Connecting to Device router 1: " + Router1["ip"])

Router1 = {
	"device_type": "cisco_ios",
                            
        "ip":"192.168.1.18",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}

net_connect = ConnectHandler(**Router1)
net_connect.enable()
config_command = ['interface ethernet 2/1','no shutdown','ip address 12.1.1.1 255.0.0.0','exit',
 
                  'interface ethernet 2/2','no shutdown','ip address 14.1.1.1 255.0.0.0','exit',
                  'interface ethernet 2/3','no shutdown','ip address 13.1.1.1 255.0.0.0','exit',
                  'interface ethernet 3/0','no shutdown','ip address 15.1.1.1 255.0.0.0','exit',
                  'router ospf 100','exit',         
                  'interface ethernet 3/0','ip ospf 100 area 0','exit',
                  'interface ethernet 2/3','ip ospf 100 area 0','exit',
                  'interface ethernet 2/1','ip ospf 100 area 0',
                  'interface loopback 1','ip address 1.1.1.1 255.255.255.255','exit',
                  'interface loopback 1','ip ospf 100 area 0','exit',
                  'router bgp 100','neighbor 3.3.3.3 remote-as 100',
                  'neighbor 3.3.3.3 update-source loopback1',
                  'exit','router ospf 100','redistribute bgp 100 subnets','exit']
                                                                                                                                                                                                       
                                                                                                                                                                                                         
output = net_connect.send_config_set(config_command)
print(output)
net_connect.disconnect()         

Router2 = {
	"device_type": "cisco_ios",
                            
        "ip":"192.168.1.17",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}
  
net_connect = ConnectHandler(**Router2)

net_connect.enable()
config_command = ['interface ethernet 2/2','no shutdown','ip address 12.1.1.2 255.0.0.0','exit',

                  'interface ethernet 2/1','no shutdown','ip address 23.1.1.2 255.0.0.0','exit']
                   

print("")
 
print('##############################******########################################')
 
print("")
 
print(" Connecting to Device Router 3: " + Router3["ip"])
 
 
                        
Router3 = {
	"device_type": "cisco_ios",
                            
        "ip":"192.168.1.15",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}

  
net_connect = ConnectHandler(**Router3)

net_connect.enable() 
config_command = ['interface ethernet 2/1','no shutdown','ip address 23.1.1.3 255.0.0.0','exit',
 	       'interface ethernet 2/3','no shutdown','ip address 24.1.1.3 255.0.0.0','exit',
 	       'interface ethernet 2/2','no shutdown','ip address 35.1.1.3 255.0.0.0','exit',
               'interface ethernet 3/0','no shutdown','ip address 25.1.1.3 255.0.0.0','exit',
 	       'interface loopback 1','ip address 3.3.3.3 255.255.255.255','exit',
               'router ospf 100','exit','interface ethernet 3/0','ip ospf 100 area 0','exit',    
               'interface loopback 1','ip ospf 100 area 0','exit',
               'interface ethernet 2/1','ip ospf 100 area 0','exit',
               'interface ethernet 2/3','ip ospf 100 area 0','exit',    
               'router bgp 100','neighbor 1.1.1.1 remote-as 100',
               'neighbor 1.1.1.1 update-source loopback 1',
	       'exit','router ospf 100','redistribute bgp 100 subnets','exit',
   	       'router bgp 100','neighbor 35.1.1.5 remote-as 65500']
                                    
                           
output = net_connect.send_config_set(config_command)
print('')
print(output)
net_connect.disconnect()                                                             
print('')

print('##############################******########################################')

print('')

print(" Connecting to Device Router 4: " + Router4["ip"])

Router4 = {
	"device_type": "cisco_ios",
                            
        "ip":"192.168.1.20",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}
net_connect = ConnectHandler(**Router4)

net_connect.enable() 

config_command = ['interface ethernet 2/1','no shutdown','ip address 14.1.1.4 255.0.0.0','exit',

                  'interface ethernet 2/2','no shutdown','ip address 10.1.1.1 255.0.0.0','exit',
                  
                  'router bgp 65500','neighbor 14.1.1.1 remote-as 100',
                  'neighbor 14.1.1.1 allowas-in','exit',
                  'router bgp 65500','network 10.1.1.0 mask 255.255.255.0']
                                                      
                                                         
                                  
                           
output = net_connect.send_config_set(config_command)
print('')
print(output)
net_connect.disconnect()                                                             
print('')

  
  
print('')

print('##############################******########################################')

print('')

print(" Connecting to Device Router 5: " + Router5["ip"])



Router5 = {
	"device_type": "cisco_ios",
                            
        "ip":"192.168.1.21",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}
net_connect = ConnectHandler(**Router5)

net_connect.enable() 

config_command = ['interface ethernet 2/1','no shutdown','ip address 35.1.1.5 255.0.0.0','exit',

                  'interface ethernet 2/2','no shutdown','ip address 10.1.2.1 255.255.255.0','exit',
                  'router bgp 65500','neighbor 35.1.1.3 remote-as 100',
                  'neighbor 35.1.1.3 allowas-in',
                  'network 10.1.2.0 mask 255.255.255.0']

  
                           
output = net_connect.send_config_set(config_command)
print('')
print(output)
net_connect.disconnect()                                                             
print('')
 


print('')

print('##############################******########################################')

print('')

print(" Connecting to Device Router 6: " + Router6["ip"])

Router6 = {
	"device_type": "cisco_ios",
                            
        "ip":"192.168.1.19",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}
net_connect = ConnectHandler(**Router6)

net_connect.enable() 
config_command = ['interface ethernet 2/1','no shutdown','ip address 15.1.1.6 255.0.0.0','exit',

                  'interface ethernet 2/2','no shutdown','ip address 25.1.1.6 255.0.0.0','exit',]
                           
output = net_connect.send_config_set(config_command)
print('')
print(output)
net_connect.disconnect()                                                             
print("")
print("")

print('##############################******########################################')

print("")

print(" Connecting to Device Router 7: " + Router7["ip"])

Router7 = {
	"device_type": "cisco_ios",
                            
        "ip":"192.168.1.16",
        "username":"admin",
        "password":"admin",
        "secret":"admin",
                                            
                                                
}
net_connect = ConnectHandler(**Router7)

net_connect.enable() 
config_command = ['interface ethernet 2/1','no shutdown','ip address 13.1.1.7 255.0.0.0','exit',

                  'interface ethernet 2/2','no shutdown','ip address 24.1.1.7 255.0.0.0','exit'] 

                          
output = net_connect.send_config_set(config_command)
print('')
print(output)
net_connect.disconnect()                                                             
print('')
print('')  
  
print('***************************************************************')
 
print('!!!!!!!!!!!!!!!!!!!!!script is Complete !!!!!!!!!!!!!!!!!!!!!!!')
 
 
 
  
  

