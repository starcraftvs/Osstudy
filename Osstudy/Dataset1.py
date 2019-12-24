import os
#用os.path打印出所有目标路径下文件，子文件夹
def get_dataset(datapath,filenamepath):
    data_path=datapath
    filename_path=os.path.join(os.path.dirname(data_path),filenamepath)
    #
    dirs=os.listdir(data_path)
    i=0
    with open(filename_path,'w') as f:
        for dir in dirs:
            datalabel_path=(os.path.join(data_path,dir))
            for roots1,dirs1,files1 in os.walk(datalabel_path):
                for file1 in files1:
                    f.write(os.path.join(datalabel_path,file1)+' '+str(i)+'\n')
                i=i+1
    return filename_path
