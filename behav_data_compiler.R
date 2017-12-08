#####G x G####
#step 1, combine behav data
#step 1.1, import studied cops

setwd("F:/Benesh/Research/G by G/GxGserver")
cops<-read.csv(file="cops_to_measure_test.csv",header=TRUE,sep = ";")
names(cops)


####day 5####
setwd("F:/Benesh/Research/G by G/GxGserver/output_d5")
copsx<-subset(cops, day==5)

filex<-as.character(copsx$file.name[1])
file.i<-paste(filex,"txt",sep=".")
d<-read.delim(file=file.i,header=TRUE)
dim(d)==c(62,8) #check dim

#index them by file name
id<-rep(filex,dim(d)[1])
dt5<-cbind(id,d)

#combine them in a loop
for(i in seq_along(copsx$file.name)){
  filex<-as.character(copsx$file.name[i])
  file.i<-paste(filex,"txt",sep=".")
  d<-read.delim(file=file.i,header=TRUE)
  dim(d)==c(62,8) #check dim
  
  #index them by file name
  id<-rep(filex,dim(d)[1])
  d2<-cbind(id,d)
  
  dt5<-rbind(dt5,d2) #combine them all
  
}

dt5<-dt5[63:dim(dt5)[1],]
which(table(dt5$id)!=62) #several have incorrect length (<62)
#re-do video analysis?








####day 7####
setwd("F:/Benesh/Research/G by G/GxGserver/output_d7")
copsx<-subset(cops, day==7)

filex<-as.character(copsx$file.name[1])
file.i<-paste(filex,"txt",sep=".")
d<-read.delim(file=file.i,header=TRUE)
dim(d)==c(62,8) #check dim

#index them by file name
id<-rep(filex,dim(d)[1])
dt7<-cbind(id,d)

#combine them in a loop
for(i in seq_along(copsx$file.name)){
  filex<-as.character(copsx$file.name[i])
  file.i<-paste(filex,"txt",sep=".")
  d<-read.delim(file=file.i,header=TRUE)
  dim(d)==c(62,8) #check dim
  
  #index them by file name
  id<-rep(filex,dim(d)[1])
  d2<-cbind(id,d)
  
  dt7<-rbind(dt7,d2) #combine them all
  
}

dt7<-dt7[63:dim(dt7)[1],]
which(table(dt7$id)!=62) #several have incorrect length (<62)
#re-do video analysis?












####day 9####
setwd("F:/Benesh/Research/G by G/GxGserver/output_d9")
copsx<-subset(cops, day==9)

filex<-as.character(copsx$file.name[1])
file.i<-paste(filex,"txt",sep=".")
d<-read.delim(file=file.i,header=TRUE)
dim(d)==c(62,8) #check dim

#index them by file name
id<-rep(filex,dim(d)[1])
dt9<-cbind(id,d)

#combine them in a loop
for(i in seq_along(copsx$file.name)){
  filex<-as.character(copsx$file.name[i])
  file.i<-paste(filex,"txt",sep=".")
  d<-read.delim(file=file.i,header=TRUE)
  dim(d)==c(62,8) #check dim
    
  #index them by file name
  id<-rep(filex,dim(d)[1])
  d2<-cbind(id,d)
  names(d2)<-names(dt9)
  
  dt9<-rbind(dt9,d2) #combine them all
  
}

dt9<-dt9[63:dim(dt9)[1],]
which(table(dt9$id)!=62) #several have incorrect length (<62)
#re-do video analysis?


dt<-rbind(dt5,dt7,dt9)
dt<-subset(dt, Slice.n.!=1) #remove initial position
dt$cop.id<-substr(dt$id, 1, 5) #isolate cop name
dt$day<-as.numeric(substr(dt$id, 7,7)) #isolate day
dt$day<-factor(dt$day)

setwd("F:/Benesh/Research/G by G/GxGserver")
write.table(dt,file="behav_prelim.csv",sep=";")
