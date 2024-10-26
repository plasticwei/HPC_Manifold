function processIso_2D(infileName, outfileName, blockAllo, blockNum,...
                        mapKey, minVel, maxVel)

    load(infileName);

    if ~iscell(rangeList)
        if (size(rangeList,1) == 1)
            rangeList = {rangeList};
        else
            tempList = [];
            for i = 1:size(rangeList,1)
                tempList{i} = rangeList(i,:);
            end
            rangeList = tempList;
        end
    end

    blockSizeOrig = cellfun(@numel, rangeList);
    winSize = []; 
    for i = 1:numel(blockAllo)
        winSize(i) = round(sum(blockSizeOrig(blockAllo{i}))/timeScaleDown);
    end
    winDur = [];
    winDur{1} = [1:winSize(1)];
    for i = 2:numel(blockAllo)
        winDur{i} = [sum(winSize(1:i-1))+1:sum(winSize(1:i))];
    end

    all_Y = all_Y(:,winDur{blockNum},:);
    location = location(winDur{blockNum},:);
    velocity = velocity(winDur{blockNum});

    new_location = fixLocation(location, mapKey);

    locColor = ones(size(new_location,1),3);
    locColor(:,3) = 0.85;
    maxRadius = max(sqrt(new_location(:,2).^2+new_location(:,1).^2))+1;
    locColor(:,2) = abs(complex(new_location(:,2),...
                        new_location(:,1)))/maxRadius;
    locColor(:,1) = mod(angle(complex(new_location(:,2),...
        new_location(:,1))) - 1.3, 2*pi)/(2*pi);


    newY = zeros(size(all_Y));
    corrVal = [];
    rhos = [];
    phaseList = [];
    for i = 1:size(all_Y)
        [newY(i,:,:), corrVal(i), rhos(i,:,:), phaseList(i,:)] = ...
            findOptAngle(new_location, ...
            squeeze(all_Y(i,:,:)), 0);
    end

    errorCurve = (1-all_Error(2:end)./all_Error(1:end-1));
    bestIsoIdx = find(diff(errorCurve > 0.1)==-1,1,'last') + 2;
    bestIsoIdx = min(bestIsoIdx,size(all_Y,1));
    
    gridSizesPlace = [40, 40];
    gridSizesMental = [40, 40];
%     gridSizesPlace = [20, 20];
%     gridSizesMental = [20, 20];

    placeFields = [];
    placeInfo = [];
    placeSparse = [];
    mentalFields = [];
    mentalInfo = [];
    mentalSparse = [];
    PFIdx = find((velocity >= minVel).*(velocity <= maxVel));
    neuroData = X_train;

    for i = 1:size(neuroData,2)
        xLimPlace = [min(new_location(:,1)), max(new_location(:,1))];
        yLimPlace = [min(new_location(:,2)), max(new_location(:,2))];
        [placeFields(i,:,:), placeInfo(i), placeSparse(i)] = ...
                                    calcPlaceField(new_location(PFIdx,:), ...
                                    neuroData(PFIdx,i) - min(neuroData(PFIdx,i)),...
                                    xLimPlace, yLimPlace, gridSizesPlace);
        for j = 1:size(newY,1)
            xLimMental = [min(newY(j,:,1)), max(newY(j,:,1))];
            yLimMental = [min(newY(j,:,2)), max(newY(j,:,2))];
            [mentalFields(i,j,:,:), mentalInfo(i,j), mentalSparse(i,j)] = ...
                        calcPlaceField(squeeze(newY(j,PFIdx,:)), ...
                        neuroData(PFIdx,i) - min(neuroData(PFIdx,i)),...
                                        xLimMental, yLimMental, gridSizesMental);
        end
    end
    
    thisvelocity = velocity;
    save(outfileName,'new_location','locColor','newY','corrVal',...
            'rhos','phaseList','errorCurve','bestIsoIdx','placeFields',...
            'placeInfo', 'placeSparse', 'mentalFields',...
            'mentalInfo', 'mentalSparse','thisvelocity');
    
end
