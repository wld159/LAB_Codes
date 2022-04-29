% ==============================
%
% Automatic Control Homework
% 3rd_Week
% No. 1 - c
%
% ==============================
clear;
clc;
% Define coefficients of numerator and denominator
num = [0.05 0.1];
den = [1 0.6 11.2 1 2];
% Generate Transfer Function
sys = tf(num, den);
% Plot
% Set step input as 500N
step(500*sys)