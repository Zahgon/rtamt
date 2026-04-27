from rtamt.explanation.stl.discrete_time.explainer import STLExplainer
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification
from rtamt.syntax.ast.parser.stl.specification_parser import StlAst
from rtamt.semantics.stl.discrete_time.offline.interpreter import StlDiscreteTimeOfflineInterpreter
from rtamt.semantics.stl.discrete_time.online.interpreter import StlDiscreteTimeOnlineInterpreter
from rtamt.semantics.iastl.discrete_time.online.interpreter import IAStlOutputRobustnessDiscreteTimeOnlineInterpreter, IAStlInputRobustnessDiscreteTimeOnlineInterpreter, IAStlInputVacuityDiscreteTimeOnlineInterpreter, IAStlOutputVacuityDiscreteTimeOnlineInterpreter
from rtamt.semantics.iastl.discrete_time.offline.interpreter import IAStlOutputRobustnessDiscreteTimeOfflineInterpreter, IAStlInputRobustnessDiscreteTimeOfflineInterpreter, IAStlInputVacuityDiscreteTimeOfflineInterpreter, IAStlOutputVacuityDiscreteTimeOfflineInterpreter
from rtamt.semantics.enumerations.options import *
from rtamt.pastifier.stl.pastifier import StlPastifier

def StlDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    pass

def StlDiscreteTimeOfflineSpecification():
    pass

def StlDiscreteTimeOnlineSpecification():
    pass

def StlDiscreteTimeOnlineSpecificationCpp():
    pass