from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.core import Qos, Policy
from cyclonedds.pub import DataWriter
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic
from cyclonedds.idl import IdlStruct
from cyclonedds.idl.annotations import key
from time import sleep, time
from datetime import datetime
import numpy as np
try:
    from names import get_full_name
    name = get_full_name()
except:
    import os
    name = f"{os.getpid()}"

# C, C++ require using IDL, Python doesn't
@dataclass
class Chatter(IdlStruct, typename="Chatter"):
    name: str
    key("name")
    message: str
    count: int
    timestamp: str  # Add timestamp field

rng = np.random.default_rng()
dp = DomainParticipant()
tp = Topic(dp, "Hello", Chatter, qos=Qos(Policy.Reliability.Reliable(0)))
dw = DataWriter(dp, tp)
dr = DataReader(dp, tp)

count = 0
num_messages = 100  # Number of messages to calculate frequency over
start_time = time()

while True:
    timestamp = datetime.now().isoformat()  # Get current timestamp
    sample = Chatter(name=name, message="Hello, World!", count=count, timestamp=timestamp)
    count += 1
    dw.write(sample)
    
    if count % num_messages == 0:
        end_time = time()
        elapsed_time = end_time - start_time
        frequency = num_messages / elapsed_time
        print(f"Frequency: {frequency:.2f} messages per second")
        start_time = end_time  # Reset start time for next frequency calculation

    for sample in dr.take(10):
        pass
    sleep(0.001)