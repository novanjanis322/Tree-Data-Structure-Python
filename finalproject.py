import os
class Tree:
    def __init__(self,datanama, datanomor):
        self.datanama = datanama
        self.datanomor = datanomor
        self.left = None
        self.right = None

    def inputdata_man(self, name, phonenumber):
        if self.left is None:
            self.left = Tree(name, phonenumber)
            print(f'berhasil menambahkan {self.left.datanama} dengan nomor {self.left.datanomor} ke dalam data konsumen pria.')  
        else:
            self.rekursive_inputdata_man(name,phonenumber, self.left)

    def rekursive_inputdata_man(self, name, phonenumber, node):
            if node.left is None:
                node.left=Tree(name, phonenumber)
                print(f"berhasil menambahkan {node.left.datanama} dengan nomor {node.left.datanomor} ke dalam data konsumen pria.")
            else:
                if node.right is None:
                    node.right=Tree(name, phonenumber)
                    print(f"berhasil menambahkan {node.right.datanama} dengan nomor {node.right.datanomor} ke dalam data konsumen pria.")
                else:
                    self.rekursive_inputdata_man(name, phonenumber, node.left)
            
    def inputdata_woman(self, name, phonenumber):
        if self.right is None:
            self.right = Tree(name, phonenumber)
            print(f'berhasil menambahkan {self.right.datanama} dengan nomor {self.right.datanomor} ke dalam data konsumen wanita.') 
        else:
            self.rekursive_inputdata_woman(name,phonenumber, self.right)

    def rekursive_inputdata_woman(self, name, phonenumber, node):
            if node.right is None:
                node.right=Tree(name, phonenumber)
                print(f"berhasil menambahkan {node.right.datanama} dengan nomor {node.right.datanomor} ke dalam data konsumen wanita.")
            else:
                if node.left is None:
                    node.left=Tree(name, phonenumber)
                    print(f"berhasil menambahkan {node.left.datanama}dengan nomor {node.left.datanomor} ke dalam data konsumen wanita.")
                else:
                    self.rekursive_inputdata_woman(name, phonenumber, node.right)               

    def simplesearchdata(self, val):
        if self.left is not None and self.left.datanama.upper()==val.upper():
            return(f"Data {self.left.datanama} ditemukan pada data konsumen pria ")
        if self.right is not None and self.right.datanama.upper()==val.upper():
            return(f"Data {self.right.datanama} ditemukan pada data konsumen wanita")
        elif self.left is None:
            if self.right is not None:
                return self.rekursive_simplesearchright(val, self.right)
        else:
            return self.rekursive_simplesearchleft(val, self.left)
        return(" ")

    def rekursive_simplesearchleft(self, val, node):
        if node.left is None:
            return self.rekursive_simplesearchright(val, self)
        elif node.left is not None and node.left.datanama.upper()==val.upper():
            return(f"Data {node.left.datanama} ditemukan pada data konsumen pria")
        elif node.right is not None and node.right.datanama.upper()==val.upper():
            return(f"Data {node.right.datanama} ditemukan pada data konsumen pria")
        return self.rekursive_simplesearchleft(val, node.left)

    def rekursive_simplesearchright(self, val, node):
        if node.right is None:
            return (f" ")
        elif node.right is not None and node.right.datanama.upper()==val.upper():
            return(f"Data {node.right.datanama} ditemukan pada data konsumen wanita")
        elif node.left is not None and node.left.datanama.upper()==val.upper():
            return(f"Data {node.left.datanama} ditemukan pada data konsumen wanita")
        return self.rekursive_simplesearchright(val, node.right)
        
    def komplekssearchdata(self, val):
        if self.left is not None and  val.upper() in self.left.datanama.upper():
            print(f"Pencarian data kompleks {val} ditemukan pada data konsumen pria [{self.left.datanama}] ")
        if self.left is not None:
            self.rekursive_komplekssearchleft(val, self.left)
        if self.right is not None and val.upper() in self.right.datanama.upper():
            print(f"Pencarian data kompleks {val} ditemukan pada data konsumen wanita [{self.right.datanama}] ")
        if  self.right is not None:
            self.rekursive_komplekssearchright(val, self.right)
       
    def rekursive_komplekssearchleft(self, val, node):
        if node.left is None:
            return
        if node.left is not None and val.upper() in node.left.datanama.upper():
            print(f"Pencarian data kompleks {val} ditemukan pada data konsumen pria [{node.left.datanama}] ")
        if node.right is not None and val.upper() in node.right.datanama.upper():
            print(f"Pencarian data kompleks {val} ditemukan pada data konsumen pria [{node.right.datanama}] ")
        return self.rekursive_komplekssearchleft(val, node.left)

    def rekursive_komplekssearchright(self, val, node):
        if node.right is None:
            return
        if node.right is not None and val.upper() in node.right.datanama.upper():
            print(f"Pencarian data kompleks {val} ditemukan pada data konsumen wanita [{node.right.datanama}] ")
        if node.left is not None and val.upper() in node.left.datanama.upper():
            print(f"Pencarian data kompleks {val} ditemukan pada data konsumen wanita [{node.left.datanama}] ")
        return self.rekursive_komplekssearchright(val, node.right)

    def datakonsumen_man(self):
        if self.left is not None:
            print("Nama\t\t\t\t\t\tNomor Handphone")
            print(f"{self.left.datanama}\t\t\t\t\t\t{self.left.datanomor}")
            self.rekursif_datakonsumen_man(self.left)
        else:
            return
    
    def rekursif_datakonsumen_man(self,node):
        if node.left is not None:
            if node.right is not None:
                print(f"{node.left.datanama}\t\t\t\t\t\t{node.left.datanomor}")
                print(f"{node.right.datanama}\t\t\t\t\t\t{node.right.datanomor}")
            else:
                print(f"{node.left.datanama}\t\t\t\t\t\t{node.left.datanomor}")
            return self.rekursif_datakonsumen_man(node.left)
        elif node.left is None:
            return
            
    def datakonsumen_woman(self):
        if self.right is not None:
            print("Nama\t\t\t\t\t\tNomor Handphone")
            print(f"{self.right.datanama}\t\t\t\t\t\t{self.right.datanomor}")
            self.rekursif_datakonsumen_woman(self.right)
        else:
            return
    
    def rekursif_datakonsumen_woman(self,node):
        if node.right is not None:
            if node.left is not None:
                print(f"{node.right.datanama}\t\t\t\t\t\t{node.right.datanomor}")
                print(f"{node.left.datanama}\t\t\t\t\t\t{node.left.datanomor}")
            else:
                print(f"{node.right.datanama}\t\t\t\t\t\t{node.right.datanomor}")
            return self.rekursif_datakonsumen_woman(node.right)
        elif node.right is None:
            return

tree = Tree("Buku Kontak","Konsumen Toko Maju Jaya")
while True:
    print('''
=============================================================
Program pembuatan data konsumen "Toko Maju Jaya"
=============================================================
1. Input data Konsumen
2. Pencarian "SEDERHANA" data Konsumen (pencarian nama spesifik)
3. Pencarian "KOMPLEKS" data Konsumen
4. Lihat data Konsumen
0. Exit ''')
    try:
        
        pilihmenu=int(input('input menu yang akan dipilih : '))
        if pilihmenu==1:
            os.system('cls')
            print("=========================Input Data=========================")
            jumlahinput=int(input('\nInput jumlah data konsumen yang akan diinput : '))
            while jumlahinput!=0:
                gender, nama, nomor=input("\nInput nama konsumen [(pria/wanita), nama, nomor] : ").split(", ")
                if gender.upper()=="PRIA":
                    tree.inputdata_man(nama, nomor)
                    jumlahinput-=1
                elif gender.upper()=="WANITA":
                    tree.inputdata_woman(nama, nomor)
                    jumlahinput-=1
                else:
                    print("Pastikan input gender adalah pria/wanita. Data tidak ditambahkan.")
            
            print("\nInput data telah selesai.")
        elif pilihmenu==2:
            carinama=input("input nama yang akan dicari : ")
            os.system('cls')
            print("===================Hasil simple search data===================")
            print(tree.simplesearchdata(carinama))
            kembali=input("\ninput apapun untuk kembali ke menu utama : ")
            os.system('cls')
            continue
        
        elif pilihmenu==3:
            carinama_kompleks=input("input data yang akan dicari : ")
            os.system('cls')
            print("==================Hasil kompleks search data==================")
            tree.komplekssearchdata(carinama_kompleks)
            kembali=input("\ninput apapun untuk kembali ke menu utama : ")
            os.system('cls')
            continue
                    
        elif pilihmenu==4:
            os.system('cls')
            print(f"=============={tree.datanama} {tree.datanomor}===============\n")
            print("-----------------------------Pria-------------------------------")
            tree.datakonsumen_man()
            print("----------------------------Wanita------------------------------")
            tree.datakonsumen_woman()
            kembali=input("\ninput apapun untuk kembali ke menu utama : ")
            os.system('cls')
            continue

        elif pilihmenu==0:
            yes_no=input("apakah anda yakin (yes/no) : ")
            if yes_no.upper()=="YES":
                os.system('cls')
                print("program penambahan data telah selesai.")
                break
            elif yes_no.upper()=="NO":
                os.system('cls')
                print("kembali ke menu utama.")
            else:
                os.system('cls')
                print("input tidak sesuai. kembali ke menu utama.")
        else:
            os.system('cls')
            print("Hanya bisa input angka 1-3 dan 0. kembali ke menu utama.")
    except ValueError:
        os.system('cls')
        print("Input tidak tepat. kembali ke menu utama.")
        continue