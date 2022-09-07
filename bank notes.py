#bank_notes
#cara 1

#input
N = int(input()) # N = int(0<N<1000000)

# data
banyak_seratus = N // 100 
banyak_lima_puluh = (N % 100) // 50
banyak_dua_puluh = ((N % 100) % 50) // 20
banyak_sepuluh = (((N % 100) % 50) % 20) // 10
banyak_lima = ((((N % 100) % 50) % 20) % 10) // 5
banyak_dua = (((((N % 100) % 50) % 20) % 10) % 5) // 2
banyak_satu = ((((((N % 100) % 50) % 20) % 10) % 5) % 2) // 1


# output
print(banyak_seratus,"nota(s) de R$ 100,00")
print(banyak_lima_puluh,"nota(s) de R$ 50,00")
print(banyak_dua_puluh,"nota(s) de R$ 20,00")
print(banyak_sepuluh,"nota(s) de R$ 10,00")
print(banyak_lima,"nota(s) de R$ 5,00")
print(banyak_dua,"nota(s) de R$ 2,00")
print(banyak_satu,"nota(s) de R$ 1,00")


