from opentelemetry import trace
from opentelemetry import metrics

from random import randint
from flask import Flask

#Create tracer and tag it with the name of the flow
tracer = trace.get_tracer("diceroller.tracer")

#Create a meter to record metrics
meter = metrics.get_meter("diceroller.meter")

roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)

app = Flask(__name__)

@app.route("/rolldice")
def roll_dice():
    return str(do_roll())

def do_roll():
    with tracer.start_as_current_span("do_roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        #Add 1 to counter for given roll value
        roll_counter.add(1, {"roll.value": res})
    return res
