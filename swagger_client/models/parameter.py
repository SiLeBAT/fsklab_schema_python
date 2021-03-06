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

class Parameter(object):
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
        'id': 'str',
        'classification': 'str',
        'name': 'str',
        'description': 'str',
        'unit': 'str',
        'unit_category': 'str',
        'data_type': 'str',
        'source': 'str',
        'subject': 'str',
        'distribution': 'str',
        'value': 'str',
        'reference': 'Reference',
        'variability_subject': 'str',
        'min_value': 'str',
        'max_value': 'str',
        'error': 'str'
    }

    attribute_map = {
        'id': 'id',
        'classification': 'classification',
        'name': 'name',
        'description': 'description',
        'unit': 'unit',
        'unit_category': 'unitCategory',
        'data_type': 'dataType',
        'source': 'source',
        'subject': 'subject',
        'distribution': 'distribution',
        'value': 'value',
        'reference': 'reference',
        'variability_subject': 'variabilitySubject',
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'error': 'error'
    }

    def __init__(self, id=None, classification=None, name=None, description=None, unit=None, unit_category=None, data_type=None, source=None, subject=None, distribution=None, value=None, reference=None, variability_subject=None, min_value=None, max_value=None, error=None):  # noqa: E501
        """Parameter - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._classification = None
        self._name = None
        self._description = None
        self._unit = None
        self._unit_category = None
        self._data_type = None
        self._source = None
        self._subject = None
        self._distribution = None
        self._value = None
        self._reference = None
        self._variability_subject = None
        self._min_value = None
        self._max_value = None
        self._error = None
        self.discriminator = None
        self.id = id
        self.classification = classification
        self.name = name
        if description is not None:
            self.description = description
        self.unit = unit
        if unit_category is not None:
            self.unit_category = unit_category
        self.data_type = data_type
        if source is not None:
            self.source = source
        if subject is not None:
            self.subject = subject
        if distribution is not None:
            self.distribution = distribution
        if value is not None:
            self.value = value
        if reference is not None:
            self.reference = reference
        if variability_subject is not None:
            self.variability_subject = variability_subject
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if error is not None:
            self.error = error

    @property
    def id(self):
        """Gets the id of this Parameter.  # noqa: E501

        An unambiguous ID given to each of the parameters - preferably autogenerated by a software tool and compatible with SBML ID requirements, only letters from A to Z, numbers and '_'  # noqa: E501

        :return: The id of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Parameter.

        An unambiguous ID given to each of the parameters - preferably autogenerated by a software tool and compatible with SBML ID requirements, only letters from A to Z, numbers and '_'  # noqa: E501

        :param id: The id of this Parameter.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def classification(self):
        """Gets the classification of this Parameter.  # noqa: E501

        General classification of the parameter (e.g. Input, Constant, Output...)  # noqa: E501

        :return: The classification of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this Parameter.

        General classification of the parameter (e.g. Input, Constant, Output...)  # noqa: E501

        :param classification: The classification of this Parameter.  # noqa: E501
        :type: str
        """
        if classification is None:
            raise ValueError("Invalid value for `classification`, must not be `None`")  # noqa: E501
        allowed_values = ["CONSTANT", "INPUT", "OUTPUT"]  # noqa: E501
        if classification not in allowed_values:
            raise ValueError(
                "Invalid value for `classification` ({0}), must be one of {1}"  # noqa: E501
                .format(classification, allowed_values)
            )

        self._classification = classification

    @property
    def name(self):
        """Gets the name of this Parameter.  # noqa: E501

        A name given to the parameter  # noqa: E501

        :return: The name of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.

        A name given to the parameter  # noqa: E501

        :param name: The name of this Parameter.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Parameter.  # noqa: E501

        General description of the parameter  # noqa: E501

        :return: The description of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parameter.

        General description of the parameter  # noqa: E501

        :param description: The description of this Parameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unit(self):
        """Gets the unit of this Parameter.  # noqa: E501

        Unit of the parameter  # noqa: E501

        :return: The unit of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Parameter.

        Unit of the parameter  # noqa: E501

        :param unit: The unit of this Parameter.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def unit_category(self):
        """Gets the unit_category of this Parameter.  # noqa: E501

        Empty  # noqa: E501

        :return: The unit_category of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._unit_category

    @unit_category.setter
    def unit_category(self, unit_category):
        """Sets the unit_category of this Parameter.

        Empty  # noqa: E501

        :param unit_category: The unit_category of this Parameter.  # noqa: E501
        :type: str
        """

        self._unit_category = unit_category

    @property
    def data_type(self):
        """Gets the data_type of this Parameter.  # noqa: E501

        Information on the data format of the parameter, e.g. if it the input parameter is a file location or a date or a number. This is important for software tools interpreting the metadata and generate user interfaces for parameter input.  # noqa: E501

        :return: The data_type of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Parameter.

        Information on the data format of the parameter, e.g. if it the input parameter is a file location or a date or a number. This is important for software tools interpreting the metadata and generate user interfaces for parameter input.  # noqa: E501

        :param data_type: The data_type of this Parameter.  # noqa: E501
        :type: str
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["INTEGER", "DOUBLE", "NUMBER", "DATE", "FILE", "BOOLEAN", "VECTOROFNUMBERS", "VECTOROFSTRINGS", "MATRIXOFNUMBERS", "MATRIXOFSTRINGS", "OBJECT", "STRING"]  # noqa: E501
        if data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def source(self):
        """Gets the source of this Parameter.  # noqa: E501

        Information on the type of knowledge used to define the parameter value  # noqa: E501

        :return: The source of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Parameter.

        Information on the type of knowledge used to define the parameter value  # noqa: E501

        :param source: The source of this Parameter.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def subject(self):
        """Gets the subject of this Parameter.  # noqa: E501

        Scope of the parameter, e.g. if it refers to an animal, a batch of animals, a batch of products, a carcass, a carcass skin etc  # noqa: E501

        :return: The subject of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Parameter.

        Scope of the parameter, e.g. if it refers to an animal, a batch of animals, a batch of products, a carcass, a carcass skin etc  # noqa: E501

        :param subject: The subject of this Parameter.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def distribution(self):
        """Gets the distribution of this Parameter.  # noqa: E501

        Distribution describing the parameter variabilty. If no distribution selected this means the value provided in \"Parameter value\" is a point estimate. In case a distribution is selected the value provided in \"Parameter value\" is a string that the model code can parse in order to sample from the named distribution  # noqa: E501

        :return: The distribution of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this Parameter.

        Distribution describing the parameter variabilty. If no distribution selected this means the value provided in \"Parameter value\" is a point estimate. In case a distribution is selected the value provided in \"Parameter value\" is a string that the model code can parse in order to sample from the named distribution  # noqa: E501

        :param distribution: The distribution of this Parameter.  # noqa: E501
        :type: str
        """

        self._distribution = distribution

    @property
    def value(self):
        """Gets the value of this Parameter.  # noqa: E501

        A default value for the parameter. This is mandatory (needs to be provided) for all parameters of type 'Input'  # noqa: E501

        :return: The value of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Parameter.

        A default value for the parameter. This is mandatory (needs to be provided) for all parameters of type 'Input'  # noqa: E501

        :param value: The value of this Parameter.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def reference(self):
        """Gets the reference of this Parameter.  # noqa: E501


        :return: The reference of this Parameter.  # noqa: E501
        :rtype: Reference
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Parameter.


        :param reference: The reference of this Parameter.  # noqa: E501
        :type: Reference
        """

        self._reference = reference

    @property
    def variability_subject(self):
        """Gets the variability_subject of this Parameter.  # noqa: E501

        Information 'per what' the variability is described. It can be variability between broiler in a flock,  variability between all meat packages sold, variability between days, etc.  # noqa: E501

        :return: The variability_subject of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._variability_subject

    @variability_subject.setter
    def variability_subject(self, variability_subject):
        """Sets the variability_subject of this Parameter.

        Information 'per what' the variability is described. It can be variability between broiler in a flock,  variability between all meat packages sold, variability between days, etc.  # noqa: E501

        :param variability_subject: The variability_subject of this Parameter.  # noqa: E501
        :type: str
        """

        self._variability_subject = variability_subject

    @property
    def min_value(self):
        """Gets the min_value of this Parameter.  # noqa: E501

        Numerical value of the minimum limit of the parameter that determines the range of applicability for which the model applies  # noqa: E501

        :return: The min_value of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this Parameter.

        Numerical value of the minimum limit of the parameter that determines the range of applicability for which the model applies  # noqa: E501

        :param min_value: The min_value of this Parameter.  # noqa: E501
        :type: str
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this Parameter.  # noqa: E501

        Numerical value of the maximum limit of the parameter that determines the range of applicability for which the model applies  # noqa: E501

        :return: The max_value of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this Parameter.

        Numerical value of the maximum limit of the parameter that determines the range of applicability for which the model applies  # noqa: E501

        :param max_value: The max_value of this Parameter.  # noqa: E501
        :type: str
        """

        self._max_value = max_value

    @property
    def error(self):
        """Gets the error of this Parameter.  # noqa: E501

        Error of the parameter value  # noqa: E501

        :return: The error of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Parameter.

        Error of the parameter value  # noqa: E501

        :param error: The error of this Parameter.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(Parameter, dict):
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
        if not isinstance(other, Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
