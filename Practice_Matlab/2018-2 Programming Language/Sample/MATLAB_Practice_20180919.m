%HOMEWORK 1

%1. CALCULATE
23.234+143.017+7.63-109.754
(37.254*97.115-7.58)/1.27
3.692*10^3+8.573*10^4-6.342*10^2
8.574*10^-2/7.549*10^3

%2. SOLVE THE QUADRATIC EQUATIONS FOR X.
roots([1, 7.539, 9.354])
roots([5.278, 8.378, -7.624])

%3. SOLVE THE SIMULTANEOUS EQUATIONS
inv([2.5, 7.3; -6.1, 3.1])*([5.4; -11.5])
inv([1, 1, 1; 1, -2, 5; 1, 3, -7])*([3; 7; -11])

%4. FOR THE ARITHMETIC SEQUENCE, g(x) = 0.8+(x-1)(0.25) CALCULATE g(2),
%g(3), g(4), g(5), g(6), SUM FROM 1 TO 6
g=@(x) 0.8+(x-1)*0.25
x = ([2, 3, 4, 5, 6])
y = g([2, 3, 4, 5, 6])
syms k x; symsum(0.8+(k-1)*0.25, k, 1, 6)

%5. FOR THE FUNCTION, f(x) = exp(x)+log(x)+sin(2*x), CALCULATE f(1),
%f(1.5), f(2), f(2.5)
f=@(x) exp(x)+log(x)+sin(2*x)
x = ([1, 1.5, 2, 2.5])
y = f([1, 1.5, 2, 2.5])
plot(x, y)