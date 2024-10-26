clear;

metaList = {...
%             'E:\Data\Endoscope\MetaData\JZ207Sq1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ207I1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ207Tee1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ207Circle1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ207Circle2.mat',...
%             'E:\Data\Endoscope\MetaData\JZ209Circle1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ218Circle1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ219Circle1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ219Tee1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ222Tee1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ224Circle1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ226Tee1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ229Tee1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ231H1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ231H2.mat',...
%             'E:\Data\Endoscope\MetaData\JZ231I1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ231O1.mat',...
%             'E:\Data\Endoscope\MetaData\JZ231O2.mat',...
%             'E:\Data\Endoscope\MetaData\JZ231O3.mat',...
%             'E:\Data\Endoscope\MetaData\WG027T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG032T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG034T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG035T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG036O1.mat',...
%             'E:\Data\Endoscope\MetaData\WG037O1.mat',...
            'E:\Data\Endoscope\MetaData\WG037O2.mat',...
            };
        
minVel = 10;
maxVel = 1000;
anlysID = 'Anlys9';

for j = 1:numel(metaList)
    load(metaList{j});
    for i = 1:numel(sessionIDList)
        infileName = [dataFolder,'\',animalID,'\',sessionIDList{i},...
                    '\',resultFolderList{i},'\',resultNameList{i},'.mat'];
        disp(infileName);
        outfileName = [dataFolder,'\',animalID,'\',sessionIDList{i},...
                    '\',resultFolderList{i},'\',resultNameList{i},'_',...
                    anlysID,'.mat'];
        processIso_2D(infileName, outfileName, sessionBlkAlloList{i},...
                    sessionBlkNumList{i},mapKeyList{i}, minVel, maxVel);
    end
end
