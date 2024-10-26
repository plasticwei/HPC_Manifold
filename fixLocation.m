function new_location = fixLocation(location, mapID)
    switch mapID
        case 'tee1'
            rotAngle = (-3/180)*pi;
            offsetDim1 = -325;
            offsetDim2 = -263;
        case 'tee2'
            rotAngle = (0/180)*pi;
            offsetDim1 = -385;
            offsetDim2 = -240;
        case 'tee3'
            rotAngle = (-179/180)*pi;
            offsetDim1 = 330;
            offsetDim2 = 220;
        case 'circle1'
            rotAngle = (-3/180)*pi;
            offsetDim1 = -300;
            offsetDim2 = -235;
        case 'circle2'
            rotAngle = (1/180)*pi;
            offsetDim1 = -250;
            offsetDim2 = -225;
        case 'linear1'
            rotAngle = (-3/180)*pi;
            offsetDim1 = -290;
            offsetDim2 = -265;
        case 'sq1'
            rotAngle = (-3/180)*pi;
            offsetDim1 = -300;
            offsetDim2 = -265;
        case 'h1'
            rotAngle = (0/180)*pi;
            offsetDim1 = -325;
            offsetDim2 = -230;
        case 'i1'
            rotAngle = (-45/180)*pi;
            offsetDim1 = -50;
            offsetDim2 = -390;
        case 't1'
            rotAngle = (181/180)*pi;
            offsetDim1 = 330;
            offsetDim2 = 220;
        otherwise
            disp('This map not defined');
            new_location = [];
            return;
    end
    
    rotMat = [cos(rotAngle),-sin(rotAngle);sin(rotAngle),cos(rotAngle)];
    new_location = location*rotMat;
    new_location(:,1) = new_location(:,1) + offsetDim1;
    new_location(:,2) = new_location(:,2) + offsetDim2;
end
