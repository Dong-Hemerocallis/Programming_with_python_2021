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

my_city_name = 'Guangzhou'
my_city_population = 15300000
my_previous_city_name = 'Shenzhen'
my_previoius_city_population = 12530000

if my_city_population < 10000000:
    print ('My city is not a megacity')
elif  1000000 < my_city_population < 15000000:
    print ('My city is a medium sized megacity')
else: print ('My city is a large megacity')

if my_city_population > my_previoius_city_population:
    print('The Population of my city is larger than that of Shenzhen')

print ('End of script')

