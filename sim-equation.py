import math
import string

print('\n\tENTER COEFFICIENTS of X,Y AND THE REMAINDER VALUES FOR EQN-1: ')

#Equation 1
eqnOneX = int(input('\n\tCO-EFFICIENT OF X: '))

eqnOneY = int(input('\n\tCO-EFFICIENT OF Y: '))

eqnOneZ = int(input('\n\tREMAINDER VALUE: '))

print('\n\t**************************************************\n\n')
#Equation 2
print('\n\tENTER COEFFICIENTS of X,Y AND THE REMAINDER VALUES FOR EQN-2: ')
eqnTwoX = int(input('\n\tCO-EFFICIENT OF X: '))

eqnTwoY = int(input('\n\tCO-EFFICIENT OF Y: '))

eqnTwoZ = int(input('\n\tREMAINDER VALUE: '))

print('\n\t**************************************************\n\n')

print('\n\tHOW THE SIMULTANEOUS EQUATION LOOKS LIKE BASED ON YOUR INPUTS\n')
print('\n\t'+ str(eqnOneX)+'x + '+str(eqnOneY)+'y = '+ str(eqnOneZ)+'\n')
print('\n\t'+ str(eqnTwoX)+'x + '+str(eqnTwoY)+'y = '+ str(eqnTwoZ)+'\n')

Y = ((eqnTwoX*eqnOneZ)-(eqnOneX*eqnTwoZ))/((eqnTwoX*eqnOneY)-(eqnOneX*eqnTwoY)); #Formula for finding Y
X = (eqnOneZ - (eqnOneY*Y))/eqnOneX; #Formula for X after finding Y

print('\n\tX: '+ str(X) +'\n')
print('\n\tY: '+ str(Y) +'\n')