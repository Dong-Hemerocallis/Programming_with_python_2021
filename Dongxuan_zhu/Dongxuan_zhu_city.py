# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Dongxuan_Zhu
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Dongxuan Zhu
# Email: dongxuan.zhu@iaac.student.net
# Status: development
##################################################


city_name = 'Guangzhou'
city_area = 7343
city_population = 1530
household_population = 953
overall_urbanization_rate = 0.86
household_population_urbanization_rate = 0.80
flowing_population = city_population - household_population
urbanized_population = city_population * overall_urbanization_rate
urbanized_household_population = household_population * household_population_urbanization_rate
urbanized_flowing_population_rate = round (float( urbanized_population - urbanized_household_population ) / flowing_population, 3)
city_density = round (float (city_population/city_area ) * 10, 3)



print ('The population density of Guangzhou is {} thousand people per square km'.format (city_density) )
print ('The urbanized rate of its flowing population is {} '.format (urbanized_flowing_population_rate))

