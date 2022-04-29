% Advanced Engineering Mathematics
% 12.1 Basic Concepts of PDEs
% plotting 3-dimension
%%

% No.3
f1 = @(x, t) cos(4*t)*sin(2*x);
fsurf(f1, [0 pi 0 pi/2])
title('cos(4t)sin(2x) for x and t in [0, \pi] and [0, \pi/2]')
xlabel('x');
ylabel('t');
zlabel('u');
ax = gca;
ax.XTick = 0:pi/4:pi;
ax.XTickLabel = {'0', '\pi/4', '\pi/2', '3\pi/4', '\pi'};
ax.YTick = 0:pi/8:pi/2;
ax.YTickLabel = {'0', '\pi/8', '\pi/4', '3\pi/8', '\pi/2'};
ax.ZTick = -1:0.5:1;
ax.ZTickLabel = {'-1', '-0.5', '0', '0.5', '1'};
box on
%% 

% No.6
f2 = @(x, t) exp(-t)*sin(x);
fsurf(f2, [0 2*pi 0 1])
title('exp(-t)sin(x) for x and t in [0, 2\pi] and [0, 1]')
xlabel('x');
ylabel('t');
zlabel('u');
ax = gca;
ax.XTick = 0:pi:2*pi;
ax.XTickLabel = {'0', '\pi', '2\pi'};
ax.YTick = 0:0.5:1;
ax.YTickLabel = {'0', '0.5', '1'};
ax.ZTick = -1:1:1;
ax.ZTickLabel = {'-1', '0', '1'};
box on
%%

% No. 9
f3 = @(x, t) exp(-pi^2*t)*cos(25*x);
fsurf(f3, [0 pi/10 0 1/10])
title('exp(-\pi^2t)cos(25x) for x and t in [0, \pi] and [0, 1/10]')
xlabel('x');
ylabel('t');
zlabel('u');
ax = gca;
ax.XTick = 0:pi/20:pi/10;
ax.XTickLabel = {'0', '\pi/20', '\pi/10'};
ax.YTick = 0:1/20:1/10;
ax.YTickLabel = {'0', '1/20', '1/10'};
ax.ZTick = -1:1:1;
ax.ZTickLabel = {'-1', '0', '1'};
box on
%%

% No. 12_1
f4 = @(x, y) cos(y)*sinh(x);
fsurf(f4, [-1 1 0 2*pi])
title('cos(y)sinh(x) for x and y in [-1, 1] and [0, 2\pi]')
xlabel('x');
ylabel('y');
zlabel('u');
ax = gca;
ax.XTick = -1:1:1;
ax.XTickLabel = {'-1', '0', '1'};
ax.YTick = 0:pi:2*pi;
ax.YTickLabel = {'0', '\pi', '2\pi'};
ax.ZTick = -1:1:1;
ax.ZTickLabel = {'-1.2', '0', '1.2'};
box on
%%

% No. 12_2
f5 = @(x, y) sin(y)*cosh(x);
fsurf(f5, [-1 1 0 2*pi])
title('sin(y)cosh(x) for x and y in [-1, 1] and [0, 2\pi]')
xlabel('x');
ylabel('y');
zlabel('u');
ax = gca;
ax.XTick = -1:1:1;
ax.XTickLabel = {'-1', '0', '1'};
ax.YTick = 0:pi:2*pi;
ax.YTickLabel = {'0', '\pi', '2\pi'};
ax.ZTick = -1:1:1;
ax.ZTickLabel = {'-1.6', '0', '1.6'};