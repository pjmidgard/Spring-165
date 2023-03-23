from time import time
cvf=0
import os
import binascii
namez = input("c  for compress or e for extract: ")
#@Author Jurijus Pacalovas
class compression:
    def cryptograpy_compression(self):
                

        
            
    
                self.name = "@Author: Jurijus Pacalovas"
                print(self.name)
                if namez=="e":
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                           print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit                    
                    namea=""
                    namem=""
                    namema="?"
                    Times_of_compression1=0
                    blockw=5
                    blockw1=4
                    assxw1=0
                    assxw2=0
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    
                    nac=len(nameas)

                    Times_of_compression=0
                    
                    countraz=0
                    assxw=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    count4=1
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=2
                    block2=0

                    count_time_of_copression=0

                    x=0
                    x1=0
                    x2=0
                    x = time()

            
                    
                    with open(nameas, "w") as f4:
                            f4.write(s)
                   
                    with open(name, "rb") as binary_file:

           
                  
                        # Read the whole file at once
                        
                        data = binary_file.read()
                        import paq
                        data= paq.decompress(data)
                        
                        s=str(data)
                        
            
                  
                        lenf1=len(data)
                        lenf5=len(data)
                        
            
                  
                        
                        if lenf1>(2**32)-1:
                            print("This file is too big");
                            raise SystemExit
                        if lenf1==0:
                            
                            raise SystemExit

                        assx=0
                        qqqwz=0
                        
            
                   
                        while assx<10:
                       
                            aas1=0
                            a1=0

                
           
                    
                            cvf=cvf+1
                            
                
                    
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

      
                                    
                                    
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                    
                                
                                    
                                    if countraz==1:

                                        
                                        
                                        

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1


                                    
                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(len(sda2))
                                assxw=1
                                if assxw==1:
                                            assxw1=0
                                            #print(count4)
                                            
                                            while assxw1!=50:
                                                    assxw=0
                                                    sda3=""
                                                    sda5=""
                                                    sda8=""
                                                    sda4=""
                                                    block3=0
                                                    lenf2=len(sda2)
                                                 
                                                   
                                                    count4=1
                                                    while block3<lenf2:
                                                        count4+=1
                                                        e5=sda2[block3:block3+8]


                                                        Reverse=0
                                                        #print(e5)
                                                        e11=""

                                                        
                                                           
                                                        
                                                

                                                        while e5!=e11:

                                                            if Reverse==256:
                                                                Reverse=0

                                                            e4=format(Reverse,'08b')
                                                            
                                        
                                       
                                                            
                                                            e6=e4
                                                            #print(e6)
                                                            e10=e4[:3]+e4[3:5][::-1]+e4[5:]
                                                            e4=e10[::-1]
                                                            e14=e4
                                                            if e4[0:2]=="01" and count4==5:
                                                                    e4=e4[2:]
                                                                    e7="11"+e4
                                                            elif e4[0:2]=="01" and count4==6:
                                                                    e4=e4[2:]
                                                                    e7="11"+e4
                                                                    

                                                            
                                                            elif e4[0:2]=="10" and count4==5:
                                                                    e4=e4[2:]
                                                                    e7="00"+e4
                                                            elif e4[0:2]=="10" and count4==6:
                                                                    e4=e4[2:]
                                                                    e7="10"+e4
                                                                    
                                                            elif e4[0:2]=="00" and count4==5:
                                                                    e4=e4[2:]
                                                                    e7="10"+e4
                                                            elif e4[0:2]=="00" and count4==6:
                                                                    e4=e4[2:]
                                                                    e7="01"+e4      
                                                            
                                                            elif e4[0:2]=="11" and count4==5:
                                                                    e4=e4[2:]
                                                                    e7="01"+e4
                                                            elif e4[0:2]=="11" and count4==6:
                                                                    e4=e4[2:]
                                                                    e7="00"+e4  
                                                           
                                                                  
                                                                    
                                                          
                                                                                                                              
                                                            
                                                            
                                                            elif e4[0:2]=="00" and count4==1:
                                                              
                                                                e4=e4[2:]

                                                                
                                                                e7="00"+e4
                                                                
                                                              
                                                            elif e4[0:2]=="01" and count4==2:
                                                                e4=e4[2:]

                                                                
                                                                e7="00"+e4
                                                                
                                                                
                                                            elif e4[0:2]=="10" and count4==3:
                                                                e4=e4[2:]

                                                                
                                                                e7="00"+e4
                                                                
                                                              
                                                            elif e4[0:2]=="11" and count4==4:
                                                                e4=e4[2:]

                                                                
                                                                e7="00"+e4
                                                                
                                                                                           

                                                            elif e4[0:2]=="01" and count4==1:
                                                              
                                                                e4=e4[2:]

                                                                
                                                                e7="01"+e4
                                                                
                                                            
                                                            elif e4[0:2]=="10" and count4==2:
                                                                e4=e4[2:]

                                                                
                                                                e7="01"+e4
                                                                
                                                                
                                                                
                                                            elif e4[0:2]=="11" and count4==3:
                                                                e4=e4[2:]

                                                                
                                                                e7="01"+e4
                                                               
                                                            elif e4[0:2]=="00" and count4==4:
                                                                e4=e4[2:]

                                                                
                                                                e7="01"+e4
                                                                
                                                                                          

                                                            elif e4[0:2]=="10" and count4==1:
                                                              
                                                                e4=e4[2:]

                                                                
                                                                e7="10"+e4
                                                               
                                                            elif e4[0:2]=="11" and count4==2:
                                                                e4=e4[2:]

                                                                
                                                                e7="10"+e4
                                                            
                                                                
                                                            elif e4[0:2]=="01" and count4==3:
                                                                e4=e4[2:]

                                                                
                                                                e7="10"+e4
                                                            
                                                            elif e4[0:2]=="01" and count4==4:
                                                                e4=e4[2:]

                                                                
                                                                e7="10"+e4
                                                                
                                                                        

                                                            elif e4[0:2]=="11" and count4==1:
                                                              
                                                                e4=e4[2:]

                                                                
                                                                e7="11"+e4
                                                               
                                                            elif e4[0:2]=="00" and count4==2:
                                                                e4=e4[2:]

                                                                
                                                                e7="11"+e4
                                                                
                                                                
                                                            elif e4[0:2]=="00" and count4==3:
                                                                e4=e4[2:]

                                                                
                                                                e7="11"+e4
                                                                
                                                                
                                                            elif e4[0:2]=="10" and count4==4:
                                                                e4=e4[2:]

                                                                
                                                                e7="11"+e4
                                                                
                                                                                    
                                                            e11=e7
                                                            #print(e11)
                                                            #if len(e11)!=8:
                                                                #print(e11)

                                                        
                                                            #print(e12)
                                                            Reverse+=1
                                                            #print(e11)
                                                            
                                                            #print(e11)
                                                        sda3+=e6
                                                        if count4==6:
                                                            count4=1
                                                        	 
                                                       
                                                        #print(count4)
                                                        block3+=8
	                                           
	                                            #print(e5)
	                                            
	                        
	                                            #print(len(sda3))
                                                                                          
	                                              
	                                            #print(sda2)
                                                    
	                                            
                                                    sda2=sda3
                                                    #print(sda2)
                                                    assxw1=assxw1+1
                                                    #print(assxw1)
                                                    
                                            #print(jl)
                                            #print(Times_of_compression1)

                                            #print(count4)
                                                    if assxw1==1:
                                                            assxw1=0
                                                            assxw=0

                                                            n = int(sda3, 2)
                                                            qqwslenf=len(sda3)
                                                            qqwslenf=(qqwslenf/8)*2
                                                            qqwslenf=str(qqwslenf)
                                                            qqwslenf="%0"+qqwslenf+"x"
                                                            jl=binascii.unhexlify(qqwslenf % n)
                                                            
                                                            assxw2=1
                                                            if assxw2==1:
                                                                assx=10
                                                                if assx==10:
                                                                    f2.write(jl)
                                                                    x2 = time()
                                                                    x3=x2-x
                                                                    return print(x3)
                            

                           
    
            
    def cryptograpy_unpack(self):                       
                    if namez=="c":
                        name = input("What is name of file? ")
                        if os.path.exists(name):
                           print('Path is exists!')
                        else:
                            print('Path is not exists!')
                            raise SystemExit
                        namea=""
                        namem=""
                        namema="?"
                        block2=0
                        
                        count1=12
                        count2=0
                        count3=0
                        count4=1
                        count6=0
                        assxw1=0
                        Times_of_compression=0
                        assxw2=0
              

                        assxw=0
                        blockw=5
                        blockw1=4
                        nameas=name
                        
                        nac=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
                        countraz=0
                        cvf=2
                        cvf1=0
                        s=""
                        e2=0
                        e3=2
                        e4=""
                        c=2
                        sw=2
                        elw=0
                       
                        sda3=""

                        sscvf=0
                        
                        qqqqwzl=0

                        block=0

                        x=0
                        x1=0
                        x2=0
                        x = time()
                       
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            
                            data = binary_file.read()

                        
                            s=str(data)
                            lenf1=len(data)
                            lenf5=len(data)
                            
                            if lenf1>(2**32)-1:
                                print("This file is too big");
                                raise SystemExit
                            if lenf1==0:
                            	raise SystemExit
                            
                            assx=0
                            
                            qqqwz=0
                            while assx<10:
                          
                                aas1=0
                                a1=0
                                
                                cvf=cvf+1
                                
                                countraz=countraz+1

                                with open(nameas, "ab") as f2:
                                    if countraz==1:
                                        sda=bin(int(binascii.hexlify(data),16))[2:]
                                        lenf=len(sda)
                                        
                                        lenf1=len(data) 
                                        xc=(lenf1*8)-lenf
                                        z=0
                                        if xc!=0:
                                            while z<xc:
                                                sda="0"+sda
                                                z=z+1
                                        sda2=sda
                                        lenf3=len(sda2)
                                    lenf2=len(sda2)  
                                    block3=0
                                    sda3=""
                                    sda5=""
                                    sda8=""
                                    sda4=""
                                    
                                    count3+=1
                                    #print(count4)
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                    #print(len(sda2))
                                  
                                   
                                    count4=1
                                    while block3<lenf2:
                                        count4+=1
                                       
                                        e4=sda2[block3:block3+8]
                                        e6=e4
                                        e10=e4[:3]+e4[3:5][::-1]+e4[5:]
                                        e4=e10[::-1]
                                        e14=e4

                                        
                                        
                                        if e4[0:2]=="01" and count4==5:
                                                e4=e4[2:]
                                                sda3+="11"+e4
                                                block3+=8
                                        elif e4[0:2]=="01" and count4==6:
                                                e4=e4[2:]
                                                sda3+="11"+e4
                                                block3+=8
                                                                    

                                                            
                                        elif e4[0:2]=="10" and count4==5:
                                                e4=e4[2:]
                                                sda3+="00"+e4
                                                block3+=8
                                        elif e4[0:2]=="10" and count4==6:
                                                e4=e4[2:]
                                                sda3+="10"+e4
                                                block3+=8
                                                                    
                                        elif e4[0:2]=="00" and count4==5:
                                                e4=e4[2:]
                                                sda3+="10"+e4
                                                block3+=8
                                        elif e4[0:2]=="00" and count4==6:
                                                e4=e4[2:]
                                                sda3+="01"+e4
                                                block3+=8
                                                            
                                        elif e4[0:2]=="11" and count4==5:
                                                e4=e4[2:]
                                                sda3+="01"+e4
                                                block3+=8
                                        elif e4[0:2]=="11" and count4==6:
                                                e4=e4[2:]
                                                sda3+="00"+e4
                                                block3+=8
                                  
                                   
                                   
                                        
                                        
                                        
                                        elif e4[0:2]=="00" and count4==1:
                                          
                                            e4=e4[2:]

                                            
                                            sda3+="00"+e4
                                            block3+=8
                                          
                                        elif e4[0:2]=="01" and count4==2:
                                            e4=e4[2:]

                                            
                                            sda3+="00"+e4
                                            block3+=8
                                            
                                        elif e4[0:2]=="10" and count4==3:
                                            e4=e4[2:]

                                            
                                            sda3+="00"+e4
                                            block3+=8
                                          
                                        elif e4[0:2]=="11" and count4==4:
                                            e4=e4[2:]

                                            
                                            sda3+="00"+e4
                                            block3+=8
                                                                       

                                        elif e4[0:2]=="01" and count4==1:
                                          
                                            e4=e4[2:]

                                            
                                            sda3+="01"+e4
                                            block3+=8
                                            
                                        elif e4[0:2]=="10" and count4==2:
                                            e4=e4[2:]

                                            
                                            sda3+="01"+e4
                                            block3+=8
                                            
                                            
                                        elif e4[0:2]=="11" and count4==3:
                                            e4=e4[2:]

                                            
                                            sda3+="01"+e4
                                            block3+=8
                                        elif e4[0:2]=="00" and count4==4:
                                            e4=e4[2:]

                                            
                                            sda3+="01"+e4
                                            block3+=8
                                                                      

                                        elif e4[0:2]=="10" and count4==1:
                                          
                                            e4=e4[2:]

                                            
                                            sda3+="10"+e4
                                            block3+=8
                                        elif e4[0:2]=="11" and count4==2:
                                            e4=e4[2:]

                                            
                                            sda3+="10"+e4
                                            block3+=8
                                            
                                        elif e4[0:2]=="01" and count4==3:
                                            e4=e4[2:]

                                            
                                            sda3+="10"+e4
                                            block3+=8
                                        elif e4[0:2]=="01" and count4==4:
                                            e4=e4[2:]

                                            
                                            sda3+="10"+e4
                                            block3+=8
                                                    

                                        elif e4[0:2]=="11" and count4==1:
                                          
                                            e4=e4[2:]

                                            
                                            sda3+="11"+e4
                                            block3+=8
                                        elif e4[0:2]=="00" and count4==2:
                                            e4=e4[2:]

                                            
                                            sda3+="11"+e4
                                            block3+=8
                                            
                                        elif e4[0:2]=="00" and count4==3:
                                            e4=e4[2:]

                                            
                                            sda3+="11"+e4
                                            block3+=8
                                            
                                        elif e4[0:2]=="10" and count4==4:
                                            e4=e4[2:]

                                            
                                            sda3+="11"+e4
                                            block3+=8
                                            
                                        #print(len(sda3))
                                    	
             
                                        if count4==6:
                                            count4=1
                                   
                                    #print(count4)
                                    
          	
                                    #print(sda3)
                                    #os.system("pause")
                                    
                                    sda2=sda3
                                    #n = int(sda2, 2)
                                                                                                    
                                            
                                    #n = int(sda2, 2)                                                                                     
                                            
                                    #qqwslenf=len(sda2)
                                    #qqwslenf=(qqwslenf/8)*2
                                    #qqwslenf=str(qqwslenf)
                                    #qqwslenf="%0"+qqwslenf+"x"
                                    ##jl=binascii.unhexlify(qqwslenf % n)
                                    #print(len(jl))
                                    #import paq
                                    #jl= paq.compress(jl)
                                    #print(len(jl))
                                    assxw=assxw+1
                                    print(assxw)
                                    if assxw==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(sda2)
                                        #os.system("pause")
                                        
                                        
                                            
               
                                        n = int(sda3, 2)
                                        qqwslenf=len(sda3)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                        jl=binascii.unhexlify(qqwslenf % n)
                                        import paq
                                        jl= paq.compress(jl)
                                        #print(len(jl))
                                            
                                      
                                        assxw1=1
                                     
                                            
                                            
                                            #print(assxw1)
                                            
                                        if assxw1==1:
                                        
                                                assx=10
                                                if assx==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)        
                                                                                  														    
                                         



   
            
                     

d=compression()


  
xw=d.cryptograpy_compression()
print(xw)


xw1=d.cryptograpy_unpack()
print(xw1)
