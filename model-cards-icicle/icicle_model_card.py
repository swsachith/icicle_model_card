from dataclasses import dataclass, field
from typing import List
from dataclasses import dataclass


@dataclass
class AIModel:
    name: str
    version: str
    description: str
    owner: str
    location: str
    licence: str


@dataclass
class Metric:
    key: str
    value: str


@dataclass
class BiasAnalysis:
    name: str
    numbers: List[Metric] = field(default_factory=list)


@dataclass
class ExplainabilityAnalysis:
    name: str
    numbers: List[Metric] = field(default_factory=list)


@dataclass
class ModelCard:
    name: str
    version: str
    description: str
    author: str
    input_data: str
    output_data: str
    model: AIModel
    bias_analysis: BiasAnalysis
    xai_analysis: ExplainabilityAnalysis
