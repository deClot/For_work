import check_branch


def Separate_transitions (J0,Ka0,Kc0,str1,Tr):
    str1=str1[1:78]
    str1=str1.split()

    if len(str1)==6:
        J,Ka,Kc,Trans,I,E=str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)

    elif len(str1)>6 and len(str1)<12:
        J,Ka,Kc,Trans,I,E, *_=str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)
    elif len(str1) == 12:
        J,Ka,Kc,Trans,I,E,*_=str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)

        *_, J,Ka,Kc,Trans,I,E =str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)

#
#    print (Tr.R_Tr, Tr.R_I,Tr.Q_Tr, Tr.Q_I,Tr.P_Tr, Tr.P_I)
