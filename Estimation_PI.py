# =============================================================================
# Nom : GNANASEELAN BENEDICT Jathurshan
#       TCHAKAH Koffi Kafui
# Master SEP
# 2020/2021
# =============================================================================

from random import *

def is_point_inside_unit_circle(p):
 x, y = random(), random()
 return 1 if x*x + y*y < 1 else 0

nin = is_point_inside_unit_circle()
#nin permet de determiner si le point selectionné est dans le cercle où pas, le résultat affiche 1 si oui 0 sinon

def pi_estimator_spark(n):
count.map(is_point_inside_unit_circle)
count = sc.parallelize(xrange(0, 20)).map(sample).reduce(lambda a, b: a + b)
print "Pi is roughly %f" % (4.0 * count / 20)
def pi_estimator_spark(n):
