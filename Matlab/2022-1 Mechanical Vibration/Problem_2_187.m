% ==============================
%
% Mechanical Vibration Homework
% Chapter 2. Free Vibration of Single Degree of Freedom Systems
% No. 187
%
% ==============================
clear;
clc;
% This Program will use dfunc1.m
tspan = 0: 0.05: 1;
x0 = [0.4; 0.0];
[t, x] = ode23('dfunc1', tspan, x0);
plot(t, x(:, 1));
xlabel('t');
ylabel('x(t)');