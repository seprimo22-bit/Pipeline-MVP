from flask import Flask, request, jsonify

import datetime

app = Flask(name)

class HybridPipeline:def __init__(self):

    self.vectors = {

        "TimePressure": 0.0,

        "InfoCompleteness": 0.0,

        "Reversibility": 0.0,

        "EntropyRisk": 0.0,

        "AgencyControl": 0.0,

        "StakeAsymmetry": 0.0,

        "ConstraintDensity": 0.0,

        "Alignment": 0.0

    }

def paper_zero(self, text):

    text_lower = text.lower()

    hedge = sum(

        1 for w in ["maybe", "perhaps", "might"]

        if w in text_lower

    )

    is_decision = "should i" in text_lower

    return {

        "intent": "DECISION" if is_decision else "INQUIRY",

        "hedge_density": hedge,

        "cleaned": text

    }

def run(self, text):

    pz = self.paper_zero(text)

    if "urgent" in text.lower():

        self.vectors["TimePressure"] = 7

    if "should i" in text.lower():

        self.vectors["AgencyControl"] = 5

    tension = sum(self.vectors.values()) / 8

    return {

        "timestamp": str(datetime.datetime.now()),

        "paper_zero": pz,

        "vectors": self.vectors,

        "tension_score": round(tension, 2),

        "classification": (

            "DECISION_READY"

            if pz["intent"] == "DECISION"

            else "INFORMATIONAL"

        )

    }
