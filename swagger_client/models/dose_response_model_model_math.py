# coding: utf-8

"""
    RAKIP Generic model

    TODO  # noqa: E501

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DoseResponseModelModelMath(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'parameter': 'list[Parameter]',
        'quality_measures': 'list[QualityMeasures]',
        'model_equation': 'list[ModelEquation]',
        'fitting_procedure': 'str',
        'exposure': 'Exposure',
        'event': 'list[str]'
    }

    attribute_map = {
        'parameter': 'parameter',
        'quality_measures': 'qualityMeasures',
        'model_equation': 'modelEquation',
        'fitting_procedure': 'fittingProcedure',
        'exposure': 'exposure',
        'event': 'event'
    }

    def __init__(self, parameter=None, quality_measures=None, model_equation=None, fitting_procedure=None, exposure=None, event=None):  # noqa: E501
        """DoseResponseModelModelMath - a model defined in Swagger"""  # noqa: E501
        self._parameter = None
        self._quality_measures = None
        self._model_equation = None
        self._fitting_procedure = None
        self._exposure = None
        self._event = None
        self.discriminator = None
        self.parameter = parameter
        if quality_measures is not None:
            self.quality_measures = quality_measures
        if model_equation is not None:
            self.model_equation = model_equation
        if fitting_procedure is not None:
            self.fitting_procedure = fitting_procedure
        if exposure is not None:
            self.exposure = exposure
        if event is not None:
            self.event = event

    @property
    def parameter(self):
        """Gets the parameter of this DoseResponseModelModelMath.  # noqa: E501


        :return: The parameter of this DoseResponseModelModelMath.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this DoseResponseModelModelMath.


        :param parameter: The parameter of this DoseResponseModelModelMath.  # noqa: E501
        :type: list[Parameter]
        """
        if parameter is None:
            raise ValueError("Invalid value for `parameter`, must not be `None`")  # noqa: E501

        self._parameter = parameter

    @property
    def quality_measures(self):
        """Gets the quality_measures of this DoseResponseModelModelMath.  # noqa: E501


        :return: The quality_measures of this DoseResponseModelModelMath.  # noqa: E501
        :rtype: list[QualityMeasures]
        """
        return self._quality_measures

    @quality_measures.setter
    def quality_measures(self, quality_measures):
        """Sets the quality_measures of this DoseResponseModelModelMath.


        :param quality_measures: The quality_measures of this DoseResponseModelModelMath.  # noqa: E501
        :type: list[QualityMeasures]
        """

        self._quality_measures = quality_measures

    @property
    def model_equation(self):
        """Gets the model_equation of this DoseResponseModelModelMath.  # noqa: E501


        :return: The model_equation of this DoseResponseModelModelMath.  # noqa: E501
        :rtype: list[ModelEquation]
        """
        return self._model_equation

    @model_equation.setter
    def model_equation(self, model_equation):
        """Sets the model_equation of this DoseResponseModelModelMath.


        :param model_equation: The model_equation of this DoseResponseModelModelMath.  # noqa: E501
        :type: list[ModelEquation]
        """

        self._model_equation = model_equation

    @property
    def fitting_procedure(self):
        """Gets the fitting_procedure of this DoseResponseModelModelMath.  # noqa: E501


        :return: The fitting_procedure of this DoseResponseModelModelMath.  # noqa: E501
        :rtype: str
        """
        return self._fitting_procedure

    @fitting_procedure.setter
    def fitting_procedure(self, fitting_procedure):
        """Sets the fitting_procedure of this DoseResponseModelModelMath.


        :param fitting_procedure: The fitting_procedure of this DoseResponseModelModelMath.  # noqa: E501
        :type: str
        """

        self._fitting_procedure = fitting_procedure

    @property
    def exposure(self):
        """Gets the exposure of this DoseResponseModelModelMath.  # noqa: E501


        :return: The exposure of this DoseResponseModelModelMath.  # noqa: E501
        :rtype: Exposure
        """
        return self._exposure

    @exposure.setter
    def exposure(self, exposure):
        """Sets the exposure of this DoseResponseModelModelMath.


        :param exposure: The exposure of this DoseResponseModelModelMath.  # noqa: E501
        :type: Exposure
        """

        self._exposure = exposure

    @property
    def event(self):
        """Gets the event of this DoseResponseModelModelMath.  # noqa: E501


        :return: The event of this DoseResponseModelModelMath.  # noqa: E501
        :rtype: list[str]
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this DoseResponseModelModelMath.


        :param event: The event of this DoseResponseModelModelMath.  # noqa: E501
        :type: list[str]
        """

        self._event = event

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DoseResponseModelModelMath, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DoseResponseModelModelMath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other