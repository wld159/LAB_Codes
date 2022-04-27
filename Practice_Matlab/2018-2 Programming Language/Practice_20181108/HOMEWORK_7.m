% HOMEWORK 7
% ID#: 20181490
% NAME: Kwon Gyeong Ho
% DATE: 11-08-2018
%
% 1. Arrays: Matrices
a = [1, 2, 3; -2, 7, -5]
b = [4, 1, 2; 3, -5, 7]
c = [1, 2; 3, 4; 5, 6]
% Two Important Matrix Properties:
%
% (i) Scalar Multiplication
3 * a
2 * c
% (ii) Vector Additions
a + b
% a + c
%
% When any array satisfies these properties, then it is called "MATRIX".
% Otherwise, they are just called "MATRICES".
%
% Size of a Matrix
size(a)
size(b)
size(c)
% Length of a Matrix
length(a)
length(b)
length(c)
% Matrix Multiplication
% a * b
% a * c
% Transpose of a Matrix
a'
b'
c'
% Size of a transposed Matrix
size(a')
size(b')
size(c')
% Length of a transposed Matrix
length(a')
length(b')
length(c')
% 
% Convenient Operations Provided by Matlab
%
% Additoin of a Vector by a Scalar
%
a
a + 3
a + [3, 3, 3; 3, 3, 3]
c - 5
%
% Element-by-Element Operations:
a
b
% a * b
a .* b
% a^2
a.^2
c.^3
a./b
%
% Library Functions
%
exp(a)
exp(c)
sin(b)
tan(c)
log(a)
log2(a)
log10(a)
log(b)
exp(c)
%
% Row Vectors and Column Vectors
%
a(1, 1: 3)
c(1:3, 2)
%
% Transpose of a Vector
a'
b'
c'
%