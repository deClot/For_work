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
def find_previous_energy (branch, file2):
   if branch[0][2] == branch[0][3]:
       return 0
       #file2.write('%3d%3d%3d%12.5f %7.3f\n' % (branch[0][2],branch[0][3],branch[0][4],\
       #                                                 branch[0][0], branch[0][1]))
   elif len(branch)>=3:       
       delta11 = branch[1][0]-branch[0][0]
       delta12 = branch[2][0]-branch[1][0]

       delta2 = delta12 - delta11
       file2.write('%3d%3d%3d%12.5f\n' % (branch[0][2]-1,branch[0][3],branch[0][4]-1,\
                                                              branch[0][0]-delta11+delta2))
   return 0

def find_continiuos_energy (branch,i,file2):
    if i == len(branch)-1:
        file2.write('%3d%3d%3d%12.5f\n' % (branch[i][2]+1,branch[i][3],branch[i][4]+1,\
                                                              branch[i][0]+branch[i][0]-branch[i-1][0]+\
                                                              branch[i][0]-branch[i-1][0]-\
                                                              branch[i-1][0]+branch[i-2][0]))


    return 0


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
       file[i] = file[i].replace('forbidden',' ')
       file[i] = file[i].replace('sliplis',' ')


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

           #print (str1)
           #print (abs(ref.J-J0),abs (ref.Kc-Kc0),ref.Ka,Ka0)
           if abs(ref.J-J0) == abs (ref.Kc-Kc0) and ref.Ka == Ka0:
               continue
           else:
               #print ('@')
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
           separate_transitions.Separate_transitions(J0,Ka0,Kc0,str1,ref)

   file2 = open('For_work/RESULTS', 'w')

   if count > 1:
       name_list = [Up_State1, Up_State2]
   else: name_list = [Up_State1]

   for name in name_list:
       file2.write('\n\n!!!!!!!!!!!!!\n')
       file2.write('!!!--R Branch--!!!\n')
       for i in range(len(name.R_Tr)):
           if i == 0:
               find_previous_energy (name.R_Tr, file2)

               file2.write('%3d%3d%3d%12.5f %7.3f\n' % (name.R_Tr[i][2],name.R_Tr[i][3],name.R_Tr[i][4],\
                                                        name.R_Tr[i][0], name.R_Tr[i][1]))
           elif i==1:
               file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f\n' % (name.R_Tr[i][2],name.R_Tr[i][3],name.R_Tr[i][4],\
                                                              name.R_Tr[i][0], name.R_Tr[i][1],\
                                                              name.R_Tr[i][0]-name.R_Tr[i-1][0]))
           else:
               file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f %9.5f\n' % (name.R_Tr[i][2],name.R_Tr[i][3],name.R_Tr[i][4],\
                                                              name.R_Tr[i][0], name.R_Tr[i][1],\
                                                              name.R_Tr[i][0]-name.R_Tr[i-1][0],\
                                                              name.R_Tr[i][0]-name.R_Tr[i-1][0]-\
                                                              name.R_Tr[i-1][0]+name.R_Tr[i-2][0] ))
           find_continiuos_energy (name.R_Tr,i,file2)

       file2.write('\n!!!--Q Branch--!!!\n')
       for i in range(len(name.Q_Tr)):
           if i == 0:
               find_previous_energy (name.Q_Tr, file2)             
               file2.write('%3d%3d%3d%12.5f %7.3f\n' % (name.Q_Tr[i][2],name.Q_Tr[i][3],name.Q_Tr[i][4],\
                                                        name.Q_Tr[i][0],name.Q_Tr[i][1]))
           elif i==1:
               file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f\n' % (name.Q_Tr[i][2],name.Q_Tr[i][3],name.Q_Tr[i][4],\
                                                              name.Q_Tr[i][0], name.Q_Tr[i][1],\
                                                     name.Q_Tr[i][0]-name.Q_Tr[i-1][0] ))
           else:
               file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f %9.5f\n' % (name.Q_Tr[i][2],name.Q_Tr[i][3],name.Q_Tr[i][4],\
                                                              name.Q_Tr[i][0], name.Q_Tr[i][1],\
                                                              name.Q_Tr[i][0]-name.Q_Tr[i-1][0],\
                                                              name.Q_Tr[i][0]-name.Q_Tr[i-1][0]-\
                                                              name.Q_Tr[i-1][0]+name.Q_Tr[i-2][0] ))
           find_continiuos_energy (name.Q_Tr,i,file2) 

       file2.write('\n!!!--P Branch--!!!\n')
       for i in range(len(name.P_Tr)):
           if i == 0:
               find_previous_energy (name.P_Tr, file2)
               file2.write('%3d%3d%3d%12.5f %7.3f\n' % (name.P_Tr[i][2],name.P_Tr[i][3],name.P_Tr[i][4],\
                                                    name.P_Tr[i][0], name.P_Tr[i][1]))
           elif i==1:
               file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f\n' % (name.P_Tr[i][2],name.P_Tr[i][3],name.P_Tr[i][4],\
                                                              name.P_Tr[i][0], name.P_Tr[i][1],\
                                                              name.P_Tr[i][0]-name.P_Tr[i-1][0] ))
           else:
               file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f %9.5f\n' % (name.P_Tr[i][2],name.P_Tr[i][3],name.P_Tr[i][4],\
                                                              name.P_Tr[i][0], name.P_Tr[i][1],\
                                                              name.P_Tr[i][0]-name.P_Tr[i-1][0],\
                                                              name.P_Tr[i][0]-name.P_Tr[i-1][0]-\
                                                              name.P_Tr[i-1][0]+name.P_Tr[i-2][0] ))
           find_continiuos_energy (name.P_Tr,i,file2)

   for attribute in [name.P_Tr_f1,name.P_Tr_f2,name.R_Tr_f1,name.R_Tr_f2,\
                      name.Q_Tr_f1,name.Q_Tr_f2]:
       if len(attribute)!=0:
           file2.write('\n!!!--Forbidden Branch--!!!\n')
           for i in range(len(attribute)):
               if i == 0:
                   file2.write('%3d%3d%3d%12.5f %7.3f\n' % (attribute[i][2],attribute[i][3],attribute[i][4],\
                                                            attribute[i][0], attribute[i][1]))
               elif i==1:
                   file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f\n' % (attribute[i][2],attribute[i][3],attribute[i][4],\
                                                                  attribute[i][0], attribute[i][1],\
                                                                  attribute[i][0]-attribute[i-1][0]))
               else:
                   file2.write('%3d%3d%3d%12.5f %7.3f| %9.5f %9.5f\n' % (attribute[i][2],attribute[i][3],attribute[i][4],\
                                                                         attribute[i][0], attribute[i][1],\
                                                                         attribute[i][0]-attribute[i-1][0],\
                                                                         attribute[i][0]-attribute[i-1][0]\
                                                                         -attribute[i-1][0]+attribute[i-2][0] ))


   file2.close()




