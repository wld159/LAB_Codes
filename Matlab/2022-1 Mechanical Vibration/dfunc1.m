function f = dfunc1(~, x)
u = 0.5;
k = 100;
m = 5;
f = zeros(2, 1);
f(1) = x(2);
f(2) = -u * 9.81 * sign(x(2)) - k * x(1) / m;