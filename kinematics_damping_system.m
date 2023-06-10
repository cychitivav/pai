clear, clc, close 'all'

% parameters
width = 165;
% parameters damper mechanism
L1 = 20;          
L2 = 80;
L3 = 80;
L4 = 20;


P_damper = [width/2; 10];
k_damper = 2;  % N/m

q1 = -45*pi/180; % angle parameter first articulation 
q5 = -45*pi/180; % angle parameter last articulation

points = kinematic_chain(q1,q5,width,L1,L2,L3,L4) % position damping mechanism

% parameters wheel mechanism
LL= 100;
LR = 100;
alpha_i = pi/2;

alpha_d = pi/2;
hL = 80;
hR = 80;
% position wheel mechanism
[q1,q5,points_wheels] = wheel_mechanism(hL,hR,LL,LR,alpha_i,alpha_d,width); 

q1*180/pi
q5*180/pi

points = kinematic_chain(q1,q5,width,L1,L2,L3,L4) 

%%
n=10;       % number of iterations

vhL= linspace(40,80 ,n);    % vector height left wheel

vhR= linspace(40, 80,n);    % vector height right wheel


mesh_F_damper  = zeros(n,n);
mesh_F_L  = zeros(n,n);
mesh_F_R = zeros(n,n);


for i = 1:n

    for j = 1:n
     
        hL = vhL(i);
        hR = vhR(j);
        
        [q1,q5,points_wheels] = wheel_mechanism(hL,hR,LL,LR,alpha_i,alpha_d,width);

        [points,P3,P4] = kinematic_chain(q1,q5,width,L1,L2,L3,L4) ;
        
        x = points(1,:);
        y = points(2,:);
        P2 = points(:,3);
    
    
        [theta_damper,L_damper] = cart2pol(P_damper(1)-P2(1),P_damper(2)-P2(2));
        F_damper = k_damper*(L_damper-25);
        
        % kinetics damper system
        F_reactions = linsolve([cos(q1),cos(-q5); sin(q1),sin(-q5)],F_damper*[cos(theta_damper); sin(theta_damper)]);

        F_L =F_reactions(1) *[cos(q1);sin(q1)];     % Force direction entering the system
        F_R =F_reactions(2) *[cos(-q5);sin(-q5)];   % Force direction exiting the system
        
        F_L+F_R+F_damper*[cos(theta_damper);sin(theta_damper)];

        mesh_F_damper (i,j) = F_damper;
        mesh_F_L (i,j) = F_reactions(1);
        mesh_F_R (i,j) = F_reactions(2);
    
        plot(x,y,'o-');
        hold on
        plot([P4(1),P3(1)],[P4(2),P3(2)],'o-');
        plot([0,P4(1)],[0,P4(2)],'*')
        plot([P2(1),P_damper(1)],[P2(2),P_damper(2)],'-+')
        plot(points_wheels(1,:),points_wheels(2,:)) 
        axis equal
        grid on
        xlim([-100,300])
        ylim([-150,100])
    
        pause (0.01)
        hold off
    end

end
%%

[Q1,Q5] = meshgrid(vhL,vhR);
figure()
surf(Q1,Q5,mesh_F_damper)
hold on 
surf(Q1,Q5,-mesh_F_L,'FaceAlpha',0.8)
surf(Q1,Q5,mesh_F_R,'FaceAlpha',0.1)

xlabel("height left [mm]")
ylabel("height right [mm]")
title   ("Force [N]")

function [q1,q5,points_wheels] = wheel_mechanism(hL,hR,LL,LR,alpha_i,alpha_d,width)
qin1 = asin(hL/LL);
qin5 = asin(hR/LR);

q1 = qin1 + alpha_i -pi

q5 = qin5 + alpha_d -pi
Pi = LL*[cos(qin1-pi);sin(qin1-pi)];
Pd = LL*[cos(-qin5);sin(-qin5)];
P0 = [0;0];
P4 = [width;0]
points_wheels = [Pi,P0,P4,P4+Pd];
end

function [q_a, q_b] =  inverse_kinematics(Lx,Ly,La,Lb)
    L = norm([Lx,Ly]);
    c_b = (L^2-La^2-Lb^2)/(2*La*Lb);
    s_b = sqrt(1-c_b^2);       % signo: positivo codo arriba, negativo codo abajo
    q_b = atan2(s_b,c_b);
    disp("q_b " + string(q_b*180/pi))
    
    alpha = atan2(Ly,Lx);
    gamma = atan2(Lb*s_b,La+Lb*c_b);
    disp("alpha " + string(alpha*180/pi))
    disp("gamma " + string(gamma*180/pi))

    q_a = -gamma + alpha;

end


function [points,P3,P4] = kinematic_chain(q1,q5,width,L1,L2,L3,L4) 
    
    P1 = L1*[cos(q1);sin(q1)];
    
    P4 = [width;0];
    
    P3 = P4 - L4*[cos(-q5);sin(-q5)];
    Lx = P3(1) - P1(1);
    Ly = P3(2) - P1(2);
    
    [qa, q3] =  inverse_kinematics(Lx,Ly,L2,L3);
    q2 = qa - q1;
    q4 = -(q1 + q2 + q3 +q5);
    
    
    P2 = P1 + L2*[cos(q1+q2); sin(q1+q2)];
    P3_calc = P2 + L3*[cos(q1+q2+q3); sin(q1+q2+q3)];
    
    P4_calc = P3_calc + L4*[cos(q1+q2+q3+q4); sin(q1+q2+q3+q4)];
    P0 = [0;0];

    points =[P0,P1,P2,P3_calc,P4_calc];
    %vecnorm(diff(points,1,2))          % check length
end



