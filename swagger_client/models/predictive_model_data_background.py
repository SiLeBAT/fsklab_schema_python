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

class PredictiveModelDataBackground(object):
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
        'study': 'Study',
        'study_sample': 'list[StudySample]',
        'laboratory': 'list[Laboratory]',
        'assay': 'list[Assay]'
    }

    attribute_map = {
        'study': 'study',
        'study_sample': 'studySample',
        'laboratory': 'laboratory',
        'assay': 'assay'
    }

    def __init__(self, study=None, study_sample=None, laboratory=None, assay=None):  # noqa: E501
        """PredictiveModelDataBackground - a model defined in Swagger"""  # noqa: E501
        self._study = None
        self._study_sample = None
        self._laboratory = None
        self._assay = None
        self.discriminator = None
        self.study = study
        if study_sample is not None:
            self.study_sample = study_sample
        if laboratory is not None:
            self.laboratory = laboratory
        if assay is not None:
            self.assay = assay

    @property
    def study(self):
        """Gets the study of this PredictiveModelDataBackground.  # noqa: E501


        :return: The study of this PredictiveModelDataBackground.  # noqa: E501
        :rtype: Study
        """
        return self._study

    @study.setter
    def study(self, study):
        """Sets the study of this PredictiveModelDataBackground.


        :param study: The study of this PredictiveModelDataBackground.  # noqa: E501
        :type: Study
        """
        if study is None:
            raise ValueError("Invalid value for `study`, must not be `None`")  # noqa: E501

        self._study = study

    @property
    def study_sample(self):
        """Gets the study_sample of this PredictiveModelDataBackground.  # noqa: E501


        :return: The study_sample of this PredictiveModelDataBackground.  # noqa: E501
        :rtype: list[StudySample]
        """
        return self._study_sample

    @study_sample.setter
    def study_sample(self, study_sample):
        """Sets the study_sample of this PredictiveModelDataBackground.


        :param study_sample: The study_sample of this PredictiveModelDataBackground.  # noqa: E501
        :type: list[StudySample]
        """

        self._study_sample = study_sample

    @property
    def laboratory(self):
        """Gets the laboratory of this PredictiveModelDataBackground.  # noqa: E501


        :return: The laboratory of this PredictiveModelDataBackground.  # noqa: E501
        :rtype: list[Laboratory]
        """
        return self._laboratory

    @laboratory.setter
    def laboratory(self, laboratory):
        """Sets the laboratory of this PredictiveModelDataBackground.


        :param laboratory: The laboratory of this PredictiveModelDataBackground.  # noqa: E501
        :type: list[Laboratory]
        """

        self._laboratory = laboratory

    @property
    def assay(self):
        """Gets the assay of this PredictiveModelDataBackground.  # noqa: E501


        :return: The assay of this PredictiveModelDataBackground.  # noqa: E501
        :rtype: list[Assay]
        """
        return self._assay

    @assay.setter
    def assay(self, assay):
        """Sets the assay of this PredictiveModelDataBackground.


        :param assay: The assay of this PredictiveModelDataBackground.  # noqa: E501
        :type: list[Assay]
        """

        self._assay = assay

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
        if issubclass(PredictiveModelDataBackground, dict):
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
        if not isinstance(other, PredictiveModelDataBackground):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other