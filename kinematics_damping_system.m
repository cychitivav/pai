clear, clc, close 'all'

% parameters
width = 165;

L1 = 20;          
L2 = 80;
L3 = 80;
L4 = 20;

n=10;

P_damper = [width/2; 10];
k_damper = 2;  % N/m


q1 = -45*pi/180; % angle parameter first articulation 
q5 = -45*pi/180; % angle parameter last articulation

points = kinematic_chain(q1,q5,width,L1,L2,L3,L4) 

vq1= linspace(-30, -70,n);

vq5= linspace(-30, -70,n);

datalog = zeros(n,n);

for i = 1:n

    for j = 1:n
     
        q1 = vq1(i)*pi/180;
        q5 = vq5(j)*pi/180;
    
        [points,P3,P4] = kinematic_chain(q1,q5,width,L1,L2,L3,L4) ;
        
        x = points(1,:);
        y = points(2,:);
        P2 = points(:,3);
    
    
        L_damper = norm(P2-P_damper);
        F_damper = k_damper*L_damper;
    
        datalog (i,j) = F_damper;
    
        plot(x,y,'o-');
        hold on
        plot([P4(1),P3(1)],[P4(2),P3(2)],'o-');
        plot([0,P4(1)],[0,P4(2)],'*')
        plot([P2(1),P_damper(1)],[P2(2),P_damper(2)],'-+')
         
        axis equal
        grid on
    
        pause (0.01)
        hold off
    end

end
%%

[Q1,Q5] = meshgrid(vq1,vq5);

surf(Q1,Q5,datalog)

xlabel("Angle Q1 [deg]")
ylabel("Angle Q5 [deg]")
title   ("Force [N]")

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


