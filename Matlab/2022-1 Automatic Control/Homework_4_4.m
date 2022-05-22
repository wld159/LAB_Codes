% ==============================
%
% Automatic Control Homework
% 12nd_Week
% No. 4 - c
%
% ==============================
clear;
clc;
% Define transfer function
s = tf('s');
% Subtitute L(s)
sysS = 1/(s*(s+3)*(s^2+3*s+7));
% Plot Root Locus
rlocus(sysS)