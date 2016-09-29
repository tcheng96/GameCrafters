from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [1,2,3,4,5]
else:
    data = []

def filter(x):
	if (x % 2 == 0):
		return True
	else:
		return False

#Scatter
data = comm.scatter(data, root=0)
print("rank", rank, "recieved", data)
data = data + 2

#Filter
data = (filter_condition(data), data)

#Gather
data = comm.gather(data, root=0)

comm.Barrier()

if rank == 0:
    print(data)