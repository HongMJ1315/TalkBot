def wlogs(line):
    logs=open('log.txt','a')
    logs.writelines(line)
    logs.close()