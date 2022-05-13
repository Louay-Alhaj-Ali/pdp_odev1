#################################################################################################
#                      Ad & Soyad: Lüey Elhac Ali 
#                      oğrenci numarasi : b201200554
#                      Ödev adı : block zincri
#################################################################################################
import hashlib ##Programda kullanacağımız kütüphaneyi çağırdım 
class LueyCoinBlock:##doviz adi
 def __init__(self,previous_block_hash ,transaciton_list):##önceki blok karma ve islemler listesi
         
         ##Her blok bir önceki bloğa bağlıdır, böylece bloklardan birinde değişiklik yapıldığında bütün de değişir.
         self.previous_block_hash=previous_block_hash
         self.transaciton_list=transaciton_list
      
         self.block_data="______________".join(transaciton_list) + "______________" + previous_block_hash
         self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()
    
         self.block_data="______________".join(transaciton_list) + "______________" + previous_block_hash #her islemler ayni listede toplanir
         self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest() # burasi verileri kodalanacak
         
         
    #islemler#
a1 = "luey sends 7 LC to his teacher"
a2 = "luey sends 3.7 LC to his brother"
a3 = "luey's teacher sends 15.02 LC to his son"
a4 = "luey sends 15.021 LC to his university"

initial_block = LueyCoinBlock("Initial string", [a1, a2])
initial_block = LueyCoinBlock("Initial string", [a1, a2])#1.blok oluşturduc
 
print(initial_block.block_data)
print(initial_block.block_hash)
print(initial_block.block_data)#işlemler bilgileri gösterir
print(initial_block.block_hash)#şire gösterir

second_block = LueyCoinBlock("Initial string", [a3, a4])
 
print(second_block.block_data )
print(second_block.block_hash)
print(second_block.block_hash)

#Burada en basit değişiklikte şifrelemenin değişeceğini fark ediyoruz.
third_block = LueyCoinBlock("Initial string", [a3])
 
print(third_block.block_data )
print(third_block.block_hash)
fourthly_block = LueyCoinBlock("Initial string", [a4])
 
print(fourthly_block.block_data )
print(fourthly_block.block_hash)