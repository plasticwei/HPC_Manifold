function [placeField, infoMetric, sparseMetric] = ...
    calcPlaceField(location, response, xLim, yLim, gridSizes)

    stepSize(1) = (xLim(2)-xLim(1))/gridSizes(1);
    stepSize(2) = (yLim(2)-yLim(1))/gridSizes(2);
    xGrid = xLim(1):stepSize(1):xLim(2);
    yGrid = yLim(1):stepSize(2):yLim(2);
    placeField = zeros(numel(xGrid)-1,numel(yGrid)-1);
    timeOccu = zeros(numel(xGrid)-1,numel(yGrid)-1);
    for i = 1:numel(response)
        idx1 = ceil((location(i,1)-xLim(1))/stepSize(1));
        idx2 = ceil((location(i,2)-yLim(1))/stepSize(2));
        idx1 = max(idx1,1);
        idx2 = max(idx2,1);
        placeField(idx1,idx2) = placeField(idx1,idx2) + response(i);
        timeOccu(idx1,idx2) = timeOccu(idx1,idx2) + 1;
    end
    placeField = placeField./timeOccu;
    
    validRFs = placeField(find(~isnan(placeField)));
    validTime = timeOccu(find(~isnan(placeField)));
    validOccu = validTime/sum(validTime);
    meanRate = sum(response)/sum(timeOccu(:));

    infoMetric = nansum(log2(validRFs/meanRate).*(validRFs/meanRate).*validOccu);
    sparseMetric = nansum(validRFs.*validOccu)^2/nansum(validOccu.*(validRFs.^2));
    
end
