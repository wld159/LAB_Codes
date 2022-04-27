% HOMEWORK 6
% ID#: 20181490
% NAME: Kwon Gyeong Ho
% DATE: 11-07-2018
%
% 1. For
V1 = [1. -3, 5]
V2 = [5, 2, 9]
V3 = [7, -5, 3]
% Compute
ANS1 = dot(V1, V2)
ANS2 = dot(V1, cross(V2, V3))
ANS3 = norm(V1+V2)
ANS4 = sin(V1), cos(V2), tan(V3)
ANS5 = exp(V1), log(V3), log10(V2), log2(V1)
%
% 2. For
A = [1, -2, 3; -4, 5, 6; 7, 8, -9]
B = [4, 9, -3; 8, -2, 6; -1, 7, 5]
C = [-1, 4; 2, 5; 3, 6]
% Compute
% ANS6 = A + B, B + C
% ANS7 = A * B, A * C, C * A, C * B
ANS8 = sum(A,'all')
ANS9 = sum(abs(B),'all')
ANS10 = sum(A(2, :))
ANS11 = sum(B(:, 3))