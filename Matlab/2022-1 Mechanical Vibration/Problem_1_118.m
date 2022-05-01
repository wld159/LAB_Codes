% ======================================================
%
% Program1.m
% Program for calling the subroutine FORIER
%
% ======================================================
% Run "Program.m" in MATLAB Command Window. Program1.m and forier.m should
% be in the same file folder, and set the path to this folder
% Following 6 lines contain problem-dependent data
n = 16;
m = 3;
time = 0.32;
x = [9 13 17 29 43 59 63 57 49 35 35 41 47 41 13 7];
t = 0.02:0.02:0.32;
% end of problem-dependent data
% Follwing line calls subroutine forier.m
[azero, a, b, xsin, xcos] = forier(n, m, time, x, t);
% Following outputs data
fprintf("Fourier series expansion of the function x(t) \n\n");
fprintf("Data: \n\n")
fprintf("Number of data points in one cycle = %3.0f \n", n);
fprintf(" \n");
fprintf("Number of Fourier Coefficients required = %3.0f \n", m);
fprintf(" \n");
fprintf("Time period = %8.6e \n\n", time);
fprintf("Station i        ")
fprintf("Time at station i: t(i)         ")
fprintf("x(i) at t(i)")
for i = 1:n
    fprintf("\n %8d%25.6e%27.6e ", i, t(i), x(i));
end
fprintf(" \n\n");
fprintf("Results of Fourier analysis: \n\n");
fprintf('azeros=%8.6e \n\n', azero);
fprintf("values of i     a(i)                b(i)\n");
for i = 1:m
    fprintf("%10.0g %8.6e%20.6e \n", i, a(i), b(i));
end