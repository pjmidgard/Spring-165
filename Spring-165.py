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
                    count4=-1
                 
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
                                            
                                            
                                                assxw=0
                                                sda3=""
                                                sda5=""
                                                sda8=""
                                                sda4=""
                                                block3=0
                                                lenf2=len(sda2)
                                                count4=-1
                                                count1=-1
                                                
                                                while block3<lenf2:
                                                        count4+=1
                                                        count1+=1
                                                        if count1==65535:
                                                        	count4-=65535
                                                        if count1==255:
                                                        	count4-=255
                                                        e4=sda2[block3:block3+16]
                                                        Chanel=format(count4,'016b')
                                                        if e4[0:16]==Chanel and count4==count4:
                                                        	e4="0000000000000000"
                                                        	sda3+=e4
                                                        	block3+=16
                                                        elif e4[0:16]=="0000000000000000" and count4==count4:
                                                        	e4=Chanel
                                                        	sda3+=e4
                                                        	block3+=16
                                                        else:
                                                        	sda3+=e4
                                                        	block3+=16
                                                        if count4==65535:
                                                        	count4=0
                                          
					                                           
	                                            #print(e5)
	                                            
	                        
	                                            #print(len(sda3))
                                                                                          
	                                              
	                                            #print(sda2)
                                                    
                                                                                          
                                                sda2=sda3
                                                    #print(sda2)
                                                assxw1=assxw1+1
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
                        count4=-1
                        count6=0
                        assxw1=0
                        assxw3=0
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
                            
                            if lenf1>(2**26)-1 or  lenf1<(1024):
                                print("This file is too big or is too small");
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
                                    F=0
                                    count4=-1
                                 
                                    lenf2=len(sda2)
                                    #print(lenf2)
                                    N2=-1
                                    N1=1
                                    N5=0
                                    
                                    N8=len(sda2)
                                    while N1!=0:
                                    	N2+=1
                                    	long=len(sda2)
                                    
                                    	
                                    	N=int(sda2[:long-N2],2)
                                    	N5=N//((2**10)-1)
                                    	
                                    	N1=N%((2**10)-1)
                                    	#print(N2)
                                    Bias=bin(N5)[2:]
                                    if N5==0:
                                    	print("Number is  too small")
                                    	raise SystemExit
                                    long61=len(Bias)
                                    long62=len(sda2[long-N2:])
                                    NS=long61
                                    NS1=N8-long62
                                    NS2=NS1-1-long61
                                    Nj=len(bin(N2)[2:])
                                    #print(Nj)
                                    if Nj>(2**5)-1:
                                        print("Number is too big")
                                        raise SystemExit
                                    
                                    
                                    
                                    C="0"+str(5)+"b"
                                    
                                    Bias2=format(Nj,C)   
                                    sda3=Bias+sda3 
                                    #print(Bias)
                                    #print(N5)                       	
                                    
                                   
                                    sda3=Bias+sda2[long-N2:]+Bias2
                                    #print(N2)


                                    
                                    sda2=sda3
                                    #print(len(sda2))
                                    #n = int(sda2, 2)
                                                                                                    
                                            
                                    #n = int(sda2, 2)                                                                                     
                                            
                                    #qqwslenf=len(sda2)
                                    #qqwslenf=(qqwslenf/8)*2
                                    #qqwslenf=str(qqwslenf)
                                    #qqwslenf="%0"+qqwslenf+"x"
                                    #jl=binascii.unhexlify(qqwslenf % n)
                                    #print(len(jl))
                                    #import paq
                                    #jl= paq.compress(jl)
                                    #print(len(jl))
                                    
                                    assxw3+=1  
                                    if len(sda2)<=8184:
                                                                                                                                                                                                                                
														                                                                                      
														                                                                                                                                                                                                                                                                   
											                                                                                        sda3="1"+sda3
											                                                                                        lenf=len(sda3)
											                                                                                        add_bits118=""
											                                                                                        count_bits=8-lenf%8
											                                                                                        z=0
											                                                                                       
											                                                                                        if count_bits!=8:
											                                                                                                while z<count_bits:
											                                                                                                    add_bits118="0"+add_bits118
											                                                                                                    z=z+1
											
											                                                                                                    
											                                        
											                                                                                        
											                                                                                        
											                                                                                        sda3=add_bits118+sda3
											                                                                                        assxw=1
											                                                                                        T=format(assxw3,'032b')
											                                                                                        sda3=T+sda3
                                    
                                    
                                    #print(assxw)
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
                                        #import paq
                                        #jl= paq.compress(jl)
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
