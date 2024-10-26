% Collect all the Ca2+ footprints for CellReg
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
%             'E:\Data\Endoscope\MetaData\JZ231Os.mat',...
%             'E:\Data\Endoscope\MetaData\WG027T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG032T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG034T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG035T1.mat',...
%             'E:\Data\Endoscope\MetaData\WG036O1.mat',...
%             'E:\Data\Endoscope\MetaData\WG037O1.mat',...
            'D:\Data\Endoscope\MetaData\JZ231HI.mat',...
            };


tmpFolder = 'D:\Temp\npz_tmp';

for j = 1:numel(metaList)
    load(metaList{j});
    slashIdx = find(metaList{j}=='\',1,'last');
    groupName = metaList{j}(slashIdx+1:end-4);
    outFolder = [metaList{j}(1:end-4)];
    mkdir(outFolder);
    for i = 1:numel(sessionIDList)
        infileName = [dataFolder,'\',animalID,'\',sessionIDList{i},...
                    '\',resultFolderList{i},'\',resultFolderList{i},...
                    '_results.npz'];
        disp(infileName);
        delete([tmpFolder,'\*.*']);
        unzip(infileName, tmpFolder);
        A = readNPY([tmpFolder,'\A.npy']);
        allFiltersMat = reshape(A',size(A,2),240,376);
        outfileName = [groupName,'_footprint',num2str(i),'.mat'];
        save([outFolder,'\',outfileName], 'allFiltersMat');
    end
end




