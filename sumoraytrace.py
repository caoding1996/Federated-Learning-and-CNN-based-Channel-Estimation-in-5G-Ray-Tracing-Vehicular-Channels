import os, sys
import traci
import math
import ssl
import matlab.engine

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

sumoBinary = 'C:/Program Files (x86)/Eclipse/Sumo/bin/sumo-gui'
# sumoBinary = 'C:/Program Files (x86)/Eclipse/Sumo/bin/sumo' ## Use this code to hide sumo visualization
sumoCmd = [sumoBinary, "-c", "TST_total/osm.sumocfg", "--no-step-log", "true", "-W"]

traci.start(sumoCmd)

Time = 100
VehIDlist = []
Geopositionnlist = []
transmitterlist = []
receiverlist = []
numrt = 0

for step in range(Time):
  traci.simulationStep()
  VehIDlist = traci.vehicle.getIDList()
  for VehID in VehIDlist:
    Positionx, Positiony = traci.vehicle.getPosition(VehID)    #  Get the position of the sender and receiver in the SUMO coordinate system
    lon, lat = traci.simulation.convertGeo(Positionx, Positiony)  #  Get the latitude and longitude of the sender and receiver in the Geo coordinate system
    Geopositionnlist.append([lat, lon])
# print(Geopositionnlist)
traci.close(False)

for i in range (len(Geopositionnlist)-1):
    if i%2==0:
        transmitterlist.append(Geopositionnlist[i])
        receiverlist.append(Geopositionnlist[i+1])

# save the Geo coordinate of transmitters and receivers.
with open('transmitter.txt', 'w') as ftx:
    ftx.write(str(transmitterlist))
    ftx.close()
with open('receiver.txt', 'w') as frx:
    frx.write(str(receiverlist))
    frx.close()
# print(transmitterlist[0][0], transmitterlist[0][1], receiverlist[0][0], receiverlist[0][1])

hperchanlist = []
# python matlab engine to start ray tracing process.
print("start matlab ray tracing")
eng = matlab.engine.start_matlab()
#for j in range(len(transmitterlist)):
for j in range(len(transmitterlist)):
  hperchan = eng.rtchannel(transmitterlist[j][0], transmitterlist[j][1], receiverlist[j][0], receiverlist[j][1], numrt, nargout=1)
  numrt+=1

with open('hperfect','w') as fhper:
    fhper.write(str(hperchanlist))
    fhper.close()
