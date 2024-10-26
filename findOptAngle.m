function [newY, corrVal, rhos, phaseList] = findOptAngle(location, Y, dim)
    phaseList = 0:12:360;
    % Finding correlation values for each angle
    rhos = zeros(2,numel(phaseList));
    for i = 1:2
        for phaseIdx = 1:numel(phaseList)
            rotAngle = (phaseList(phaseIdx)/180)*pi;
            rotMat = [cos(rotAngle),-sin(rotAngle);...
                sin(rotAngle),cos(rotAngle)];
            thisY = Y*rotMat;
            [rhos(i,phaseIdx), ~] = ...
                corr(location(:,i),...
                thisY(:,i),'type','spearman');
        end
    end
    [~, peakIdx] = max(rhos,[],2);
    % Do a mirror flip on Y
    if (abs(diff(phaseList(peakIdx))) > 90) && (abs(diff(phaseList(peakIdx))) < 270)
        rhos = zeros(2,numel(phaseList));
        Y(:,1) = -Y(:,1);
        for i = 1:2
            for phaseIdx = 1:numel(phaseList)
                rotAngle = (phaseList(phaseIdx)/180)*pi;
                rotMat = [cos(rotAngle),-sin(rotAngle);...
                    sin(rotAngle),cos(rotAngle)];
                thisY = Y*rotMat;
                [rhos(i,phaseIdx), ~] = ...
                    corr(location(:,i),...
                    thisY(:,i),'type','spearman');
            end
        end
        [~, peakIdx] = max(rhos,[],2);
    end
    
    % Rotate according to peak correlation value at the 
    if (dim == 1)
        [corrVal, phaseIdx] = max(rhos(1,:));
    elseif (dim == 2)
        [corrVal, phaseIdx] = max(rhos(2,:));
    else
        [corrVal, phaseIdx] = max(mean(rhos));
    end
    
    rotAngle = (phaseList(phaseIdx)/180)*pi;
    rotMat = [cos(rotAngle),-sin(rotAngle);...
                sin(rotAngle),cos(rotAngle)];
    newY = Y*rotMat;
    
end
