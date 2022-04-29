% Advanced Engineering Mathematics
% 12.3 Solution by Separating Variables. Use of Fourier Series
% plotting 3-dimension
%%

% No.6
f1 = @(x, t) 0.01*(cos(pi*t)*sin(pi*x)-1/2*cos(2*pi*t)*sin(2*pi*x));
fsurf(f1, [0 2 0 2])
xlabel('x');
ylabel('t');
zlabel('u');
ax = gca;
ax.XTick = 0:1:2;
ax.XTickLabel = {'0', '1', '2'};
ax.YTick = 0:1:2;
ax.YTickLabel = {'0', '1', '2'};
ax.ZTick = -1/50:1/50:1/50;
ax.ZTickLabel = {'-1/50', '0', '1/50'};
box on
%% 

% No.9
f2 = @(x, t) (4/(5*pi^2))*(cos(pi*t)*sin(pi*x)-1/9*cos(3*pi*t)*sin(3*pi*x)+1/25*cos(5*pi*t)*sin(5*pi*x));
fsurf(f2, [0 2 0 2])
xlabel('x');
ylabel('t');
zlabel('u');
ax = gca;
ax.XTick = 0:1:2;
ax.XTickLabel = {'0', '1', '2'};
ax.YTick = 0:1:2;
ax.YTickLabel = {'0', '1', '2'};
ax.ZTick = -0.1:0.1:0.1;
ax.ZTickLabel = {'-0.1', '0', '0.1'};
box on
%%

% No. 12
f3 = @(x, t) (2*sqrt(2)/pi^2)*(cos(pi*t)*sin(pi*x)+1/9*cos(3*pi*t)*sin(3*pi*x)-1/25*cos(5*pi*t)*sin(5*pi*x));
fsurf(f3, [0 2 0 2])
xlabel('x');
ylabel('t');
zlabel('u');
ax = gca;
ax.XTick = 0:1:2;
ax.XTickLabel = {'0', '1', '2'};
ax.YTick = 0:1:2;
ax.YTickLabel = {'0', '1', '2'};
ax.ZTick = -0.3:0.3:0.3;
ax.ZTickLabel = {'-0.3', '0', '0.3'};
box on