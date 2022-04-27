% =========================================
%
% Subroutine forier.m
%
% =========================================
function [azero, a, b, xsin, xcos] = forier(n, m, time, x, t)
pi = 3.1416;
sumz = 0.0;
for i = 1:n
    sumz = sumz + x(i);
end
azero = 2.0*sumz/n;
for ii = 1:m
    sums = 0.0;
    sumc = 0.0;
    for i = 1:n
        theta = 2.0*pi*t(i)*ii/time;
        xcos(i) = x(i) * cos(theta);
        xsin(i) = x(i) * sin(theta);
        sums = sums + xsin(i);
        sumc = sumc + xcos(i);
    end
    a(ii) = 2.0 * sumc/n;
    b(ii) = 2.0 * sums/n;
end