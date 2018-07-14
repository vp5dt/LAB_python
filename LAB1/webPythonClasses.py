web=["bhavesh","kranthi","yuvesh","kiran"];
python=["bhavesh","kranthi","vinay","sirisha"];
def common(web,python):
    comm=[]
    notcomm=web+python
    comm=set(web).intersection(python)
    #for i in range(len(web)):
     #   for j in range(len(python)):
      #      if(web[i]==python[j]):
       #         comm.append(web[i])
    notcomm=list(set(notcomm)-set(comm))
    print("Common Students in both the classes:")
    print(comm)
    print("Not Common Students in both the classes:")
    print(notcomm)


common(web,python)