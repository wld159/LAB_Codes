% ==============================
%
% Automatic Control Homework
% 12nd_Week
% No. 3 - c
%
% ==============================
clear;
clc;
% Define transfer function
s = tf('s');
% Subtitute L(s)
sysS = (s+5)/(s*(s+1)*(s^2+6*s+10));
% Plot Root Locus
rlocus(sysS)