import separate_transitions

class Transition:
    def __init__(self, J, Ka, Kc):
        self.J = J
        self.Ka= Ka
        self.Kc = Kc
        self.R_Tr = []
        self.Q_Tr = []
        self.P_Tr = []
        self.R_Tr_f1 = []
        self.Q_Tr_f1 = []
        self.P_Tr_f1 = []
        self.R_Tr_f2 = []
        self.Q_Tr_f2 = []
        self.P_Tr_f2 = []
###########################################################

def main_function(src):
   file=open(src, 'r').readlines()
   l=len(file)

   for i in range(l):
       file[i] = file[i].replace('+',' ')
       file[i] = file[i].replace('-',' ')
       file[i] = file[i].replace('?',' ')
       file[i] = file[i].replace('shum',' ')
       file[i] = file[i].replace('out of range',' ')
       file[i] = file[i].replace('vr',' ')
       file[i] = file[i].replace('w',' ')
       file[i] = file[i].replace('I',' ')
       file[i] = file[i].replace('no line',' ')
       file[i] = file[i].replace('_',' ')
       file[i] = file[i].replace('cd',' ')
       file[i] = file[i].replace('p',' ')


       '''with open('result','w') as F:
       F.writelines(file) '''

   count = 0

   for i in range(l):
       str1=file[i]

       if str1.find('Sea',0,len(str1))!=-1:
           str1=str1.split()
           _,J0,Ka0,Kc0,*_=str1 
           J0=int(J0)
           Ka0=int(Ka0)
           Kc0=int(Kc0)

           Up_State1 = Transition(J0, Ka0, Kc0)
           count+=1
           ref = Up_State1
           #file.seek(0) 
           print (str1)
           break
       print (count)

   for i in range(l):
       str1=file[i]

       if str1.find('Sea',0,len(str1))!=-1:
           str1=str1.split()
           _,J0,Ka0,Kc0,*_=str1
           J0=int(J0)
           Ka0=int(Ka0)
           Kc0=int(Kc0)

           print (str1)
           #print (abs(ref.J-J0),abs (ref.Kc-Kc0),ref.Ka,Ka0)
           if abs(ref.J-J0) == abs (ref.Kc-Kc0) and ref.Ka == Ka0:
               continue
           else:
               print ('@')
               if count == 1:
                   Up_State2 = Transition(J0, Ka0, Kc0)
                   count+=1
                   ref = Up_State2
                   continue
               else:
                   if ref == Up_State1:
                       ref = Up_State2
                   elif ref == Up_State2:
                       ref = Up_State1
       else:
           print (str1)
           separate_transitions.Separate_transitions(J0,Ka0,Kc0,str1,ref)

   file2 = open('RESULTS', 'w')

   if count > 1:
       name_list = [Up_State1, Up_State2]
   else: name_list = [Up_State1]

   for name in name_list:
       file2.write('\n\n!!!!!!!!!!!!!\n')
       file2.write('!!!--R Branch--!!!\n')
       for i in range(len(name.R_Tr)):
           if i == 0:
               file2.write('%3d%3d%3d%12.5f %7.3f\n' % (name.R_Tr[i][2],name.R_Tr[i][3],name.R_Tr[i][4],\
                                                        name.R_Tr[i][0], name.R_Tr[i][1]))
           else:
               file2.write('%3d%3d%3d%12.5f %7.3f %9.5f\n' % (name.R_Tr[i][2],name.R_Tr[i][3],name.R_Tr[i][4],\
                                                              name.R_Tr[i][0], name.R_Tr[i][1],\
                                                              name.R_Tr[i][0]-name.R_Tr[i-1][0] ))

       file2.write('\n!!!--Q Branch--!!!\n')
       for i in range(len(name.Q_Tr)):
           if i == 0:
               file2.write('%3d%3d%3d%12.5f %7.3f\n' % (name.Q_Tr[i][2],name.Q_Tr[i][3],name.Q_Tr[i][4],\
                                                        name.Q_Tr[i][0],name.Q_Tr[i][1]))
           else:
               file2.write('%3d%3d%3d%12.5f %7.3f %9.5f\n' % (name.Q_Tr[i][2],name.Q_Tr[i][3],name.Q_Tr[i][4],\
                                                              name.Q_Tr[i][0], name.Q_Tr[i][1],\
                                                     name.Q_Tr[i][0]-name.Q_Tr[i-1][0] ))

   file2.write('\n!!!--P Branch--!!!\n')
   for i in range(len(name.P_Tr)):
       if i == 0:
           file2.write('%3d%3d%3d%12.5f %7.3f\n' % (name.P_Tr[i][2],name.P_Tr[i][3],name.P_Tr[i][4],\
                                                    name.P_Tr[i][0], name.P_Tr[i][1]))
       else:
           file2.write('%3d%3d%3d%12.5f %7.3f %9.5f\n' % (name.P_Tr[i][2],name.P_Tr[i][3],name.P_Tr[i][4],\
                                                          name.P_Tr[i][0], name.P_Tr[i][1],\
                                     name.P_Tr[i][0]-name.P_Tr[i-1][0] ))

   for attribute in [name.P_Tr_f1,name.P_Tr_f2,name.R_Tr_f1,name.R_Tr_f2,\
                      name.Q_Tr_f1,name.Q_Tr_f2]:
       if len(attribute)!=0:
           file2.write('\n!!!--Forbidden Branch--!!!\n')
           for i in range(len(attribute)):
               if i == 0:
                   file2.write('%3d%3d%3d%12.5f %7.3f\n' % (attribute[i][2],attribute[i][3],attribute[i][4],\
                                                            attribute[i][0], attribute[i][1]))
               else:
                   file2.write('%3d%3d%3d%12.5f %7.3f %9.5f\n' % (attribute[i][2],attribute[i][3],attribute[i][4],\
                                                                  attribute[i][0], attribute[i][1],\
                                               attribute[i][0]-attribute[i-1][0]))

   file2.close()




