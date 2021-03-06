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

class PopulationGroup(object):
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
        'name': 'str',
        'target_population': 'str',
        'population_span': 'list[str]',
        'population_description': 'list[str]',
        'population_age': 'list[str]',
        'population_gender': 'str',
        'bmi': 'list[str]',
        'special_diet_groups': 'list[str]',
        'pattern_consumption': 'list[str]',
        'region': 'list[str]',
        'country': 'list[str]',
        'population_risk_factor': 'list[str]',
        'season': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'target_population': 'targetPopulation',
        'population_span': 'populationSpan',
        'population_description': 'populationDescription',
        'population_age': 'populationAge',
        'population_gender': 'populationGender',
        'bmi': 'bmi',
        'special_diet_groups': 'specialDietGroups',
        'pattern_consumption': 'patternConsumption',
        'region': 'region',
        'country': 'country',
        'population_risk_factor': 'populationRiskFactor',
        'season': 'season'
    }

    def __init__(self, name=None, target_population=None, population_span=None, population_description=None, population_age=None, population_gender=None, bmi=None, special_diet_groups=None, pattern_consumption=None, region=None, country=None, population_risk_factor=None, season=None):  # noqa: E501
        """PopulationGroup - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._target_population = None
        self._population_span = None
        self._population_description = None
        self._population_age = None
        self._population_gender = None
        self._bmi = None
        self._special_diet_groups = None
        self._pattern_consumption = None
        self._region = None
        self._country = None
        self._population_risk_factor = None
        self._season = None
        self.discriminator = None
        self.name = name
        if target_population is not None:
            self.target_population = target_population
        if population_span is not None:
            self.population_span = population_span
        if population_description is not None:
            self.population_description = population_description
        if population_age is not None:
            self.population_age = population_age
        if population_gender is not None:
            self.population_gender = population_gender
        if bmi is not None:
            self.bmi = bmi
        if special_diet_groups is not None:
            self.special_diet_groups = special_diet_groups
        if pattern_consumption is not None:
            self.pattern_consumption = pattern_consumption
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country
        if population_risk_factor is not None:
            self.population_risk_factor = population_risk_factor
        if season is not None:
            self.season = season

    @property
    def name(self):
        """Gets the name of this PopulationGroup.  # noqa: E501

        Name of the population for which the model or data applies  # noqa: E501

        :return: The name of this PopulationGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PopulationGroup.

        Name of the population for which the model or data applies  # noqa: E501

        :param name: The name of this PopulationGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target_population(self):
        """Gets the target_population of this PopulationGroup.  # noqa: E501

        Population of individual that we are interested in describing and making statistical inferences about  # noqa: E501

        :return: The target_population of this PopulationGroup.  # noqa: E501
        :rtype: str
        """
        return self._target_population

    @target_population.setter
    def target_population(self, target_population):
        """Sets the target_population of this PopulationGroup.

        Population of individual that we are interested in describing and making statistical inferences about  # noqa: E501

        :param target_population: The target_population of this PopulationGroup.  # noqa: E501
        :type: str
        """

        self._target_population = target_population

    @property
    def population_span(self):
        """Gets the population_span of this PopulationGroup.  # noqa: E501


        :return: The population_span of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._population_span

    @population_span.setter
    def population_span(self, population_span):
        """Sets the population_span of this PopulationGroup.


        :param population_span: The population_span of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._population_span = population_span

    @property
    def population_description(self):
        """Gets the population_description of this PopulationGroup.  # noqa: E501


        :return: The population_description of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._population_description

    @population_description.setter
    def population_description(self, population_description):
        """Sets the population_description of this PopulationGroup.


        :param population_description: The population_description of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._population_description = population_description

    @property
    def population_age(self):
        """Gets the population_age of this PopulationGroup.  # noqa: E501


        :return: The population_age of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._population_age

    @population_age.setter
    def population_age(self, population_age):
        """Sets the population_age of this PopulationGroup.


        :param population_age: The population_age of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._population_age = population_age

    @property
    def population_gender(self):
        """Gets the population_gender of this PopulationGroup.  # noqa: E501

        Description of the percentage of gender  # noqa: E501

        :return: The population_gender of this PopulationGroup.  # noqa: E501
        :rtype: str
        """
        return self._population_gender

    @population_gender.setter
    def population_gender(self, population_gender):
        """Sets the population_gender of this PopulationGroup.

        Description of the percentage of gender  # noqa: E501

        :param population_gender: The population_gender of this PopulationGroup.  # noqa: E501
        :type: str
        """

        self._population_gender = population_gender

    @property
    def bmi(self):
        """Gets the bmi of this PopulationGroup.  # noqa: E501


        :return: The bmi of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._bmi

    @bmi.setter
    def bmi(self, bmi):
        """Sets the bmi of this PopulationGroup.


        :param bmi: The bmi of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._bmi = bmi

    @property
    def special_diet_groups(self):
        """Gets the special_diet_groups of this PopulationGroup.  # noqa: E501


        :return: The special_diet_groups of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._special_diet_groups

    @special_diet_groups.setter
    def special_diet_groups(self, special_diet_groups):
        """Sets the special_diet_groups of this PopulationGroup.


        :param special_diet_groups: The special_diet_groups of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._special_diet_groups = special_diet_groups

    @property
    def pattern_consumption(self):
        """Gets the pattern_consumption of this PopulationGroup.  # noqa: E501


        :return: The pattern_consumption of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._pattern_consumption

    @pattern_consumption.setter
    def pattern_consumption(self, pattern_consumption):
        """Sets the pattern_consumption of this PopulationGroup.


        :param pattern_consumption: The pattern_consumption of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._pattern_consumption = pattern_consumption

    @property
    def region(self):
        """Gets the region of this PopulationGroup.  # noqa: E501


        :return: The region of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PopulationGroup.


        :param region: The region of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._region = region

    @property
    def country(self):
        """Gets the country of this PopulationGroup.  # noqa: E501


        :return: The country of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PopulationGroup.


        :param country: The country of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._country = country

    @property
    def population_risk_factor(self):
        """Gets the population_risk_factor of this PopulationGroup.  # noqa: E501


        :return: The population_risk_factor of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._population_risk_factor

    @population_risk_factor.setter
    def population_risk_factor(self, population_risk_factor):
        """Sets the population_risk_factor of this PopulationGroup.


        :param population_risk_factor: The population_risk_factor of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._population_risk_factor = population_risk_factor

    @property
    def season(self):
        """Gets the season of this PopulationGroup.  # noqa: E501


        :return: The season of this PopulationGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PopulationGroup.


        :param season: The season of this PopulationGroup.  # noqa: E501
        :type: list[str]
        """

        self._season = season

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
        if issubclass(PopulationGroup, dict):
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
        if not isinstance(other, PopulationGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
