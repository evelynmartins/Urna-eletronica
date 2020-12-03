# -*- coding: utf-8 -*-
#Criar um programa simulando a urna eletronica. Deve receber uma lista de
# de cadastros de "titulos de eleitor" e consultar essa lista. Se estiver}
# na lista, deve pedir o numero dos candidatos. Mostrar o nome pelo numero digita
# o candidato e pedir a confirmação. Depois do voto em todos os candidatos, 
# Fazer o somatorio de votos, numero de absteções 

candipres={"Boulos":50, "Ciro":12, "Moro":25 }
candgov={"Tarcisio":50,"Benedita":13,"Romário":12}
Boulos=0
Ciro=0
Moro=0
nulop=0
Brancop=0
Tarsicio=0
Benedita=0
Romário=0
nulog=0
Brancog=0
eleitores= [123001, 123002, 123003, 123004, 123005, 123006, 123007, 123008, 123009, 123010, 123011, 123012, 123013, 123014, 123015, 123016, 123017, 123018, 123019, 123020, 123021, 123022, 123023, 123024, 123025, 123026, 123027, 123028, 123029, 123030, 123031, 123032, 123033, 123034, 123035, 123036, 123037, 123038, 123039, 123040, 123041, 123042, 123043, 123044, 123045, 123046, 123047, 123048, 123049, 123050, 123051, 123052, 123053, 123054, 123055, 123056, 123057, 123058, 123059, 123060, 123061, 123062, 123063, 123064, 123065, 123066, 123067, 123068, 123069, 123070, 123071, 123072, 123073, 123074, 123075, 123076, 123077, 123078, 123079, 123080, 123081, 123082, 123083, 123084, 123085, 123086, 123087, 123088, 123089, 123090, 123091, 123092, 123093, 123094, 123095, 123096, 123097, 123098, 123099, 123100, 123101, 123102, 123103, 123104, 123105, 123106, 123107, 123108, 123109, 123110, 123111, 123112, 123113, 123114, 123115, 123116, 123117, 123118, 123119, 123120, 123121, 123122, 123123, 123124, 123125, 123126, 123127, 123128, 123129, 123130, 123131, 123132, 123133, 123134, 123135, 123136, 123137, 123138, 123139, 123140, 123141, 123142, 123143, 123144, 123145, 123146, 123147, 123148, 123149]
votantes=[]

while True:
    tit=int(input("Digite o número do título de eleitor: "))
    if tit == 0:
     break   
    elif tit not in eleitores:
     tit=int(input("Título inválido. Digite o número do título de eleitor válido: "))        
    
    else:      
     print("Eleitor válido. Siga para a urna eletronica.")
    votantes.append(tit)
    votopres=int(input("Qual o seu voto para presidente? "))
    if votopres == 50:
     Boulos=Boulos+1
    elif votopres == 12:
        Ciro=Ciro+1
    elif votopres == 25:
        Moro=Moro+1
    elif votopres == 0:
        Brancop=Brancop+1
    else:
        nulop=nulop+1
        
    votogov=int(input("Qual o seu voto para Governador? "))
    if votogov == 50:
     Tarsicio=Tarsicio+1
    elif votogov == 12:
        Romário=Romário+1
    elif votogov == 13:
        Benedita=Benedita+1
    elif votogov == 0:
        Brancog=Brancog+1
    else:
        nulog=nulog+1
        
    print("FIM")

    
    
boulp= Boulos*100/total    
ele=len(eleitores)
total=(Boulos+Ciro+Moro+Brancop+nulop)
Abstenção=len(eleitores)-total
vot=len(votantes)
print("Apuração:")
print("--------------------------------")
print("Essa sessão tem %d eleitores. "%ele)
print("Tivemos %d Votantes. "%vot)
print("--------------------------------")
print("Resultado presidente:")    
print("O candidato Boulos teve %d votos." %Boulos)
print("O candidato Ciro teve %d votos." %Ciro)
print("O candidato Moro teve %d votos." %Moro)
print("Tivemos %d votos em branco." %Brancop)
print("Tivemos %d votos nulos." %nulop)
print("Tivemos %d abstênções." %Abstenção)
print("--------------------------------")
print("Resultado governardor:")    
print("O candidato Tarsicio teve %d votos." %Tarsicio)
print("A candidata Benedita teve %d votos." %Benedita)
print("O candidato Romário teve %d votos." %Romário)
print("Tivemos %d votos em branco." %Brancog)
print("Tivemos %d votos nulos." %nulog)
print("Tivemos %d abstênções." %Abstenção)
print(boulp)




#falta:
# consultar se já votou
# consultar se é valido mas pertence a outra sessão
# calcular os percentuais