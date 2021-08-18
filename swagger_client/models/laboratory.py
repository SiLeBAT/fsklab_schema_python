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

class Laboratory(object):
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
        'accreditation': 'list[str]',
        'name': 'str',
        'country': 'str'
    }

    attribute_map = {
        'accreditation': 'accreditation',
        'name': 'name',
        'country': 'country'
    }

    def __init__(self, accreditation=None, name=None, country=None):  # noqa: E501
        """Laboratory - a model defined in Swagger"""  # noqa: E501
        self._accreditation = None
        self._name = None
        self._country = None
        self.discriminator = None
        self.accreditation = accreditation
        if name is not None:
            self.name = name
        if country is not None:
            self.country = country

    @property
    def accreditation(self):
        """Gets the accreditation of this Laboratory.  # noqa: E501


        :return: The accreditation of this Laboratory.  # noqa: E501
        :rtype: list[str]
        """
        return self._accreditation

    @accreditation.setter
    def accreditation(self, accreditation):
        """Sets the accreditation of this Laboratory.


        :param accreditation: The accreditation of this Laboratory.  # noqa: E501
        :type: list[str]
        """
        if accreditation is None:
            raise ValueError("Invalid value for `accreditation`, must not be `None`")  # noqa: E501

        self._accreditation = accreditation

    @property
    def name(self):
        """Gets the name of this Laboratory.  # noqa: E501

        Laboratory code (National laboratory code if available) or Laboratory name  # noqa: E501

        :return: The name of this Laboratory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Laboratory.

        Laboratory code (National laboratory code if available) or Laboratory name  # noqa: E501

        :param name: The name of this Laboratory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def country(self):
        """Gets the country of this Laboratory.  # noqa: E501

        Country where the laboratory is placed. (ISO 3166-1-alpha-2)  # noqa: E501

        :return: The country of this Laboratory.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Laboratory.

        Country where the laboratory is placed. (ISO 3166-1-alpha-2)  # noqa: E501

        :param country: The country of this Laboratory.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if issubclass(Laboratory, dict):
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
        if not isinstance(other, Laboratory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other