import quan_number

def Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr):
    J,Ka,Kc,Trans,I,E=quan_number.Quantum_numbers (J,Ka,Kc,Trans,I,E)

    if abs(Ka-Ka0)<2 and abs(Kc-Kc0)<2:    # allowed transitions
        if J==J0:
            Tr.Q_Tr.append([Trans,I,J,Ka,Kc])
        elif J<J0:
            Tr.R_Tr.append([Trans,I,J,Ka,Kc])
        elif J>J0:
            Tr.P_Tr.append([Trans,I,J,Ka,Kc])

    else:
        if J<J0:
            if Ka>Ka0:
                Tr.R_Tr_f1.append([Trans,I,J,Ka,Kc])
            else:
                Tr.R_Tr_f2.append([Trans,I,J,Ka,Kc])
        elif J>J0:
            if Ka>Ka0:
                Tr.P_Tr_f1.append([Trans,I,J,Ka,Kc])
            else:
                Tr.P_Tr_f2.append([Trans,I,J,Ka,Kc])
        elif J==J0:
            if Ka>Ka0:
                Tr.Q_Tr_f1.append([Trans,I,J,Ka,Kc])
            else:
                Tr.Q_Tr_f2.append([Trans,I,J,Ka,Kc])
