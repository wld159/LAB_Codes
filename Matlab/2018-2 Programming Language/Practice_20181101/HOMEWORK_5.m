% HOMEWORK 5
% ID#: 20181490
% NAME: Kwon Gyeong Ho
% DATE: 11-01-2018
%
% Create an M-File and turn in the result.
%
% 1. When
%    a = [1, 3, 5], b = [4, 0, 8], c = [-2, 9, 1]
a = [1, 3, 5]
b = [4, 0, 8]
c = [-2, 9, 1]
ANS1 = dot(a, b)
ANS2 = dot(b, c)
ANS3 = norm(a)
ANS4 = norm(a+b)
ANS5 = norm(a+c)^2 + norm(a-c)^2 - 2*(norm(a)^2+norm(c)^2)
ANS6 = dot(a, (b - c))
ANS7 = 5*a-7*b+3*c
ANS8 = cross(a, b)
ANS9 = cross(b, a)
ANS10 = dot(b, cross(a, c))
%
% 2. By Defining a Function
ANS11 = f(1)
ANS12 = f(2)
ANS13 = f(10)
ANS14 = f(pi)

function [x] = f(x)
y = exp(-x)*cos(x) + x^2 + x + 1 - log10(x)
end
%q