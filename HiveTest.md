#### run cloudera Docker container:
```
docker run --hostname=quickstart.cloudera --privileged=true -t -i -v ~/docker_share:/mnt --publish-all=true -p 8888 cloudera/quickstart /usr/bin/docker-quickstart
```

#### to find cloudera port:
```
docker inspect <container id>
```

#### run .hql script:
```
hive -f <filename>
```


#### script: [TableFromCsv.hql](https://github.com/v-asyunin/Sber_DE_test/blob/main/TableFromCsv.hql)


#### demo:
https://www.youtube.com/
