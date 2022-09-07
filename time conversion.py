#time conversion
#cara 1
N = int(input())
hour = N // 3600
minutes = N // 60
second_time = N % 60
print(f"{hour}:{minutes}:{second_time}")



#cara 2 
#memperkecil variabel
N = int(input())
print(f"{N // 3600}:{N // 60}:{N % 60}")
